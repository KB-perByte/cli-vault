Flow for v1.0.0
```mermaid
flowchart TD
    A[User runs 'kini command'] --> B[__main__.py Entry Point]
    B --> C[main() in password_manager.py]
    C --> D[ArgumentParser Setup]
    D --> E[PasswordManager Init]
    
    E --> F[Data Directory Setup]
    F --> G[~/.kini/ directory]
    G --> H[passwords.json - Encrypted DB]
    G --> I[master.hash - Master Password Hash]
    G --> J[salt.key - Encryption Salt]
    G --> K[backups/ - Backup Directory]
    
    C --> L[Authentication Check]
    L --> M{Master Password Exists?}
    M -->|No| N[First Time Setup]
    M -->|Yes| O[Authenticate User]
    
    N --> P[Welcome Message + Mascot]
    P --> Q[Create Master Password]
    Q --> R[Hash Master Password SHA-256]
    R --> S[Generate Salt os.urandom(16)]
    S --> T[Generate Key PBKDF2HMAC]
    T --> U[Create Fernet Cipher]
    U --> V[Initialize Empty Database]
    
    O --> W[Load Master Hash]
    W --> X[Verify Password Hash]
    X --> Y{Password Valid?}
    Y -->|No| Z[Authentication Failed]
    Y -->|Yes| AA[Load Salt]
    AA --> BB[Generate Key PBKDF2HMAC]
    BB --> CC[Create Fernet Cipher]
    CC --> DD[Load & Decrypt Database]
    
    C --> EE[Command Execution]
    EE --> FF{Command Type}
    
    FF -->|add| GG[Add Password]
    FF -->|get| HH[Get Password]
    FF -->|search| II[Search Passwords]
    FF -->|list| JJ[List Passwords]
    FF -->|history| KK[Show History]
    FF -->|delete| LL[Delete Password]
    FF -->|backup| MM[Create Backup]
    FF -->|restore| NN[Restore Backup]
    
    GG --> OO[Interactive/CLI Input]
    OO --> PP[Store in data.passwords]
    PP --> QQ[Move Old to History]
    QQ --> RR[Encrypt & Save Database]
    
    HH --> SS[Find Service in DB]
    SS --> TT[Display Password Info]
    
    II --> UU[Query Match Against Services]
    UU --> VV[Display Matches]
    VV --> WW[Interactive Selection]
    
    MM --> XX[Copy DB to Backup Dir]
    XX --> YY[Timestamp Filename]
    
    NN --> ZZ[Verify Backup Exists]
    ZZ --> AAA[Copy Backup to DB]
    AAA --> BBB[Reload Database]
    
    subgraph "Security Layer"
        CCC[AES-256 Encryption Fernet]
        DDD[PBKDF2HMAC Key Derivation]
        EEE[SHA-256 Password Hashing]
        FFF[100,000 Iterations]
        GGG[16-byte Random Salt]
    end
    
    subgraph "Data Structure"
        HHH[{"passwords": {<br/>&nbsp;&nbsp;"service": {<br/>&nbsp;&nbsp;&nbsp;&nbsp;"username": "user",<br/>&nbsp;&nbsp;&nbsp;&nbsp;"password": "pass",<br/>&nbsp;&nbsp;&nbsp;&nbsp;"created_at": "timestamp",<br/>&nbsp;&nbsp;&nbsp;&nbsp;"updated_at": "timestamp"<br/>&nbsp;&nbsp;}<br/>},<br/>"history": {<br/>&nbsp;&nbsp;"service": [old_entries]<br/>}}]
    end
    
    subgraph "File System"
        III[~/.kini/passwords.json]
        JJJ[~/.kini/master.hash]
        KKK[~/.kini/salt.key]
        LLL[~/.kini/backups/]
    end
    
    RR --> CCC
    DD --> CCC
    T --> DDD
    BB --> DDD
    R --> EEE
    X --> EEE
    
    style A fill:#e1f5fe
    style CCC fill:#ffebee
    style DDD fill:#ffebee
    style EEE fill:#ffebee
    style HHH fill:#f3e5f5
    style III fill:#e8f5e8
    style JJJ fill:#e8f5e8
    style KKK fill:#e8f5e8
```
