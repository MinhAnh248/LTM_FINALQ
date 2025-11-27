# BẢO MẬT HỆ THỐNG

## 1. Bảo mật dữ liệu người dùng

### Mã hóa mật khẩu
- ✅ Sử dụng **bcrypt** để hash mật khẩu
- ✅ Salt tự động cho mỗi mật khẩu
- ✅ Không lưu mật khẩu dạng plain text

### Xác thực JWT
- ✅ Token JWT với thời hạn 30 ngày
- ✅ Token được mã hóa với SECRET_KEY
- ✅ Kiểm tra token mỗi request

### Bảo vệ dữ liệu
- ✅ CORS được cấu hình chặt chẽ
- ✅ Dữ liệu tài chính được lưu trong database SQLite
- ✅ Không log thông tin nhạy cảm

## 2. Phân quyền truy cập

### Vai trò người dùng
- **Admin (vai_tro_id = 1)**
  - Xem tất cả người dùng
  - Khóa/Mở khóa tài khoản
  - Truy cập trang admin.html

- **User (vai_tro_id = 2)**
  - Chỉ xem dữ liệu của mình
  - Không thể truy cập dữ liệu người khác
  - Truy cập trang index.html

### Kiểm tra quyền
```python
# Middleware tự động kiểm tra:
- Tài khoản bị khóa → Từ chối truy cập
- Token hết hạn → Yêu cầu đăng nhập lại
- Không đủ quyền → Trả về lỗi 403
```

## 3. Bảo mật API

### Các endpoint được bảo vệ
- ✅ Tất cả API yêu cầu JWT token (trừ login/register)
- ✅ Kiểm tra user_id từ token
- ✅ Chỉ trả về dữ liệu của user đó

### Ví dụ bảo mật
```python
@jwt_required()  # Bắt buộc có token
def get_transactions():
    user_id = get_jwt_identity()  # Lấy ID từ token
    # Chỉ lấy giao dịch của user này
    transactions = GiaoDich.query.filter_by(user_id=user_id).all()
```

## 4. Tính dễ sử dụng

### Giao diện thân thiện
- ✅ Thiết kế đơn giản, trực quan
- ✅ Màu sắc dễ nhìn
- ✅ Form nhập liệu rõ ràng
- ✅ Thông báo lỗi dễ hiểu

### Responsive Design
- ✅ Tự động điều chỉnh trên mobile
- ✅ Tối ưu cho tablet
- ✅ Hoạt động tốt trên desktop

### Hỗ trợ người dùng
- ✅ Placeholder gợi ý trong form
- ✅ Validation dữ liệu đầu vào
- ✅ Alert thông báo thành công/lỗi

## 5. Tương thích đa nền tảng

### Trình duyệt
- ✅ Chrome
- ✅ Firefox
- ✅ Edge
- ✅ Safari

### Thiết bị
- ✅ Desktop (1920x1080+)
- ✅ Laptop (1366x768+)
- ✅ Tablet (768x1024)
- ✅ Mobile (375x667+)

## 6. Khuyến nghị bảo mật

### Cho người dùng
1. Sử dụng mật khẩu mạnh (8+ ký tự, chữ hoa, số, ký tự đặc biệt)
2. Không chia sẻ mật khẩu
3. Đăng xuất sau khi sử dụng
4. Không truy cập trên máy công cộng

### Cho admin
1. Thay đổi mật khẩu admin mặc định
2. Định kỳ kiểm tra tài khoản bất thường
3. Backup database thường xuyên
4. Cập nhật SECRET_KEY trong .env

### Triển khai production
1. Sử dụng HTTPS
2. Cấu hình firewall
3. Giới hạn rate limiting
4. Sử dụng database mạnh hơn (PostgreSQL/MySQL)
5. Thay đổi JWT_SECRET_KEY
6. Bật logging và monitoring

## 7. Checklist bảo mật

- [x] Mã hóa mật khẩu với bcrypt
- [x] JWT authentication
- [x] Phân quyền admin/user
- [x] Kiểm tra tài khoản bị khóa
- [x] CORS configuration
- [x] Input validation
- [x] Error handling
- [x] Responsive design
- [x] Cross-browser compatible
- [ ] HTTPS (cần khi deploy)
- [ ] Rate limiting (cần khi deploy)
- [ ] Database encryption (tùy chọn)
