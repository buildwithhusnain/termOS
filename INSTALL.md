# Installation Guide

## System Requirements

### Minimum Requirements
- **Python**: 3.6 or higher
- **Operating System**: Windows 10+, Linux (Ubuntu 18.04+), macOS 10.14+
- **Memory**: 50MB RAM
- **Storage**: 10MB disk space

### Administrator Privileges
Some network features require elevated privileges:
- **Windows**: Run as Administrator for hotspot creation
- **Linux**: sudo access for network configuration
- **macOS**: sudo access for network operations

## Installation Methods

### Method 1: pip install (Recommended)
```bash
pip install termos
```

### Method 2: From Source
```bash
# Clone repository
git clone https://github.com/username/termos.git
cd termos

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Method 3: Direct Download
```bash
# Download and extract
wget https://github.com/username/termos/archive/main.zip
unzip main.zip
cd termos-main

# Install
pip install -r requirements.txt
python -m termos.main
```

## Platform-Specific Installation

### Windows Installation
```cmd
# Using pip
pip install termos

# Or using conda
conda install -c conda-forge termos

# Run TermOS
termos
```

**Windows-specific notes:**
- Install from elevated Command Prompt for full features
- Windows Defender may require approval for network operations
- Hotspot features require Windows 10 version 1607 or later

### Linux Installation
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip
pip3 install termos

# CentOS/RHEL/Fedora
sudo yum install python3 python3-pip
# or: sudo dnf install python3 python3-pip
pip3 install termos

# Arch Linux
sudo pacman -S python python-pip
pip install termos
```

**Linux-specific notes:**
- Some distributions may require `python3-dev` package
- Network scanning may require `wireless-tools` package
- Use `sudo termos` for network configuration features

### macOS Installation
```bash
# Using Homebrew
brew install python3
pip3 install termos

# Using MacPorts
sudo port install python39 py39-pip
pip3 install termos

# Direct installation
pip3 install termos
```

**macOS-specific notes:**
- Xcode Command Line Tools may be required
- Network features may require Security & Privacy permissions
- Use `sudo termos` for network operations

## Verification

### Test Installation
```bash
# Check if TermOS is installed
termos --version

# Or run directly
python -m termos.main

# Test basic functionality
termos
> help
> info
> exit
```

### Test Network Features
```bash
termos
> net-status        # Should show network information
> http-server 8080   # Should start HTTP server
> http-stop          # Should stop server
> exit
```

## Dependencies

### Required Dependencies
- `colorama>=0.4.0` - Terminal color support

### Optional Dependencies
- `pytest>=6.0.0` - For running tests
- `setuptools>=40.0.0` - For development

### System Dependencies

**Windows:**
- Windows 10 SDK (for advanced network features)
- Visual C++ Redistributable (usually pre-installed)

**Linux:**
- `wireless-tools` - For WiFi scanning
- `net-tools` - For network configuration
- `iproute2` - Modern network utilities

**macOS:**
- Xcode Command Line Tools
- Network framework (built-in)

## Troubleshooting Installation

### Common Issues

**"Command not found: termos"**
```bash
# Check if pip bin directory is in PATH
python -m pip show termos
# Add pip bin directory to PATH or use:
python -m termos.main
```

**"Permission denied" errors**
```bash
# Install for current user only
pip install --user termos

# Or use virtual environment
python -m venv termos-env
source termos-env/bin/activate  # Linux/macOS
# termos-env\Scripts\activate   # Windows
pip install termos
```

**"Module not found" errors**
```bash
# Ensure dependencies are installed
pip install -r requirements.txt

# Or reinstall with dependencies
pip install --force-reinstall termos
```

**Network features not working**
```bash
# Windows: Run as Administrator
# Linux/macOS: Use sudo
sudo termos

# Check network adapter status
# Windows: Device Manager > Network Adapters
# Linux: ip link show
# macOS: System Preferences > Network
```

### Platform-Specific Issues

**Windows:**
- **Error**: "netsh command not found"
  - **Solution**: Ensure Windows is up to date
- **Error**: "Access denied" for hotspot
  - **Solution**: Run Command Prompt as Administrator

**Linux:**
- **Error**: "iwlist command not found"
  - **Solution**: `sudo apt install wireless-tools`
- **Error**: "Permission denied" for network
  - **Solution**: Add user to netdev group or use sudo

**macOS:**
- **Error**: "Operation not permitted"
  - **Solution**: Grant Terminal network permissions in Security & Privacy
- **Error**: "Command not found: iwconfig"
  - **Solution**: Use built-in network utilities or install wireless-tools

## Development Installation

### For Contributors
```bash
# Clone repository
git clone https://github.com/username/termos.git
cd termos

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest black flake8

# Run tests
python -m pytest
```

### Building from Source
```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Install built package
pip install dist/termos-*.whl
```

## Uninstallation

### Remove TermOS
```bash
# Using pip
pip uninstall termos

# Remove configuration (optional)
rm -rf ~/.termos  # Linux/macOS
# rmdir /s %USERPROFILE%\.termos  # Windows
```

### Clean Installation
```bash
# Remove all traces
pip uninstall termos
pip cache purge
# Remove any virtual environments created for TermOS
```

## Next Steps

After successful installation:
1. Read the [README.md](README.md) for basic usage
2. Check [EXAMPLES.md](EXAMPLES.md) for practical examples
3. Review [API.md](API.md) for advanced usage
4. Join the community for support and updates