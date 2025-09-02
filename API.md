# TermOS API Documentation

## Class: TermOS

Main class that provides terminal functionality with network features.

### Constructor

```python
TermOS()
```

Initializes the terminal with current OS detection and working directory.

**Attributes:**
- `os_type`: Current operating system (Windows/Linux/Darwin)
- `cwd`: Current working directory
- `local_server`: HTTP server instance (None when not running)

### Core Methods

#### `run_command(command: str) -> bool`
Execute system commands and display output.

**Parameters:**
- `command`: Command string to execute

**Returns:**
- `bool`: True if command succeeded, False otherwise

**Example:**
```python
terminal = TermOS()
success = terminal.run_command("ls -la")
```

#### `change_directory(path: str) -> None`
Change current working directory.

**Parameters:**
- `path`: Target directory path

**Example:**
```python
terminal.change_directory("/home/user/documents")
```

#### `show_info() -> None`
Display system information including OS, directory, Python version, and local IP.

### Network Methods

#### `get_local_ip() -> str`
Get the local IP address of the machine.

**Returns:**
- `str`: Local IP address or "127.0.0.1" if detection fails

#### `connect_network(ssid: str, password: str = None) -> None`
Connect to a WiFi network.

**Parameters:**
- `ssid`: Network name
- `password`: Network password (optional for open networks)

**Platform Support:**
- Windows: Full support via netsh
- Linux/macOS: Manual setup required

#### `scan_networks() -> None`
Scan and display available WiFi networks.

**Platform Support:**
- Windows: Uses `netsh wlan show profiles`
- Linux: Uses `iwlist scan`

#### `create_hotspot(name: str, password: str) -> None`
Create a WiFi hotspot.

**Parameters:**
- `name`: Hotspot SSID
- `password`: Hotspot password

**Platform Support:**
- Windows: Full support
- Linux/macOS: Limited support

#### `stop_hotspot() -> None`
Stop the currently running WiFi hotspot.

**Platform Support:**
- Windows: Full support

#### `network_status() -> None`
Display current network configuration and status.

**Platform Support:**
- Windows: Uses `ipconfig` and `netsh`
- Linux/macOS: Uses `ifconfig` and `iwconfig`

### Server Methods

#### `start_http_server(port: int = 8000) -> None`
Start HTTP file server on specified port.

**Parameters:**
- `port`: Server port (default: 8000)

**Features:**
- Serves files from current directory
- Runs in background thread
- Accessible from local network

#### `stop_http_server() -> None`
Stop the running HTTP server.

#### `create_proxy(local_port: int, target_host: str, target_port: int) -> None`
Create a proxy server that forwards traffic.

**Parameters:**
- `local_port`: Local port to listen on
- `target_host`: Target server hostname/IP
- `target_port`: Target server port

**Features:**
- Bidirectional traffic forwarding
- Multiple concurrent connections
- Background operation

### Main Loop

#### `start() -> None`
Start the interactive terminal session.

**Features:**
- Command prompt with current directory
- Built-in command processing
- Graceful exit handling
- Keyboard interrupt handling

## Command Reference

### Basic Commands
- `help` - Show command help
- `info` - Display system information
- `clear` - Clear terminal screen
- `exit` - Exit TermOS
- `cd <path>` - Change directory

### Network Commands
- `net-scan` - Scan WiFi networks
- `net-connect <ssid> [password]` - Connect to WiFi
- `net-hotspot <name> <password>` - Create hotspot
- `net-stop-hotspot` - Stop hotspot
- `net-status` - Show network status

### Server Commands
- `http-server [port]` - Start HTTP server
- `http-stop` - Stop HTTP server
- `proxy <local_port> <target_host> <target_port>` - Create proxy

## Error Handling

All methods include comprehensive error handling:
- Network operations catch connection failures
- File operations handle permission errors
- Server operations manage port conflicts
- Command execution captures stderr output

## Threading

Background operations use daemon threads:
- HTTP server runs in separate thread
- Proxy connections use thread per client
- Server threads automatically terminate on exit

## Security Considerations

- HTTP server only serves current directory
- Proxy server inherits user permissions
- Network operations may require elevated privileges
- No authentication on HTTP server (local network only)