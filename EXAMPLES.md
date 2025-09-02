# TermOS Usage Examples

## Basic Terminal Operations

### Navigation and File Management
```bash
# Start TermOS
python -m termos.main

# Check current system info
info

# Navigate directories
cd C:\Users\Username\Documents
cd /home/username/projects
cd ../parent-directory

# List files (OS-specific commands work)
dir          # Windows
ls -la       # Linux/macOS

# Clear screen
clear
```

## Network Management Examples

### WiFi Connection Management
```bash
# Scan for available networks
net-scan

# Connect to open network
net-connect "Public-WiFi"

# Connect to secured network
net-connect "Home-WiFi" "mypassword123"

# Check connection status
net-status
```

### Creating WiFi Hotspot (Windows)
```bash
# Create hotspot
net-hotspot "MyHotspot" "securepassword"

# Check if hotspot is running
net-status

# Stop hotspot when done
net-stop-hotspot
```

## File Sharing Server

### Basic File Sharing
```bash
# Navigate to folder you want to share
cd C:\Users\Username\Documents\SharedFiles

# Start HTTP server on default port (8000)
http-server

# Server is now accessible at:
# http://192.168.1.100:8000 (replace with your IP)
```

### Custom Port File Sharing
```bash
# Start server on custom port
http-server 8080

# Access via: http://your-ip:8080
# Stop server when done
http-stop
```

### Sharing Different Directories
```bash
# Share Downloads folder
cd C:\Users\Username\Downloads
http-server 9000

# Share project files
cd /home/user/projects
http-server 8001
```

## Proxy Server Examples

### Web Traffic Proxy
```bash
# Create proxy for web browsing
proxy 8080 google.com 80

# Configure browser to use:
# HTTP Proxy: localhost:8080
```

### Local Network Forwarding
```bash
# Forward to local web server
proxy 3000 192.168.1.50 80

# Forward to database server
proxy 5432 db-server.local 5432
```

### Multiple Service Proxies
```bash
# Terminal 1: Web proxy
proxy 8080 web-server.com 80

# Terminal 2: API proxy  
proxy 3000 api-server.com 443

# Terminal 3: Database proxy
proxy 5432 db-server.com 5432
```

## Real-World Scenarios

### Scenario 1: Mobile Development Testing
```bash
# Share web app for mobile testing
cd C:\Projects\MyWebApp\dist
http-server 8000

# Mobile devices can access:
# http://192.168.1.100:8000
```

### Scenario 2: File Transfer Between Devices
```bash
# On sender machine
cd C:\Users\Username\FilesToShare
http-server 8080

# Recipients visit: http://sender-ip:8080
# Download files directly through browser
```

### Scenario 3: Development Proxy Setup
```bash
# Proxy local development to production API
proxy 3001 api.production.com 443

# Update app config to use: localhost:3001
# Test with production data locally
```

### Scenario 4: Network Troubleshooting
```bash
# Check network connectivity
net-status

# Test proxy connectivity
proxy 8080 google.com 80
# Try accessing: http://localhost:8080

# Scan available networks
net-scan
```

### Scenario 5: Temporary Hotspot for Devices
```bash
# Create hotspot for IoT devices
net-hotspot "IoT-Setup" "temppassword"

# Configure devices to connect
# Stop when configuration complete
net-stop-hotspot
```

## Advanced Usage Patterns

### Chaining Commands with System Commands
```bash
# Create directory and start server
mkdir shared-files && cd shared-files
http-server 8000

# Download file and serve it
curl -O https://example.com/file.zip
http-server 9000
```

### Multiple Terminal Workflow
```bash
# Terminal 1: File server
cd /project/build
http-server 8000

# Terminal 2: API proxy
proxy 3000 api.server.com 80

# Terminal 3: Development work
cd /project/src
# Continue coding while services run
```

### Network Configuration Workflow
```bash
# Step 1: Check current status
net-status

# Step 2: Connect to network
net-connect "Office-WiFi" "password"

# Step 3: Verify connection
net-status

# Step 4: Start services
http-server 8000
```

## Error Handling Examples

### Common Error Scenarios
```bash
# Port already in use
http-server 8000
# Error: Port 8000 already in use
http-server 8001  # Try different port

# Network connection failed
net-connect "WrongNetwork" "wrongpass"
# Error: Connection failed

# Invalid proxy target
proxy 8080 nonexistent.server.com 80
# Error: Cannot resolve hostname
```

### Recovery Strategies
```bash
# If server won't start
http-stop          # Stop any existing server
http-server 8001   # Try different port

# If network won't connect
net-scan           # Check available networks
net-status         # Check current connection
# Try connecting to different network
```

## Performance Tips

### Optimal Server Configuration
```bash
# Use higher ports to avoid conflicts
http-server 8080   # Better than 80, 443, 8000

# Serve from SSD for better performance
cd /fast-drive/files
http-server 9000
```

### Network Optimization
```bash
# Check network status before operations
net-status

# Use local IP for better performance
# Access via 192.168.x.x instead of localhost
```