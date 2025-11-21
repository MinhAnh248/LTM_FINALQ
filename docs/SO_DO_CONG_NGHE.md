# Sơ Đồ Công Nghệ Hoạt Động Trong Dự Án

## 📊 Kiến Trúc Tổng Quan

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  index.html  │  │  admin.html  │  │ocr_hoadon.html│         │
│  │  (Đăng nhập) │  │   (Admin)    │  │  (OCR Scan)   │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬────────┘         │
│         │                  │                  │                   │
│         └──────────────────┴──────────────────┘                  │
│                            │                                      │
└────────────────────────────┼──────────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │   INTERNET      │
                    │   (HTTPS/TLS)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌────────────────┐   ┌──────────────┐
│   NETLIFY     │   │     RENDER     │   │   FIREBASE   │
│   (Frontend)  │   │   (Backend)    │   │  (Database)  │
│               │   │                │   │              │
│ HTML/CSS/JS   │   │  Python/Flask  │   │  Firestore   │
│ Tesseract.js  │   │  SQLAlchemy    │   │  Auth        │
│ Tailwind CSS  │   │  JWT/Bcrypt    │   │  Storage     │
└───────────────┘   └────────────────┘   └──────────────┘
```

## 🔄 Luồng Hoạt Động Chi Tiết

### 1. Đăng Nhập (Login Flow)

```
Browser (index.html)
    │
    │ 1. User nhập email + password
    │
    ▼
JavaScript (Fetch API)
    │
    │ 2. POST /api/auth/login
    │    Body: {"email": "...", "mat_khau": "..."}
    │
    ▼
INTERNET (HTTPS)
    │
    │ 3. TLS Encryption
    │
    ▼
Render Backend (app.py)
    │
    ├─► 4. Flask Router → @app.route('/api/auth/login')
    │
    ├─► 5. SQLAlchemy ORM
    │       NguoiDung.query.filter_by(email=email).first()
    │       ├─► SQLite Database (instance/expense.db)
    │       └─► B-tree Index Lookup: O(log n)
    │
    ├─► 6. Bcrypt Password Verification
    │       bcrypt.checkpw(password, hashed_password)
    │       └─► Độ phức tạp: O(2^12) ~ 100-300ms
    │
    ├─► 7. JWT Token Generation
    │       create_access_token(identity=user_id)
    │       └─► HMAC-SHA256 signing
    │
    └─► 8. Response: {"access_token": "...", "user_id": 123}
    │
    ▼
Browser
    │
    └─► 9. localStorage.setItem('token', token)
```

**Công nghệ hoạt động:**
- ✅ **JavaScript Fetch API** - HTTP request
- ✅ **TLS 1.3** - Mã hóa truyền tải
- ✅ **Flask** - Web framework
- ✅ **SQLAlchemy** - ORM query
- ✅ **B-tree Index** - Database lookup
- ✅ **Bcrypt** - Password hashing
- ✅ **JWT/HMAC-SHA256** - Token generation

---

### 2. OCR Hóa Đơn (Invoice Scanning)

```
Browser (ocr_hoadon.html)
    │
    │ 1. User upload ảnh hóa đơn
    │
    ▼
Tesseract.js (Client-side)
    │
    ├─► 2. Image Preprocessing
    │       ├─► Grayscale Conversion
    │       ├─► Noise Reduction (Gaussian Blur)
    │       └─► Binarization (Otsu's Method)
    │
    ├─► 3. LSTM Neural Network
    │       ├─► Character Detection
    │       ├─► Feature Extraction
    │       └─► Pattern Recognition
    │       └─► Độ phức tạp: O(width × height)
    │
    └─► 4. Output: Raw OCR Text
    │
    ▼
Custom Algorithm (parseWithGemini)
    │
    ├─► 5. Unicode Normalization (NFD)
    │       text.normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    │       └─► Xử lý dấu tiếng Việt
    │
    ├─► 6. Regex Pattern Matching
    │       /(thanh tien|tong)[:\s]*([\d,\.]+)/i
    │       └─► Tìm từ khóa + số tiền
    │
    ├─► 7. Number Filtering
    │       ├─► Loại bỏ số điện thoại (10 chữ số, bắt đầu 0)
    │       ├─► Loại bỏ số nhỏ (< 1000)
    │       └─► Ưu tiên số lớn (>= 1M)
    │
    └─► 8. Output: {storeName, date, total, items}
    │
    ▼
Display Results
```

**Công nghệ hoạt động:**
- ✅ **FileReader API** - Đọc file ảnh
- ✅ **Tesseract.js** - OCR engine
- ✅ **LSTM Neural Network** - Text recognition
- ✅ **Unicode NFD** - Normalization
- ✅ **Regex** - Pattern matching
- ✅ **Heuristic Algorithm** - Number filtering

---

### 3. Lưu Giao Dịch (Save Transaction)

```
Browser (index.html)
    │
    │ 1. User nhập: loại, số tiền, mô tả, ngày
    │
    ▼
JavaScript
    │
    │ 2. POST /api/giao-dich
    │    Headers: {"Authorization": "Bearer <token>"}
    │    Body: {"loai": "chi", "so_tien": 50000, ...}
    │
    ▼
Render Backend
    │
    ├─► 3. JWT Middleware (@jwt_required)
    │       ├─► Verify token signature (HMAC-SHA256)
    │       ├─► Check expiration (30 days)
    │       └─► Extract user_id from payload
    │
    ├─► 4. Validate Category
    │       DanhMuc.query.filter_by(id=..., nguoi_dung_id=user_id)
    │       └─► Authorization check
    │
    ├─► 5. Create Transaction
    │       giao_dich = GiaoDich(...)
    │       db.session.add(giao_dich)
    │
    ├─► 6. Update Balance (O(1))
    │       if loai == 'Chi tiêu':
    │           user.so_du -= so_tien
    │       else:
    │           user.so_du += so_tien
    │
    └─► 7. Commit to Database
            db.session.commit()
            └─► ACID Transaction
    │
    ▼
Response: {"message": "...", "so_du_moi": 950000}
```

**Công nghệ hoạt động:**
- ✅ **JWT Middleware** - Authentication
- ✅ **HMAC-SHA256** - Token verification
- ✅ **SQLAlchemy ORM** - Database operations
- ✅ **ACID Transaction** - Data consistency
- ✅ **Arithmetic** - Balance calculation

---

### 4. Lưu Hóa Đơn Firebase (Save Invoice)

```
Browser (ocr_hoadon.html)
    │
    │ 1. User click "Lưu Hóa Đơn"
    │
    ▼
Firebase SDK (Client-side)
    │
    ├─► 2. Anonymous Authentication
    │       signInAnonymously(auth)
    │       └─► Get userId
    │
    ├─► 3. Prepare Document
    │       docData = {
    │           storeName, date, total, items,
    │           timestamp: serverTimestamp(),
    │           userId: userId
    │       }
    │
    ├─► 4. WebSocket Connection
    │       └─► Persistent connection to Firebase
    │
    └─► 5. Add Document
            addDoc(collection(db, "users", userId, "invoices"), docData)
    │
    ▼
Firebase Firestore (Cloud)
    │
    ├─► 6. NoSQL Document Store
    │       users/{userId}/invoices/{invoiceId}
    │       └─► Hierarchical structure
    │
    ├─► 7. Real-time Sync
    │       └─► WebSocket push to all clients
    │
    └─► 8. Indexing & Replication
            └─► Multi-region backup
    │
    ▼
Response: Success
```

**Công nghệ hoạt động:**
- ✅ **Firebase Auth** - Anonymous authentication
- ✅ **WebSocket** - Real-time connection
- ✅ **Firestore** - NoSQL database
- ✅ **Real-time Sync** - Live updates
- ✅ **Cloud Storage** - Distributed storage

---

## 🗺️ Sơ Đồ Công Nghệ Theo Layer

### Layer 1: Presentation (Frontend)

```
┌─────────────────────────────────────────────┐
│           BROWSER (Client)                  │
├─────────────────────────────────────────────┤
│ HTML5        → Structure                    │
│ CSS3         → Styling                      │
│ Tailwind CSS → Utility-first CSS            │
│ JavaScript   → Logic & Interaction          │
│   ├─ Fetch API      → HTTP requests         │
│   ├─ Async/Await    → Asynchronous ops     │
│   ├─ DOM API        → UI manipulation       │
│   ├─ localStorage   → Client storage        │
│   └─ FileReader     → File handling         │
│                                             │
│ Libraries:                                  │
│   ├─ Tesseract.js   → OCR processing       │
│   ├─ XLSX.js        → Excel export          │
│   └─ Firebase SDK   → Database & Auth      │
└─────────────────────────────────────────────┘
```

### Layer 2: Network (Transport)

```
┌─────────────────────────────────────────────┐
│           INTERNET                          │
├─────────────────────────────────────────────┤
│ HTTP/1.1     → Request/Response protocol    │
│ HTTPS        → HTTP + TLS encryption        │
│ TLS 1.3      → Transport Layer Security     │
│ WebSocket    → Bidirectional communication  │
│ TCP/IP       → Network protocol             │
│ DNS          → Domain resolution            │
│ CDN          → Content delivery             │
└─────────────────────────────────────────────┘
```

### Layer 3: Application (Backend)

```
┌─────────────────────────────────────────────┐
│        RENDER (Python Server)               │
├─────────────────────────────────────────────┤
│ Gunicorn     → WSGI HTTP Server             │
│ Flask        → Web framework                │
│   ├─ Routing        → URL mapping           │
│   ├─ Request/Response → HTTP handling       │
│   └─ Middleware     → JWT auth              │
│                                             │
│ Flask Extensions:                           │
│   ├─ Flask-SQLAlchemy  → ORM                │
│   ├─ Flask-JWT-Extended → JWT auth          │
│   ├─ Flask-CORS        → CORS handling      │
│   └─ python-dotenv     → Env variables      │
│                                             │
│ Security:                                   │
│   ├─ Bcrypt         → Password hashing      │
│   ├─ JWT            → Token-based auth      │
│   └─ HMAC-SHA256    → Token signing         │
└─────────────────────────────────────────────┘
```

### Layer 4: Data (Database)

```
┌─────────────────────────────────────────────┐
│         DATABASES                           │
├─────────────────────────────────────────────┤
│ SQLite (Local Dev)                          │
│   ├─ File-based DB                          │
│   ├─ ACID compliance                        │
│   ├─ B-tree indexing                        │
│   └─ SQL queries                            │
│                                             │
│ Firebase Firestore (Production)             │
│   ├─ NoSQL document store                   │
│   ├─ Real-time sync                         │
│   ├─ Offline support                        │
│   └─ Cloud-based                            │
│                                             │
│ SQLAlchemy ORM                              │
│   ├─ Object-Relational Mapping              │
│   ├─ Query builder                          │
│   ├─ Connection pooling                     │
│   └─ Lazy loading                           │
└─────────────────────────────────────────────┘
```

---

## 📍 Vị Trí Hoạt Động Của Từng Công Nghệ

| Công Nghệ | Vị Trí | Chức Năng | Khi Nào Hoạt Động |
|-----------|--------|-----------|-------------------|
| **HTML/CSS/JS** | Browser | UI & Logic | Mọi lúc user mở web |
| **Tailwind CSS** | Browser | Styling | Render UI |
| **Fetch API** | Browser | HTTP Request | Khi call API |
| **localStorage** | Browser | Lưu token | Sau login |
| **Tesseract.js** | Browser | OCR | Khi upload ảnh hóa đơn |
| **XLSX.js** | Browser | Export Excel | Khi click "Xuất Excel" |
| **Firebase SDK** | Browser | Database | Khi lưu/load hóa đơn |
| **TLS 1.3** | Network | Mã hóa | Mọi HTTPS request |
| **HTTP/1.1** | Network | Protocol | Mọi request/response |
| **WebSocket** | Network | Real-time | Firebase sync |
| **Gunicorn** | Render Server | WSGI Server | Nhận HTTP requests |
| **Flask** | Render Server | Web Framework | Xử lý requests |
| **JWT Middleware** | Render Server | Auth | Mọi protected route |
| **Bcrypt** | Render Server | Hash Password | Register/Login |
| **HMAC-SHA256** | Render Server | Sign JWT | Tạo/verify token |
| **SQLAlchemy** | Render Server | ORM | Mọi DB operation |
| **B-tree Index** | SQLite | Fast Lookup | Query database |
| **ACID Transaction** | SQLite | Data Consistency | Commit changes |
| **Firestore** | Firebase Cloud | NoSQL DB | Lưu hóa đơn OCR |

---

## 🔐 Luồng Bảo Mật

```
User Input (Password: "123456")
    │
    ▼
Browser (HTTPS)
    │ TLS 1.3 Encryption
    ▼
Render Server
    │
    ├─► Bcrypt Hashing
    │   Input: "123456"
    │   Salt: random (16 bytes)
    │   Cost: 12 (2^12 iterations)
    │   Output: "$2b$12$..."
    │   Time: ~200ms
    │
    ├─► Store in Database
    │   SQLite: hashed_password column
    │
    └─► JWT Token Generation
        Header: {"alg": "HS256", "typ": "JWT"}
        Payload: {"sub": "123", "exp": 1234567890}
        Signature: HMAC-SHA256(header + payload, secret)
        Output: "eyJhbGc..."
    │
    ▼
Browser
    │
    └─► localStorage.setItem('token', token)
```

---

## 📊 Tổng Kết Công Nghệ Theo Vị Trí

### 🖥️ CLIENT-SIDE (Browser)
1. HTML5, CSS3, JavaScript
2. Tailwind CSS
3. Tesseract.js (LSTM OCR)
4. XLSX.js
5. Firebase SDK
6. Fetch API, localStorage

### 🌐 NETWORK
1. HTTPS/TLS 1.3
2. HTTP/1.1
3. WebSocket
4. TCP/IP, DNS

### ⚙️ SERVER-SIDE (Render)
1. Python 3.11
2. Flask Framework
3. Gunicorn WSGI
4. SQLAlchemy ORM
5. Bcrypt (Password)
6. JWT/HMAC-SHA256 (Auth)
7. Flask-CORS

### 💾 DATABASE
1. SQLite (Local)
2. Firebase Firestore (Cloud)
3. B-tree Indexing
4. ACID Transactions

### 🚀 DEPLOYMENT
1. Netlify (Frontend CDN)
2. Render (Backend PaaS)
3. GitHub (Version Control)
4. Git (CI/CD)

**Tổng cộng: 30+ công nghệ hoạt động đồng thời!**
