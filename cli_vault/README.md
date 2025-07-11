# CLI Vault - Secure Password Manager

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
pip install cli-vault
```

### From Source

```bash
git clone https://github.com/yourusername/cli-vault.git
cd cli-vault
pip install -e .
```

## Usage

### First Time Setup

```bash
cli-vault list
# This will prompt you to create a master password
```

### Adding Passwords

```bash
# Interactive mode
cli-vault add

# Command line mode
cli-vault add -s "gmail" -u "user@gmail.com" -p "mypassword"
```

### Retrieving Passwords

```bash
# Get specific password
cli-vault get -s "gmail"

# Search for passwords
cli-vault search -q "mail"

# List all passwords
cli-vault list
```

### Password History

```bash
# View password history for a service
cli-vault history -s "gmail"
```

### Backup & Restore

```bash
# Create backup
cli-vault backup

# List backups
cli-vault backup list

# Restore from backup
cli-vault restore -b "passwords_backup_20240101_120000.json"
```

### Other Commands

```bash
# Delete a password
cli-vault delete -s "gmail"

# Show version
cli-vault --version
```

## Security

- All passwords are encrypted using AES-256 (Fernet)
- Master password is hashed using SHA-256
- Key derivation uses PBKDF2 with 100,000 iterations
- Unique salt for each installation
- Data stored locally in `~/.cli_vault/`

## Data Location

- **Linux/macOS**: `~/.cli_vault/`
- **Windows**: `%USERPROFILE%\.cli_vault\`

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
