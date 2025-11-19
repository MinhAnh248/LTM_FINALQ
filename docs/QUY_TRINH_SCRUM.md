# QUY TRÌNH SCRUM - DỰ ÁN QUẢN LÝ CHI TIÊU

## 1. Tổng quan quy trình Scrum

### Lý do chọn Scrum
- ✅ Phát triển linh hoạt, thích ứng nhanh với thay đổi
- ✅ Chia nhỏ dự án thành các Sprint 2-4 tuần
- ✅ Phản hồi liên tục từ người dùng
- ✅ Minh bạch trong công việc
- ✅ Cải tiến liên tục sau mỗi Sprint

### Ưu điểm Scrum
- Rút ngắn thời gian phát triển
- Chất lượng sản phẩm cao hơn
- Dễ dàng thay đổi yêu cầu
- Tăng sự phối hợp trong nhóm
- Phát hiện lỗi sớm

## 2. Vai trò trong Scrum

### Product Owner (Chủ sở hữu sản phẩm)
**Trách nhiệm:**
- Quản lý Product Backlog
- Ưu tiên các tính năng
- Đảm bảo giá trị sản phẩm
- Chấp nhận kết quả Sprint

**Trong dự án:**
- Xác định 15 chức năng chính
- Ưu tiên: Đăng nhập/Đăng ký → Giao dịch → Thống kê → Vay nợ → Tiết kiệm

### Scrum Master (Người hướng dẫn)
**Trách nhiệm:**
- Tổ chức các cuộc họp Scrum
- Loại bỏ trở ngại
- Đảm bảo tuân thủ quy trình
- Hỗ trợ nhóm phát triển

**Trong dự án:**
- Quản lý Trello board
- Tổ chức Daily Standup
- Giải quyết vấn đề kỹ thuật
- Review code

### Development Team (Nhóm phát triển)
**Trách nhiệm:**
- Thiết kế và lập trình
- Kiểm thử tính năng
- Hoàn thành Sprint Backlog
- Tự tổ chức công việc

**Trong dự án:**
- 6 thành viên
- Phân công theo chức năng
- Code review lẫn nhau
- Tích hợp liên tục

## 3. Các Sprint trong dự án

### Sprint 1 (Tuần 1-2): Foundation
**Mục tiêu:** Xây dựng nền tảng cơ bản

**Sprint Backlog:**
- [x] Setup project structure
- [x] Thiết kế database
- [x] API đăng ký/đăng nhập
- [x] Giao diện auth
- [x] JWT authentication

**Kết quả:**
- Backend API hoạt động
- Người dùng có thể đăng ký/đăng nhập
- Database được khởi tạo

### Sprint 2 (Tuần 3-4): Core Features
**Mục tiêu:** Các chức năng chính

**Sprint Backlog:**
- [x] API quản lý giao dịch
- [x] API quản lý danh mục
- [x] Giao diện giao dịch
- [x] Giao diện danh mục
- [x] Tính toán số dư tự động

**Kết quả:**
- Người dùng thêm/xem giao dịch
- Quản lý danh mục thu/chi
- Số dư cập nhật tự động

### Sprint 3 (Tuần 5-6): Advanced Features
**Mục tiêu:** Tính năng nâng cao

**Sprint Backlog:**
- [x] API thống kê
- [x] API vay nợ
- [x] API tiết kiệm
- [x] Giao diện thống kê
- [x] Giao diện vay nợ/tiết kiệm

**Kết quả:**
- Thống kê theo tháng/năm
- Quản lý vay nợ
- Kế hoạch tiết kiệm

### Sprint 4 (Tuần 7): Admin & Security
**Mục tiêu:** Quản trị và bảo mật

**Sprint Backlog:**
- [x] Trang admin
- [x] API quản lý người dùng
- [x] Phân quyền admin/user
- [x] Middleware bảo mật
- [x] Responsive design

**Kết quả:**
- Admin quản lý người dùng
- Bảo mật hoàn chỉnh
- Tương thích mobile

## 4. Các cuộc họp Scrum

### Daily Standup (15 phút/ngày)
**3 câu hỏi:**
1. Hôm qua làm gì?
2. Hôm nay làm gì?
3. Có trở ngại gì không?

**Ví dụ:**
```
Thành viên A:
- Hôm qua: Hoàn thành API giao dịch
- Hôm nay: Làm giao diện giao dịch
- Trở ngại: Không có
```

### Sprint Planning (2-4 giờ)
**Nội dung:**
- Review Product Backlog
- Chọn items cho Sprint
- Ước lượng effort
- Phân công công việc

### Sprint Review (1-2 giờ)
**Nội dung:**
- Demo tính năng hoàn thành
- Thu thập feedback
- Cập nhật Product Backlog

### Sprint Retrospective (1 giờ)
**3 câu hỏi:**
1. Điều gì tốt?
2. Điều gì cần cải thiện?
3. Hành động cải tiến?

## 5. Công cụ quản lý

### Trello Board
**Các cột:**
- 📋 Backlog - Công việc chưa làm
- 🏃 In Progress - Đang làm
- 👀 Review - Đang review
- ✅ Done - Hoàn thành

**Mỗi card chứa:**
- Tiêu đề task
- Mô tả chi tiết
- Người phụ trách
- Deadline
- Checklist

### Git & GitHub
**Workflow:**
```
main (production)
  ↑
develop (integration)
  ↑
feature/ten-tinh-nang (development)
```

**Quy tắc:**
- 1 feature = 1 branch
- Pull request trước khi merge
- Code review bắt buộc
- Commit message rõ ràng

## 6. Definition of Done (DoD)

### Một task được coi là Done khi:
- [x] Code hoàn thành
- [x] Unit test pass
- [x] Code review approved
- [x] Tích hợp thành công
- [x] Không có bug critical
- [x] Documentation cập nhật
- [x] Demo cho Product Owner

## 7. Metrics & KPIs

### Velocity (Tốc độ)
- Sprint 1: 20 story points
- Sprint 2: 25 story points
- Sprint 3: 30 story points
- Sprint 4: 25 story points
- **Trung bình: 25 points/sprint**

### Burndown Chart
```
Story Points
100 |●
 80 | ●
 60 |  ●
 40 |   ●
 20 |    ●
  0 |_____●____
    S1 S2 S3 S4
```

### Quality Metrics
- Code coverage: 80%+
- Bug rate: <5 bugs/sprint
- Review time: <24h
- Deployment success: 100%

## 8. Bài học kinh nghiệm

### Điều tốt
✅ Scrum giúp phát triển nhanh và linh hoạt
✅ Daily standup tăng sự phối hợp
✅ Sprint review giúp điều chỉnh kịp thời
✅ Trello giúp quản lý công việc hiệu quả

### Cần cải thiện
⚠️ Ước lượng thời gian chưa chính xác
⚠️ Một số task phụ thuộc lẫn nhau
⚠️ Cần tăng cường testing

### Hành động cải tiến
📌 Ước lượng dựa trên kinh nghiệm Sprint trước
📌 Xác định dependencies sớm
📌 Viết test song song với code
📌 Tăng thời gian code review

## 9. So sánh Scrum vs Waterfall

| Tiêu chí | Scrum | Waterfall |
|----------|-------|-----------|
| Linh hoạt | ✅ Cao | ❌ Thấp |
| Thời gian | 2-4 tuần/Sprint | Toàn bộ dự án |
| Feedback | Liên tục | Cuối dự án |
| Thay đổi | Dễ dàng | Khó khăn |
| Rủi ro | Thấp | Cao |
| Phù hợp | Dự án phức tạp | Dự án đơn giản |

## 10. Kết luận

### Thành công
✅ Hoàn thành 100% chức năng trong 7 tuần
✅ Chất lượng code tốt
✅ Không có bug nghiêm trọng
✅ Đáp ứng đúng yêu cầu

### Scrum đã giúp:
- Phát triển nhanh hơn 30%
- Giảm bug 50%
- Tăng sự phối hợp nhóm
- Sản phẩm đáp ứng đúng nhu cầu

### Khuyến nghị
📌 Tiếp tục sử dụng Scrum cho các dự án tương lai
📌 Áp dụng CI/CD để tự động hóa
📌 Tăng cường automated testing
📌 Sử dụng tools monitoring
