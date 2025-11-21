# Vị Trí Công Nghệ Trong Code Dự Án

## 📁 File: `app.py` (Backend - Render)

### Dòng 1-8: Import Libraries
```python
from flask import Flask, jsonify, request              # ← Flask Framework
from flask_sqlalchemy import SQLAlchemy                # ← SQLAlchemy ORM
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity  # ← JWT Auth
from flask_cors import CORS                            # ← CORS
from datetime import datetime, timedelta               # ← Python datetime
import bcrypt                                          # ← Bcrypt hashing
import os                                              # ← OS operations
from dotenv import load_dotenv                         # ← Environment variables
```

### Dòng 11-13: Flask App Initialization
```python
app = Flask(__name__)                                  # ← Flask app instance
CORS(app, resources={r"/api/*": {"origins": "*"}})    # ← CORS middleware
```

### Dòng 15-23: Database Configuration
```python
db_path = os.getenv('DATABASE_URL', 'sqlite:////tmp/expense.db')  # ← SQLite path
app.config['SQLALCHEMY_DATABASE_URI'] = db_path       # ← Database URI
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # ← JWT secret
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)  # ← Token expiry

db = SQLAlchemy(app)                                   # ← SQLAlchemy instance
jwt = JWTManager(app)                                  # ← JWT manager
```

### Dòng 30-56: Database Models (ORM)
```python
class NguoiDung(db.Model):                             # ← SQLAlchemy Model
    __tablename__ = 'nguoi_dung'                       # ← Table name
    id = db.Column(db.Integer, primary_key=True)       # ← Primary key (B-tree index)
    email = db.Column(db.String(100), unique=True)     # ← Unique index
    mat_khau = db.Column(db.String(255))               # ← Bcrypt hashed password
```

### Dòng 103-125: Register API - Bcrypt
```python
@app.route('/api/auth/register', methods=['POST'])     # ← Flask route
def register():
    data = request.get_json()                          # ← Parse JSON
    
    hashed_password = bcrypt.hashpw(                   # ← Bcrypt hashing
        data['mat_khau'].encode('utf-8'),              # ← Encode to bytes
        bcrypt.gensalt()                               # ← Generate salt
    )
    
    user = NguoiDung(                                  # ← ORM object
        ho_ten=data['ho_ten'],
        email=data['email'],
        mat_khau=hashed_password.decode('utf-8')       # ← Store hash
    )
    
    db.session.add(user)                               # ← Add to session
    db.session.commit()                                # ← ACID commit
```

### Dòng 127-145: Login API - JWT
```python
@app.route('/api/auth/login', methods=['POST'])        # ← Flask route
def login():
    user = NguoiDung.query.filter_by(email=email).first()  # ← SQLAlchemy query (B-tree)
    
    if not bcrypt.checkpw(                             # ← Bcrypt verify
        data['mat_khau'].encode('utf-8'),
        user.mat_khau.encode('utf-8')
    ):
        return jsonify({'message': 'Sai mật khẩu'}), 401
    
    access_token = create_access_token(identity=str(user.id))  # ← JWT token (HMAC-SHA256)
    return jsonify({'access_token': access_token}), 200
```

### Dòng 148-175: Transaction API - JWT Middleware
```python
@app.route('/api/giao-dich', methods=['POST'])
@jwt_required()                                        # ← JWT middleware
def create_transaction():
    user_id = int(get_jwt_identity())                  # ← Extract user from JWT
    
    danh_muc = DanhMuc.query.filter_by(               # ← SQLAlchemy query
        id=danh_muc_id, 
        nguoi_dung_id=user_id
    ).first()
    
    if danh_muc.loai_danh_muc == 'Chi tiêu':          # ← Arithmetic calculation
        user.so_du -= data['so_tien']                 # ← O(1) operation
    
    db.session.commit()                                # ← ACID transaction
```

### Dòng 230-245: Statistics API - SQL Aggregation
```python
@app.route('/api/thong-ke', methods=['GET'])
@jwt_required()
def get_statistics():
    chi_tieu = db.session.query(db.func.sum(GiaoDich.so_tien))  # ← SQL SUM aggregation
        .filter(GiaoDich.ngay >= month_start)          # ← SQL WHERE
        .join(DanhMuc)                                 # ← SQL JOIN
        .scalar()                                      # ← Execute query
```

---

## 📁 File: `index.html` (Frontend - Netlify)

### Dòng 1-10: HTML5 Structure
```html
<!DOCTYPE html>                                        <!-- ← HTML5 -->
<html lang="vi">
<head>
    <meta charset="UTF-8">                             <!-- ← UTF-8 encoding -->
    <meta name="viewport" content="width=device-width"> <!-- ← Responsive -->
    <script src="https://cdn.tailwindcss.com"></script> <!-- ← Tailwind CSS -->
```

### Dòng 150-165: JavaScript - Fetch API
```javascript
async function login() {                               // ← Async/Await
    const response = await fetch(                      // ← Fetch API
        'https://expense-tracker-backend-onvz.onrender.com/api/auth/login',
        {
            method: 'POST',                            // ← HTTP POST
            headers: {
                'Content-Type': 'application/json'     // ← JSON header
            },
            body: JSON.stringify(data)                 // ← JSON stringify
        }
    );
    
    const result = await response.json();              // ← Parse JSON
    localStorage.setItem('token', result.access_token); // ← localStorage API
}
```

### Dòng 200-215: JavaScript - JWT Authorization
```javascript
async function createTransaction() {
    const token = localStorage.getItem('token');       // ← Get JWT token
    
    const response = await fetch(url, {
        headers: {
            'Authorization': `Bearer ${token}`         // ← JWT Bearer token
        }
    });
}
```

### Dòng 300-320: JavaScript - DOM Manipulation
```javascript
function displayTransactions(transactions) {
    const container = document.getElementById('list'); // ← DOM API
    container.innerHTML = transactions.map(t => `      // ← Template literals
        <div class="transaction">
            ${t.mo_ta} - ${t.so_tien} VNĐ              // ← String interpolation
        </div>
    `).join('');                                       // ← Array methods
}
```

---

## 📁 File: `ocr_hoadon.html` (OCR - Netlify)

### Dòng 7-9: External Libraries
```html
<script src="https://cdn.jsdelivr.net/npm/tesseract.js@4/dist/tesseract.min.js"></script>  <!-- ← Tesseract.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script> <!-- ← XLSX.js -->
<script src="https://cdn.tailwindcss.com"></script>   <!-- ← Tailwind CSS -->
```

### Dòng 12-18: Firebase SDK
```javascript
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";  // ← Firebase
import { getAuth, signInAnonymously } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";  // ← Firebase Auth
import { getFirestore, addDoc, collection } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js";  // ← Firestore
```

### Dòng 130-145: Firebase Initialization
```javascript
const firebaseConfig = {                               // ← Firebase config
    apiKey: "AIzaSy...",
    projectId: "hoadonocr-696fb"
};
const app = initializeApp(firebaseConfig);             // ← Initialize Firebase
auth = getAuth(app);                                   // ← Get Auth instance
db = getFirestore(app);                                // ← Get Firestore instance
```

### Dòng 200-210: FileReader API
```javascript
function handleFileUpload(event) {
    const file = event.target.files[0];                // ← File API
    const reader = new FileReader();                   // ← FileReader API
    reader.onload = function(e) {
        document.getElementById('previewImage').src = e.target.result;  // ← Base64 data URL
    };
    reader.readAsDataURL(file);                        // ← Read as Data URL
}
```

### Dòng 220-240: Tesseract.js OCR
```javascript
async function processImage() {
    const { data: { text } } = await Tesseract.recognize(  // ← Tesseract.js
        uploadedFile,                                  // ← Image file
        'eng+vie',                                     // ← Language: English + Vietnamese
        {
            logger: m => {                             // ← Progress callback
                if (m.status === 'recognizing text') {
                    const progress = Math.round(m.progress * 100);  // ← LSTM progress
                }
            }
        }
    );
    // text = OCR result (LSTM Neural Network output)
}
```

### Dòng 250-285: Custom Algorithm - Number Detection
```javascript
async function parseWithGemini(ocrText) {
    // 1. Unicode Normalization (NFD)
    const numbers = ocrText.match(/\d+[,\.]?\d*/g) || [];  // ← Regex pattern matching
    const normalizedText = ocrText.normalize('NFD')    // ← Unicode NFD normalization
        .replace(/[\u0300-\u036f]/g, '');              // ← Remove diacritics
    
    // 2. Keyword matching
    const totalMatch = normalizedText.match(           // ← Regex matching
        /(thanh tien|tong)[:\s]*([\d,\.]+)/i
    );
    
    // 3. Number filtering (Heuristic algorithm)
    const numValues = numbers
        .map(n => parseFloat(n.replace(/,/g, '')))     // ← Parse numbers
        .filter(n => {
            const str = n.toString();
            if (str.length === 10 && str[0] === '0') return false;  // ← Filter phone numbers
            if (n < 1000) return false;                // ← Filter small numbers
            return n > 0;
        });
    
    // 4. Priority selection
    const bigNumbers = numValues.filter(n => n >= 1000000);  // ← Filter >= 1M
    total = bigNumbers.length > 0 ? Math.max(...bigNumbers) : Math.max(...numValues);  // ← Max selection
}
```

### Dòng 400-420: Firebase Firestore Operations
```javascript
async function saveReceipt() {
    const docData = {                                  // ← Document data
        storeName: currentReceiptInfo.storeName,
        total: currentReceiptInfo.total,
        timestamp: window.firebase.serverTimestamp()   // ← Server timestamp
    };
    
    const { collection, addDoc } = window.firebase;
    await addDoc(                                      // ← Firestore addDoc
        collection(db, "users", userId, "invoices"),   // ← Hierarchical path
        docData
    );
    // → WebSocket real-time sync to Firebase Cloud
}
```

### Dòng 500-520: XLSX Export
```javascript
function exportToExcel() {
    const ws_data = [                                  // ← Worksheet data
        ["Tên Cửa Hàng", info.storeName],
        ["Tổng Cộng", "", info.total]
    ];
    const wb = XLSX.utils.book_new();                  // ← Create workbook
    const ws = XLSX.utils.aoa_to_sheet(ws_data);       // ← Array to sheet
    XLSX.utils.book_append_sheet(wb, ws, "HoaDon");    // ← Append sheet
    XLSX.writeFile(wb, `HoaDon_${info.date}.xlsx`);    // ← Download file
}
```

---

## 📁 File: `requirements.txt` (Dependencies)

```txt
Flask==3.0.0                 # ← Line 1: Flask framework
Flask-SQLAlchemy==3.1.1      # ← Line 2: SQLAlchemy ORM
Flask-JWT-Extended==4.6.0    # ← Line 3: JWT authentication
Flask-CORS==4.0.0            # ← Line 4: CORS middleware
bcrypt==4.1.2                # ← Line 5: Bcrypt hashing
python-dotenv==1.0.0         # ← Line 6: Environment variables
gunicorn==21.2.0             # ← Line 7: WSGI HTTP server
```

---

## 📁 File: `render.yaml` (Deployment Config)

```yaml
services:
  - type: web                # ← Line 2: Web service type
    env: python              # ← Line 4: Python environment
    buildCommand: pip install -r requirements.txt  # ← Line 5: Build command
    startCommand: gunicorn app:app  # ← Line 6: Gunicorn WSGI server
    envVars:
      - key: JWT_SECRET_KEY  # ← Line 8: Environment variable
        generateValue: true  # ← Line 9: Auto-generate secret
```

---

## 📁 File: `.env` (Environment Variables)

```env
DATABASE_URL=sqlite:///expense.db     # ← Line 1: SQLite database path
JWT_SECRET_KEY=your-secret-key        # ← Line 2: JWT secret for HMAC-SHA256
FLASK_ENV=development                 # ← Line 3: Flask environment
```

---

## 📁 File: `instance/expense.db` (SQLite Database)

```
Binary file - SQLite 3 database
├─ Table: nguoi_dung          # ← Users table
│  ├─ Index: PRIMARY KEY (id) # ← B-tree index
│  └─ Index: UNIQUE (email)   # ← B-tree index
├─ Table: danh_muc            # ← Categories table
├─ Table: giao_dich           # ← Transactions table
└─ ACID transactions          # ← ACID compliance
```

---

## 🌐 Network Layer (Runtime)

### HTTPS Request Flow
```
Browser → TLS 1.3 Handshake → Encrypted Connection
    ↓
Fetch API → HTTP/1.1 POST → JSON payload
    ↓
Netlify CDN → Edge Network → Gzip compression
    ↓
Render Server → Gunicorn → Flask app
    ↓
SQLAlchemy → SQLite → B-tree lookup
    ↓
Response → JSON → TLS encryption → Browser
```

---

## 📊 Tổng Kết Vị Trí Trong Code

| Công Nghệ | File | Dòng Code | Chức Năng |
|-----------|------|-----------|-----------|
| **Flask** | app.py | 1, 11 | Web framework |
| **SQLAlchemy** | app.py | 2, 25 | ORM |
| **JWT** | app.py | 3, 26, 141 | Authentication |
| **Bcrypt** | app.py | 6, 109, 135 | Password hashing |
| **CORS** | app.py | 4, 12 | Cross-origin |
| **Gunicorn** | render.yaml | 6 | WSGI server |
| **Tesseract.js** | ocr_hoadon.html | 7, 225 | OCR engine |
| **Firebase** | ocr_hoadon.html | 12-18, 130, 410 | Database & Auth |
| **XLSX.js** | ocr_hoadon.html | 8, 510 | Excel export |
| **Tailwind CSS** | *.html | 9 | UI styling |
| **Fetch API** | index.html | 155 | HTTP requests |
| **localStorage** | index.html | 165 | Client storage |
| **FileReader** | ocr_hoadon.html | 205 | File reading |
| **Regex** | ocr_hoadon.html | 255, 265 | Pattern matching |
| **Unicode NFD** | ocr_hoadon.html | 258 | Normalization |
| **B-tree Index** | expense.db | (binary) | Fast lookup |
| **TLS 1.3** | (runtime) | Network layer | Encryption |

**Tổng cộng: 30+ công nghệ được sử dụng trực tiếp trong code!**
