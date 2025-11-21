# Công Nghệ & Thuật Toán Sử Dụng Trong Dự Án

## 1. Ngôn Ngữ Lập Trình

### Backend
- **Python 3.11+**
  - Flask framework
  - SQLAlchemy ORM
  - JWT authentication
  - Bcrypt hashing

### Frontend
- **HTML5**
- **CSS3** (Tailwind CSS)
- **JavaScript ES6+**
  - Async/Await
  - Fetch API
  - DOM manipulation

## 2. Framework & Thư Viện

### Backend (Python)
```python
Flask==3.0.0                 # Web framework
Flask-SQLAlchemy==3.1.1      # ORM
Flask-JWT-Extended==4.6.0    # JWT authentication
Flask-CORS==4.0.0            # Cross-Origin Resource Sharing
bcrypt==4.1.2                # Password hashing
python-dotenv==1.0.0         # Environment variables
gunicorn==21.2.0             # WSGI server
```

### Frontend (JavaScript)
```javascript
Tesseract.js v4              // OCR engine
XLSX.js v0.18.5              // Excel export
Firebase v11.6.1             // Database & Auth
Tailwind CSS                 // UI framework
```

## 3. Thuật Toán & Kỹ Thuật

### A. Bảo Mật

#### 1. Password Hashing (Bcrypt)
```python
# Thuật toán: Bcrypt với salt
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Độ phức tạp: O(2^cost) - cost = 12 (mặc định)
# Thời gian: ~100-300ms per hash
```

**Đặc điểm:**
- Salt ngẫu nhiên cho mỗi password
- Chống rainbow table attacks
- Chống brute force (slow by design)

#### 2. JWT (JSON Web Token)
```python
# Thuật toán: HS256 (HMAC-SHA256)
token = create_access_token(identity=user_id)

# Cấu trúc: header.payload.signature
# Thời gian sống: 30 ngày
```

**Đặc điểm:**
- Stateless authentication
- Không cần lưu session trên server
- Chống CSRF attacks

### B. OCR (Optical Character Recognition)

#### Tesseract.js
```javascript
// Thuật toán: LSTM Neural Network
const { data: { text } } = await Tesseract.recognize(image, 'eng+vie');
```

**Quy trình:**
1. **Image Preprocessing**
   - Grayscale conversion
   - Noise reduction
   - Binarization (Otsu's method)

2. **Text Detection**
   - Connected Component Analysis
   - LSTM (Long Short-Term Memory) network
   - Character segmentation

3. **Text Recognition**
   - Feature extraction
   - Pattern matching
   - Language model correction

**Độ phức tạp:** O(n×m) với n×m là kích thước ảnh

### C. Nhận Diện Số Tiền (Custom Algorithm)

```javascript
// Thuật toán tự phát triển
function detectTotal(ocrText) {
    // 1. Normalize Unicode (NFD)
    const normalized = text.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    
    // 2. Keyword matching với regex
    const match = normalized.match(/(thanh tien|tong)[:\s]*([\d,\.]+)/i);
    
    // 3. Number filtering
    const numbers = text.match(/\d+[,\.]?\d*/g)
        .filter(n => {
            // Loại bỏ số điện thoại (10 chữ số bắt đầu 0)
            if (n.length === 10 && n[0] === '0') return false;
            // Loại bỏ số nhỏ
            if (n < 1000) return false;
            return true;
        });
    
    // 4. Prioritize large numbers (>= 1M)
    return Math.max(...numbers.filter(n => n >= 1000000));
}
```

**Độ phức tạp:** O(n) với n là độ dài text

**Kỹ thuật:**
- Unicode normalization (NFD)
- Regex pattern matching
- Heuristic filtering
- Priority-based selection

### D. Database Queries

#### SQLAlchemy ORM
```python
# Thuật toán: Query optimization với indexing
user = NguoiDung.query.filter_by(email=email).first()

# Index trên: email (UNIQUE), id (PRIMARY KEY)
# Độ phức tạp: O(log n) với B-tree index
```

**Tối ưu hóa:**
- Lazy loading relationships
- Query caching
- Connection pooling

### E. Data Processing

#### 1. Transaction Calculation
```python
# Thuật toán: Running balance
if loai == 'Chi tiêu':
    user.so_du -= so_tien
else:
    user.so_du += so_tien

# Độ phức tạp: O(1)
```

#### 2. Statistics Aggregation
```python
# Thuật toán: SQL Aggregation
chi_tieu = db.session.query(func.sum(GiaoDich.so_tien))\
    .filter(GiaoDich.ngay >= month_start)\
    .scalar()

# Độ phức tạp: O(n) với n là số giao dịch trong tháng
```

## 4. Kiến Trúc & Design Patterns

### A. Architecture Pattern
- **Client-Server Architecture**
- **RESTful API**
- **MVC Pattern** (Model-View-Controller)

### B. Design Patterns

#### 1. Repository Pattern
```python
# Abstraction layer cho database
class NguoiDung(db.Model):
    # Model definition
    
# Usage
user = NguoiDung.query.filter_by(email=email).first()
```

#### 2. Middleware Pattern
```python
# JWT authentication middleware
@jwt_required()
def protected_route():
    user_id = get_jwt_identity()
```

#### 3. Factory Pattern
```python
# Database initialization
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
```

## 5. Giao Thức Mạng

### HTTP/HTTPS
- **Protocol:** HTTP/1.1, HTTPS (TLS 1.3)
- **Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200, 201, 400, 401, 403, 404, 500

### WebSocket (Firebase Realtime)
- **Protocol:** WebSocket over TLS
- **Use case:** Real-time database sync

## 6. Cơ Sở Dữ Liệu

### SQLite (Local Development)
- **Engine:** SQLite 3
- **ACID compliance**
- **File-based database**

### Firebase Firestore (Production)
- **NoSQL document database**
- **Real-time synchronization**
- **Offline support**

**Schema Design:**
```
users/{userId}/invoices/{invoiceId}
  - storeName: string
  - date: string
  - total: number
  - items: array
  - timestamp: timestamp
```

## 7. Deployment & DevOps

### CI/CD
- **Git** - Version control
- **GitHub** - Repository hosting
- **Netlify** - Frontend auto-deploy
- **Render** - Backend auto-deploy

### Containerization
```yaml
# render.yaml
services:
  - type: web
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

## 8. Performance Optimization

### Frontend
- **Lazy Loading** - Load images on demand
- **Code Splitting** - Separate vendor bundles
- **Caching** - Browser cache, CDN

### Backend
- **Database Indexing** - B-tree indexes
- **Connection Pooling** - Reuse DB connections
- **Query Optimization** - Minimize N+1 queries

### Network
- **CDN** - Netlify Edge Network
- **Compression** - Gzip/Brotli
- **HTTP/2** - Multiplexing

## 9. Testing & Quality Assurance

### Testing Tools
- **Manual Testing** - Browser DevTools
- **API Testing** - Postman, curl
- **Network Analysis** - Wireshark

### Code Quality
- **Linting** - PEP 8 (Python)
- **Error Handling** - Try-catch blocks
- **Logging** - Console.log, print statements

## 10. Tóm Tắt Độ Phức Tạp

| Chức năng | Thuật toán | Độ phức tạp |
|-----------|-----------|-------------|
| Password hashing | Bcrypt | O(2^12) |
| JWT verification | HMAC-SHA256 | O(n) |
| Database query | B-tree index | O(log n) |
| OCR processing | LSTM | O(n×m) |
| Number detection | Regex + Filter | O(n) |
| Transaction calc | Arithmetic | O(1) |
| Statistics | SQL Aggregation | O(n) |

## 11. Security Measures

1. **Authentication:** JWT tokens
2. **Authorization:** Role-based access control
3. **Encryption:** HTTPS/TLS
4. **Password:** Bcrypt hashing
5. **CORS:** Restricted origins
6. **Input Validation:** Server-side validation
7. **SQL Injection:** ORM parameterized queries
8. **XSS:** HTML escaping

## Kết Luận

Dự án sử dụng:
- ✅ **3 ngôn ngữ:** Python, JavaScript, HTML/CSS
- ✅ **5+ thuật toán:** Bcrypt, JWT, LSTM OCR, Regex, B-tree
- ✅ **10+ công nghệ:** Flask, Firebase, Tesseract, SQLite, etc.
- ✅ **RESTful API** architecture
- ✅ **Modern web stack** với cloud deployment
