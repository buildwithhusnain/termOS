import os
import sys
import subprocess
import platform
import socket
import threading
import http.server
import socketserver
from colorama import init, Fore

init(autoreset=True)

class TermOS:
    def __init__(self):
        self.os_type = platform.system()
        self.cwd = os.getcwd()
        self.local_server = None
        
    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=self.cwd)
            
            if result.stdout:
                print(Fore.GREEN + result.stdout)
            if result.stderr:
                print(Fore.GREEN + f"Error: {result.stderr}")
            return result.returncode == 0
        except Exception as e:
            print(Fore.GREEN + f"Command failed: {e}")
            return False
    
    def change_directory(self, path):
        try:
            os.chdir(path)
            self.cwd = os.getcwd()
            print(Fore.GREEN + f"Changed to: {self.cwd}")
        except Exception as e:
            print(Fore.GREEN + f"Failed to change directory: {e}")
    
    def show_info(self):
        print(Fore.GREEN + f"OS: {self.os_type}")
        print(Fore.GREEN + f"Current Directory: {self.cwd}")
        print(Fore.GREEN + f"Python: {sys.version}")
        print(Fore.GREEN + f"Local IP: {self.get_local_ip()}")
    
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def connect_network(self, ssid, password=None):
        if self.os_type == "Windows":
            if password:
                cmd = f'netsh wlan connect name="{ssid}" ssid="{ssid}" key="{password}"'
            else:
                cmd = f'netsh wlan connect name="{ssid}"'
        else:
            print(Fore.GREEN + "Network connection on Linux/Mac requires manual setup")
            return
        
        print(Fore.GREEN + f"Connecting to {ssid}...")
        self.run_command(cmd)
    
    def scan_networks(self):
        if self.os_type == "Windows":
            self.run_command("netsh wlan show profiles")
        else:
            self.run_command("iwlist scan | grep ESSID")
    
    def create_hotspot(self, name, password):
        if self.os_type == "Windows":
            self.run_command(f'netsh wlan set hostednetwork mode=allow ssid="{name}" key="{password}"')
            self.run_command("netsh wlan start hostednetwork")
            print(Fore.GREEN + f"Hotspot '{name}' created")
        else:
            print(Fore.GREEN + "Hotspot creation requires additional setup on Linux/Mac")
    
    def stop_hotspot(self):
        if self.os_type == "Windows":
            self.run_command("netsh wlan stop hostednetwork")
            print(Fore.GREEN + "Hotspot stopped")
    
    def start_http_server(self, port=8000):
        try:
            handler = http.server.SimpleHTTPRequestHandler
            self.local_server = socketserver.TCPServer(("", port), handler)
            
            def serve():
                print(Fore.GREEN + f"HTTP server started on {self.get_local_ip()}:{port}")
                print(Fore.GREEN + f"Serving directory: {self.cwd}")
                self.local_server.serve_forever()
            
            server_thread = threading.Thread(target=serve, daemon=True)
            server_thread.start()
            
        except Exception as e:
            print(Fore.GREEN + f"Failed to start server: {e}")
    
    def stop_http_server(self):
        if self.local_server:
            self.local_server.shutdown()
            self.local_server = None
            print(Fore.GREEN + "HTTP server stopped")
        else:
            print(Fore.GREEN + "No server running")
    
    def create_proxy(self, local_port, target_host, target_port):
        def proxy_handler(client_socket):
            try:
                target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target_socket.connect((target_host, target_port))
                
                def forward(source, destination):
                    while True:
                        data = source.recv(4096)
                        if not data:
                            break
                        destination.send(data)
                
                threading.Thread(target=forward, args=(client_socket, target_socket), daemon=True).start()
                threading.Thread(target=forward, args=(target_socket, client_socket), daemon=True).start()
                
            except Exception as e:
                print(Fore.GREEN + f"Proxy error: {e}")
        
        try:
            proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            proxy_socket.bind(('', local_port))
            proxy_socket.listen(5)
            
            print(Fore.GREEN + f"Proxy server started on port {local_port} -> {target_host}:{target_port}")
            
            def accept_connections():
                while True:
                    client_socket, addr = proxy_socket.accept()
                    threading.Thread(target=proxy_handler, args=(client_socket,), daemon=True).start()
            
            threading.Thread(target=accept_connections, daemon=True).start()
            
        except Exception as e:
            print(Fore.GREEN + f"Failed to create proxy: {e}")
    
    def network_status(self):
        if self.os_type == "Windows":
            self.run_command("ipconfig")
            self.run_command("netsh wlan show interfaces")
        else:
            self.run_command("ifconfig")
            self.run_command("iwconfig")
    
    def start(self):
        print(Fore.GREEN + f"TermOS - Cross-Platform Terminal ({self.os_type})")
        print(Fore.GREEN + "Type 'help' for commands, 'exit' to quit")
        
        while True:
            try:
                cmd = input(Fore.GREEN + f"{self.cwd}> ").strip()
                
                if cmd == "exit":
                    break
                elif cmd == "help":
                    print(Fore.GREEN + "Basic Commands: cd <path>, info, clear, exit")
                    print(Fore.GREEN + "Network Commands:")
                    print(Fore.GREEN + "  net-scan - Scan available networks")
                    print(Fore.GREEN + "  net-connect <ssid> [password] - Connect to network")
                    print(Fore.GREEN + "  net-hotspot <name> <password> - Create hotspot")
                    print(Fore.GREEN + "  net-stop-hotspot - Stop hotspot")
                    print(Fore.GREEN + "  net-status - Show network status")
                    print(Fore.GREEN + "  http-server [port] - Start HTTP server (default: 8000)")
                    print(Fore.GREEN + "  http-stop - Stop HTTP server")
                    print(Fore.GREEN + "  proxy <local_port> <target_host> <target_port> - Create proxy")
                    print(Fore.GREEN + "Or run any OS command directly")
                elif cmd.startswith("cd "):
                    self.change_directory(cmd[3:])
                elif cmd == "info":
                    self.show_info()
                elif cmd == "clear":
                    os.system("cls" if self.os_type == "Windows" else "clear")
                elif cmd == "net-scan":
                    self.scan_networks()
                elif cmd.startswith("net-connect "):
                    parts = cmd.split()
                    if len(parts) >= 2:
                        ssid = parts[1]
                        password = parts[2] if len(parts) > 2 else None
                        self.connect_network(ssid, password)
                elif cmd.startswith("net-hotspot "):
                    parts = cmd.split()
                    if len(parts) >= 3:
                        self.create_hotspot(parts[1], parts[2])
                    else:
                        print(Fore.GREEN + "Usage: net-hotspot <name> <password>")
                elif cmd == "net-stop-hotspot":
                    self.stop_hotspot()
                elif cmd == "net-status":
                    self.network_status()
                elif cmd.startswith("http-server"):
                    parts = cmd.split()
                    port = int(parts[1]) if len(parts) > 1 else 8000
                    self.start_http_server(port)
                elif cmd == "http-stop":
                    self.stop_http_server()
                elif cmd.startswith("proxy "):
                    parts = cmd.split()
                    if len(parts) >= 4:
                        self.create_proxy(int(parts[1]), parts[2], int(parts[3]))
                    else:
                        print(Fore.GREEN + "Usage: proxy <local_port> <target_host> <target_port>")
                elif cmd:
                    self.run_command(cmd)
                    
            except KeyboardInterrupt:
                print(Fore.GREEN + "\nUse 'exit' to quit")
            except EOFError:
                break

def main():
    """Main entry point for console script."""
    terminal = TermOS()
    terminal.start()

if __name__ == "__main__":
    main()
