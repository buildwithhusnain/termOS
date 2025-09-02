# TermOS - Cross-Platform Terminal with Network Features

A powerful cross-platform terminal emulator with built-in network management capabilities, file sharing, and proxy functionality.

## Features

- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Network Management**: Connect to WiFi, create hotspots, scan networks
- **File Sharing**: Built-in HTTP server for local network file sharing
- **Proxy Server**: Create proxy connections for network traffic forwarding
- **System Integration**: Execute native OS commands seamlessly

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd termos
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run TermOS:
```bash
python -m termos.main
```

## Quick Start

```bash
# Start TermOS
python -m termos.main

# Basic commands
help                    # Show all available commands
info                    # Display system information
cd /path/to/directory   # Change directory
clear                   # Clear screen
exit                    # Exit TermOS
```

## Network Commands

### WiFi Management
```bash
net-scan                        # Scan available networks
net-connect MyWiFi password123  # Connect to WiFi with password
net-connect OpenWiFi            # Connect to open network
net-status                      # Show network status
```

### Hotspot Creation (Windows)
```bash
net-hotspot MyHotspot password123  # Create WiFi hotspot
net-stop-hotspot                   # Stop hotspot
```

### File Sharing
```bash
http-server         # Start HTTP server on port 8000
http-server 8080    # Start HTTP server on custom port
http-stop           # Stop HTTP server
```

### Proxy Server
```bash
proxy 3128 google.com 80        # Create proxy on port 3128
proxy 8080 192.168.1.100 80     # Forward to local server
```

## Use Cases

### 1. Local File Sharing
Share files with devices on your network:
```bash
cd /path/to/shared/folder
http-server 8000
# Access files at http://your-ip:8000
```

### 2. Network Proxy
Create a proxy for web traffic:
```bash
proxy 8080 target-server.com 80
# Configure browsers to use localhost:8080 as proxy
```

### 3. WiFi Management
Quickly connect to networks:
```bash
net-scan                    # Find available networks
net-connect "Office WiFi" password
```

## System Requirements

- Python 3.6+
- Windows 10+ (for hotspot features)
- Administrator privileges (for some network operations)

## Dependencies

- `colorama`: Terminal color support
- Built-in Python modules: `socket`, `http.server`, `subprocess`, `threading`

## Platform-Specific Features

### Windows
- Full WiFi management (connect, hotspot creation)
- Network interface configuration
- Command execution via cmd.exe

### Linux/macOS
- Basic network status
- File sharing and proxy functionality
- Command execution via shell

## Security Notes

- HTTP server serves files from current directory only
- Proxy server runs with user privileges
- Network operations may require administrator rights
- Always use strong passwords for hotspots

## Troubleshooting

### Common Issues

**"Access Denied" on Windows network commands:**
- Run terminal as Administrator
- Check Windows network adapter settings

**HTTP server port already in use:**
- Use different port: `http-server 8001`
- Stop conflicting services

**Proxy connection fails:**
- Verify target host is reachable
- Check firewall settings
- Ensure port is not blocked

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit pull request

## License

MIT License - see LICENSE file for details