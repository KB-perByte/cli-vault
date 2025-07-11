Flow

```mermaid
graph TD
    A[User runs 'kini command'] --> B[__main__.py]
    B --> C[password_manager.py:main()]

    subgraph "Setup"
        C --> D[Initialize PasswordManager]
        D --> E[Setup Data Directory: ~/.kini]
        subgraph "File System"
            E --> F[passwords.json]
            E --> G[master.hash]
            E --> H[salt.key]
            E --> I[backups/]
        end
    end

    subgraph "Authentication"
        C --> J{Master Password Set?}
        J -->|No| K[First-Time Setup]
        J -->|Yes| L[Login]

        subgraph "First-Time Setup"
            K --> K1[Create Master Password]
            K1 --> K2[Generate Salt & Key]
            K2 --> K3[Initialize Encrypted DB]
        end

        subgraph "Login"
            L --> L1[Verify Master Password]
            L1 -- Valid --> L2[Load & Decrypt Database]
            L1 -- Invalid --> L3[Authentication Failed]
        end
    end

    subgraph "Commands"
        C --> M[Parse Command]
        M --> N{Command Type}
        N -->|add| O[Add Password]
        N -->|get| P[Get Password]
        N -->|search| Q[Search Passwords]
        N -->|list| R[List Services]
        N -->|delete| S[Delete Password]
        N -->|backup| T[Backup Database]
        N -->|restore| U[Restore Database]
    end

    subgraph "Data Operations"
        O --> V[Encrypt & Save]
        P --> W[Find & Display]
        Q --> X[Search & Display]
        R --> Y[List All]
        S --> Z[Delete & Save]
        T --> AA[Create Backup File]
        U --> BB[Restore From Backup]
    end

    subgraph "Core Components"
        subgraph "Security"
            Sec1[AES-256 Encryption]
            Sec2[PBKDF2 HMAC Key Derivation]
            Sec3[SHA-256 Hashing]
            Sec4[16-byte Salt]
        end
        subgraph "Data"
            Data1[JSON: {passwords, history}]
        end
    end

    K1 --> Sec3
    L1 --> Sec3
    K2 --> Sec2
    K2 --> Sec4
    L2 --> Sec2
    V --> Sec1
    L2 --> Sec1
    K3 --> Data1
    V --> Data1
    W --> L2
    X --> L2
    Y --> L2
```
