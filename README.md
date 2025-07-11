# Kini - Secure Password Manager

A secure command-line password manager with encryption, hashing, backup, and search capabilities.

## Features

- **Secure Encryption**: Uses AES-256 encryption (Fernet) for all stored data
- **Master Password**: Single password protects all your passwords
- **Password History**: Track password changes with timestamps
- **Search Functionality**: Find passwords quickly by service name
- **Backup & Restore**: Create and restore from encrypted backups
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### From PyPI (to be published)

```bash
pip install kini
```

### From Source

```bash
git clone https://github.com/yourusername/kini.git
cd kini
pip install -e .
```

## Usage

### First Time Setup

```bash
kini list
# This will prompt you to create a master password
```

### Adding Passwords

```bash
# Interactive mode
kini add

# Command line mode
kini add -s "gmail" -u "user@gmail.com" -p "mypassword"
```

### Retrieving Passwords

```bash
# Get specific password
kini get -s "gmail"

# Search for passwords
kini search -q "mail"

# List all passwords
kini list
```

### Password History

```bash
# View password history for a service
kini history -s "gmail"
```

### Backup & Restore

```bash
# Create backup
kini backup

# List backups
kini backup list

# Restore from backup
kini restore -b "passwords_backup_20240101_120000.json"
```

### Other Commands

```bash
# Delete a password
kini delete -s "gmail"

# Show version
kini --version
```

## Security

- All passwords are encrypted using AES-256 (Fernet)
- Master password is hashed using SHA-256
- Key derivation uses PBKDF2 with 100,000 iterations
- Unique salt for each installation
- Data stored locally in `~/.kini/`

## Data Location

- **Linux/macOS**: `~/.kini/`
- **Windows**: `%USERPROFILE%\.kini\`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Security Considerations

- Never share your master password
- Regularly create backups
- Store backups in a secure location
- Use strong, unique passwords for your services
