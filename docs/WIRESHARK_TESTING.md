# Test Web Application với Wireshark

## Cài Đặt

1. **Download Wireshark**: https://www.wireshark.org/download.html
2. **Cài đặt WinPcap/Npcap** (đi kèm với Wireshark)

## Các Bước Test

### 1. Khởi động Wireshark

```bash
# Chạy với quyền Administrator
# Chọn network interface (WiFi hoặc Ethernet)
```

### 2. Bắt Đầu Capture

**Chọn interface:**
- WiFi: `Wi-Fi` hoặc `Wireless Network Connection`
- Ethernet: `Ethernet` hoặc `Local Area Connection`

**Nhấn nút xanh "Start capturing packets"**

### 3. Filter HTTP/HTTPS Traffic

**Display Filters:**

```wireshark
# Lọc theo domain
http.host contains "netlify.app"
http.host contains "onrender.com"

# Lọc HTTP requests
http.request

# Lọc HTTP responses
http.response

# Lọc theo method
http.request.method == "POST"
http.request.method == "GET"

# Lọc theo status code
http.response.code == 200
http.response.code == 500

# Lọc theo IP
ip.addr == 192.168.1.100

# Kết hợp filters
http.request.method == "POST" && http.host contains "onrender.com"
```

### 4. Test Các API Của Dự Án

#### A. Test Frontend (Netlify)

**Filter:**
```wireshark
http.host contains "majestic-babka-099eae.netlify.app"
```

**Kiểm tra:**
- ✅ GET requests cho HTML/CSS/JS
- ✅ Response code 200
- ✅ Content-Type: text/html, application/javascript

#### B. Test Backend API (Render)

**Filter:**
```wireshark
http.host contains "expense-tracker-backend-onvz.onrender.com"
```

**Test các endpoint:**

1. **Health Check**
```wireshark
http.request.uri == "/" && http.host contains "onrender.com"
```

2. **Login API**
```wireshark
http.request.uri == "/api/auth/login" && http.request.method == "POST"
```

3. **Register API**
```wireshark
http.request.uri == "/api/auth/register" && http.request.method == "POST"
```

4. **Transaction API**
```wireshark
http.request.uri contains "/api/giao-dich"
```

### 5. Phân Tích Request/Response

**Click vào packet → Follow → HTTP Stream**

**Xem thông tin:**
- Request Headers
- Request Body (JSON data)
- Response Headers
- Response Body
- Status Code

### 6. Kiểm Tra Bảo Mật

**Tìm thông tin nhạy cảm:**

```wireshark
# Tìm password trong plaintext
http contains "password"
http contains "mat_khau"

# Tìm token
http contains "Bearer"
http contains "access_token"

# Tìm API keys
http contains "apiKey"
http contains "AIzaSy"
```

⚠️ **Lưu ý:** Nếu thấy password/token trong plaintext → Cần dùng HTTPS!

### 7. Test Performance

**Statistics → HTTP → Requests**

Xem:
- Response time
- Packet count
- Data size

### 8. Export Kết Quả

**File → Export Packet Dissections**

Chọn format:
- Plain text
- CSV
- JSON

## Ví Dụ Test Dự Án

### Test Login Flow

1. **Start Wireshark capture**
2. **Apply filter:**
```wireshark
http.host contains "onrender.com" || http.host contains "netlify.app"
```

3. **Thực hiện login trên web**
4. **Dừng capture**
5. **Phân tích:**
   - POST /api/auth/login
   - Request body: `{"email":"...","mat_khau":"..."}`
   - Response: `{"access_token":"...","user_id":...}`
   - Status: 200 OK

### Test OCR Upload

1. **Filter:**
```wireshark
http.request.method == "POST" && (http.content_type contains "multipart" || http.content_type contains "json")
```

2. **Upload ảnh hóa đơn**
3. **Xem:**
   - File size
   - Upload time
   - Response data

## Capture Filters (Nâng Cao)

**Chỉ capture HTTP/HTTPS:**
```
tcp port 80 or tcp port 443
```

**Chỉ capture từ/đến domain cụ thể:**
```
host netlify.app or host onrender.com
```

**Chỉ capture POST requests:**
```
tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354
```

## Troubleshooting

### Không thấy HTTPS traffic?

**Giải pháp:**
1. Cài đặt SSL/TLS keys (nếu có)
2. Hoặc dùng Browser DevTools (F12) → Network tab
3. Wireshark chỉ thấy encrypted data với HTTPS

### Quá nhiều packets?

**Giải pháp:**
- Dùng display filters
- Stop capture khi không cần
- Clear display: `Ctrl+Shift+K`

### Không bắt được traffic?

**Nguyên nhân và giải pháp:**

1. **Ethernet không hoạt động:**
   - Kiểm tra: `ipconfig` trong CMD → xem interface nào có IP
   - Nếu dùng WiFi → Chọn **WiFi/WLAN** interface thay vì Ethernet
   - Nếu Ethernet không có IP → Không kết nối mạng

2. **Chạy Wireshark với quyền Admin:**
   - Chuột phải Wireshark → "Run as Administrator"

3. **Chọn đúng interface:**
   ```
   # Kiểm tra interface đang dùng:
   ipconfig
   
   # Tìm interface có IP address
   # Ví dụ: 192.168.1.100 (WiFi) hoặc 10.0.0.5 (Ethernet)
   ```

4. **Tắt VPN/Proxy:**
   - VPN có thể che traffic
   - Tắt VPN rồi thử lại

5. **Không thấy gì vì HTTPS:**
   - Web hiện đại dùng HTTPS (encrypted)
   - Wireshark chỉ thấy TLS handshake, không thấy nội dung
   - **Giải pháp:** Dùng **Browser DevTools (F12)** thay thế!

**Cách test nhanh:**
```bash
# 1. Mở CMD
ipconfig

# 2. Tìm interface có IP (ví dụ: Wi-Fi adapter)
# 3. Mở Wireshark → Chọn interface đó
# 4. Start capture
# 5. Mở browser → Vào http://example.com (HTTP, không HTTPS)
# 6. Nếu thấy packets → OK!
```

## Best Practices

1. ✅ **Chỉ capture khi cần** - tránh file quá lớn
2. ✅ **Dùng filters** - dễ phân tích
3. ✅ **Save captures** - để review sau
4. ✅ **Không capture password** - bảo mật
5. ✅ **Test trên localhost trước** - dễ debug

## Alternative Tools

- **Browser DevTools** (F12) - Dễ dùng hơn cho web
- **Postman** - Test API
- **Fiddler** - HTTP debugging proxy
- **Charles Proxy** - macOS/Windows

## Kết Luận

Wireshark tốt cho:
- ✅ Network-level debugging
- ✅ Performance analysis
- ✅ Security testing

Không tốt cho:
- ❌ HTTPS content (encrypted)
- ❌ Quick API testing (dùng Postman)
- ❌ Frontend debugging (dùng DevTools)

**Khuyến nghị:** Dùng Browser DevTools (F12) cho web testing thông thường!

---

## Quick Fix: Không Thấy Traffic

### Cách 1: Dùng Browser DevTools (Dễ nhất)

1. Mở Chrome/Edge
2. Nhấn **F12**
3. Chọn tab **Network**
4. Reload trang (Ctrl+R)
5. Xem tất cả requests/responses!

✅ **Ưu điểm:**
- Thấy được HTTPS content
- Xem headers, body, cookies
- Không cần Admin rights
- Dễ dùng hơn Wireshark

### Cách 2: Test với HTTP (không HTTPS)

```bash
# Test với site HTTP để kiểm tra Wireshark hoạt động:
http://example.com
http://neverssl.com
```

### Cách 3: Kiểm tra interface đang dùng

```cmd
# Mở CMD và chạy:
ipconfig /all

# Tìm interface có:
# - IPv4 Address: 192.168.x.x hoặc 10.x.x.x
# - Default Gateway: (có giá trị)

# Đó là interface đang dùng!
```

**Ví dụ output:**
```
Wireless LAN adapter Wi-Fi:
   IPv4 Address: 192.168.1.100  ← Dùng cái này!
   Default Gateway: 192.168.1.1

Ethernet adapter Ethernet:
   Media State: Media disconnected  ← Không dùng
```

➡️ **Chọn "Wi-Fi" trong Wireshark, không phải "Ethernet"!**
