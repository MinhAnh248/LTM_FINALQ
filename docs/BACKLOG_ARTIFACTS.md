# SCRUM ARTIFACTS - CÁC TÀI LIỆU SCRUM

## 1. Product Backlog (Danh sách yêu cầu sản phẩm)

### Định nghĩa
Product Backlog là danh sách đầy đủ và có thứ tự ưu tiên của tất cả các tính năng, yêu cầu, cải tiến và sửa lỗi cần thiết cho sản phẩm. Product Owner chịu trách nhiệm quản lý và ưu tiên danh sách này.

### Product Backlog - Hệ thống Quản Lý Chi Tiêu

| ID | Tính năng | Mô tả | Ưu tiên | Story Points | Trạng thái |
|----|-----------|-------|---------|--------------|------------|
| PB-01 | Đăng ký tài khoản | Người dùng có thể tạo tài khoản mới | Cao | 5 | ✅ Done |
| PB-02 | Đăng nhập | Xác thực người dùng với email/password | Cao | 5 | ✅ Done |
| PB-03 | Quản lý hồ sơ | Cập nhật thông tin cá nhân, đổi mật khẩu | Cao | 3 | ✅ Done |
| PB-04 | Thêm giao dịch | Ghi chép thu nhập và chi tiêu | Cao | 8 | ✅ Done |
| PB-05 | Xem lịch sử giao dịch | Hiển thị danh sách giao dịch | Cao | 5 | ✅ Done |
| PB-06 | Tạo danh mục | Tạo danh mục thu/chi tùy chỉnh | Cao | 5 | ✅ Done |
| PB-07 | Đặt giới hạn chi tiêu | Thiết lập ngân sách cho từng danh mục | Trung bình | 5 | ✅ Done |
| PB-08 | Cảnh báo vượt mức | Thông báo khi chi tiêu vượt giới hạn | Trung bình | 3 | ✅ Done |
| PB-09 | Thống kê theo tháng | Báo cáo chi tiêu/thu nhập theo tháng | Cao | 8 | ✅ Done |
| PB-10 | Thống kê chi tiết | Phân tích theo danh mục | Trung bình | 5 | ✅ Done |
| PB-11 | Quản lý vay nợ | Theo dõi khoản cho vay/mượn nợ | Trung bình | 8 | ✅ Done |
| PB-12 | Thanh toán nợ | Ghi nhận các khoản thanh toán | Trung bình | 5 | ✅ Done |
| PB-13 | Kế hoạch tiết kiệm | Tạo mục tiêu tiết kiệm | Trung bình | 8 | ✅ Done |
| PB-14 | Lịch sử tiết kiệm | Theo dõi tiến độ tiết kiệm | Thấp | 5 | ✅ Done |
| PB-15 | Nhắc nhở thanh toán | Thông báo đến hạn thanh toán | Thấp | 3 | ✅ Done |
| PB-16 | Quản lý admin | Admin quản lý người dùng | Cao | 8 | ✅ Done |
| PB-17 | Phân quyền | Phân quyền admin/user | Cao | 5 | ✅ Done |
| PB-18 | Bảo mật JWT | Xác thực token | Cao | 5 | ✅ Done |
| PB-19 | Responsive design | Tối ưu cho mobile/tablet | Trung bình | 5 | ✅ Done |
| PB-20 | Quản lý nhóm | Chi tiêu theo nhóm người dùng | Thấp | 13 | 🔄 Future |

**Tổng Story Points:** 115 points
**Hoàn thành:** 102 points (89%)
**Còn lại:** 13 points (11%)

### Tiêu chí ưu tiên
1. **Cao:** Tính năng cốt lõi, không thể thiếu
2. **Trung bình:** Tính năng quan trọng, tăng giá trị
3. **Thấp:** Tính năng bổ sung, có thể làm sau

## 2. Sprint Backlog (Danh sách công việc Sprint)

### Sprint 1 Backlog (Tuần 1-2): Foundation

**Mục tiêu Sprint:** Xây dựng nền tảng cơ bản cho hệ thống

| Task ID | Tên Task | Người phụ trách | Effort (h) | Trạng thái |
|---------|----------|-----------------|------------|------------|
| S1-T1 | Setup Flask project | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S1-T2 | Thiết kế database schema | Nguyễn Quốc Vũ | 6 | ✅ Done |
| S1-T3 | Implement models | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S1-T4 | API đăng ký | Phan Công Sỹ | 6 | ✅ Done |
| S1-T5 | API đăng nhập | Phan Công Sỹ | 6 | ✅ Done |
| S1-T6 | JWT authentication | Nguyễn Quốc Vũ | 8 | ✅ Done |
| S1-T7 | Giao diện đăng ký | Trần Văn Thành | 6 | ✅ Done |
| S1-T8 | Giao diện đăng nhập | Trần Văn Thành | 6 | ✅ Done |
| S1-T9 | Tích hợp auth frontend-backend | Trần Văn Thành | 4 | ✅ Done |
| S1-T10 | Testing auth flow | Vũ Đức Nguyên | 4 | ✅ Done |

**Total Effort:** 54 giờ
**Story Points:** 18 points

### Sprint 2 Backlog (Tuần 3-4): Core Features

**Mục tiêu Sprint:** Phát triển các chức năng chính

| Task ID | Tên Task | Người phụ trách | Effort (h) | Trạng thái |
|---------|----------|-----------------|------------|------------|
| S2-T1 | API tạo danh mục | Phan Công Sỹ | 4 | ✅ Done |
| S2-T2 | API lấy danh mục | Phan Công Sỹ | 3 | ✅ Done |
| S2-T3 | API thêm giao dịch | Nguyễn Quốc Vũ | 6 | ✅ Done |
| S2-T4 | API lấy giao dịch | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S2-T5 | Tính số dư tự động | Nguyễn Quốc Vũ | 6 | ✅ Done |
| S2-T6 | Giao diện danh mục | Trần Văn Thành | 8 | ✅ Done |
| S2-T7 | Giao diện giao dịch | Trần Văn Thành | 8 | ✅ Done |
| S2-T8 | Đặt giới hạn chi tiêu | Phan Công Sỹ | 5 | ✅ Done |
| S2-T9 | Cảnh báo vượt mức | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S2-T10 | Testing core features | Vũ Đức Nguyên | 6 | ✅ Done |

**Total Effort:** 54 giờ
**Story Points:** 26 points

### Sprint 3 Backlog (Tuần 5-6): Advanced Features

**Mục tiêu Sprint:** Tính năng nâng cao

| Task ID | Tên Task | Người phụ trách | Effort (h) | Trạng thái |
|---------|----------|-----------------|------------|------------|
| S3-T1 | API thống kê tổng quan | Vũ Đức Nguyên | 6 | ✅ Done |
| S3-T2 | API thống kê chi tiết | Vũ Đức Nguyên | 8 | ✅ Done |
| S3-T3 | API vay nợ | Trần Văn Thành | 6 | ✅ Done |
| S3-T4 | API thanh toán | Trần Văn Thành | 4 | ✅ Done |
| S3-T5 | API tiết kiệm | Phạm Văn Nguyên Ngọc | 6 | ✅ Done |
| S3-T6 | API lịch sử tiết kiệm | Phạm Văn Nguyên Ngọc | 4 | ✅ Done |
| S3-T7 | Giao diện thống kê | Vũ Đức Nguyên | 8 | ✅ Done |
| S3-T8 | Giao diện vay nợ | Trần Văn Thành | 6 | ✅ Done |
| S3-T9 | Giao diện tiết kiệm | Phạm Văn Nguyên Ngọc | 6 | ✅ Done |
| S3-T10 | Nhắc nhở thanh toán | Phạm Văn Nguyên Ngọc | 4 | ✅ Done |

**Total Effort:** 58 giờ
**Story Points:** 30 points

### Sprint 4 Backlog (Tuần 7): Admin & Security

**Mục tiêu Sprint:** Quản trị và bảo mật

| Task ID | Tên Task | Người phụ trách | Effort (h) | Trạng thái |
|---------|----------|-----------------|------------|------------|
| S4-T1 | API admin users | Ngô Thành Lâm | 6 | ✅ Done |
| S4-T2 | API khóa/mở khóa | Ngô Thành Lâm | 4 | ✅ Done |
| S4-T3 | Trang admin | Trần Văn Thành | 8 | ✅ Done |
| S4-T4 | Middleware phân quyền | Nguyễn Quốc Vũ | 6 | ✅ Done |
| S4-T5 | Kiểm tra tài khoản khóa | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S4-T6 | Responsive design | Trần Văn Thành | 8 | ✅ Done |
| S4-T7 | Cross-browser testing | Vũ Đức Nguyên | 4 | ✅ Done |
| S4-T8 | Security audit | Nguyễn Quốc Vũ | 4 | ✅ Done |
| S4-T9 | Documentation | Tất cả | 6 | ✅ Done |
| S4-T10 | Final testing | Vũ Đức Nguyên | 4 | ✅ Done |

**Total Effort:** 54 giờ
**Story Points:** 28 points

## 3. Increment (Kết quả Sprint)

### Sprint 1 Increment
**Ngày hoàn thành:** 15/11/2024

**Tính năng hoàn thành:**
- ✅ Hệ thống đăng ký/đăng nhập
- ✅ JWT authentication
- ✅ Database schema
- ✅ Giao diện auth

**Deliverables:**
- Backend API: `/api/auth/register`, `/api/auth/login`
- Frontend: `index.html` (auth forms)
- Database: `expense.db` với các bảng cơ bản
- Documentation: API docs

**Demo:** Người dùng có thể đăng ký và đăng nhập thành công

### Sprint 2 Increment
**Ngày hoàn thành:** 29/11/2024

**Tính năng hoàn thành:**
- ✅ Quản lý danh mục thu/chi
- ✅ Thêm/xem giao dịch
- ✅ Tính số dư tự động
- ✅ Đặt giới hạn chi tiêu
- ✅ Cảnh báo vượt mức

**Deliverables:**
- Backend API: `/api/danh-muc`, `/api/giao-dich`, `/api/gioi-han-chi-tieu`
- Frontend: Tabs Giao dịch, Danh mục
- Business logic: Tính toán số dư, kiểm tra giới hạn

**Demo:** Người dùng quản lý thu chi hoàn chỉnh

### Sprint 3 Increment
**Ngày hoàn thành:** 06/12/2024

**Tính năng hoàn thành:**
- ✅ Thống kê theo tháng/năm
- ✅ Báo cáo chi tiết
- ✅ Quản lý vay nợ
- ✅ Kế hoạch tiết kiệm
- ✅ Nhắc nhở thanh toán

**Deliverables:**
- Backend API: `/api/thong-ke`, `/api/vay-no`, `/api/tich-luy`, `/api/nhac-nho`
- Frontend: Tabs Thống kê, Vay nợ, Tiết kiệm
- Charts: Biểu đồ thống kê

**Demo:** Hệ thống phân tích tài chính đầy đủ

### Sprint 4 Increment
**Ngày hoàn thành:** 13/12/2024

**Tính năng hoàn thành:**
- ✅ Trang quản trị admin
- ✅ Phân quyền admin/user
- ✅ Bảo mật nâng cao
- ✅ Responsive design
- ✅ Documentation hoàn chỉnh

**Deliverables:**
- Backend API: `/api/admin/*`
- Frontend: `admin.html`
- Security: Middleware, CORS, JWT
- Docs: `HUONG_DAN.md`, `BAO_MAT.md`, `QUY_TRINH_SCRUM.md`

**Demo:** Hệ thống hoàn chỉnh, sẵn sàng production

## 4. Definition of Done (Tiêu chí hoàn thành)

### Tiêu chí cho mỗi Task

#### Code Quality
- [ ] Code tuân thủ coding standards
- [ ] Không có code smell
- [ ] Không có hardcoded values
- [ ] Comments đầy đủ cho logic phức tạp
- [ ] Naming conventions rõ ràng

#### Testing
- [ ] Unit tests được viết và pass
- [ ] Integration tests pass
- [ ] Manual testing hoàn thành
- [ ] Không có bug critical
- [ ] Edge cases được xử lý

#### Code Review
- [ ] Pull Request được tạo
- [ ] Ít nhất 1 người review
- [ ] Comments được giải quyết
- [ ] Approved bởi reviewer
- [ ] Conflicts được resolve

#### Integration
- [ ] Code được merge vào develop
- [ ] Build thành công
- [ ] Không break existing features
- [ ] Database migration (nếu có)
- [ ] Environment variables cập nhật

#### Documentation
- [ ] API documentation cập nhật
- [ ] README cập nhật (nếu cần)
- [ ] Code comments đầy đủ
- [ ] User guide cập nhật (nếu cần)

#### Demo
- [ ] Feature demo cho Product Owner
- [ ] Product Owner chấp nhận
- [ ] Feedback được ghi nhận
- [ ] Screenshots/video (nếu cần)

### Tiêu chí cho Sprint Increment

#### Functionality
- [ ] Tất cả Sprint Backlog items hoàn thành
- [ ] Tất cả acceptance criteria đạt
- [ ] Không có bug blocking
- [ ] Performance acceptable

#### Quality
- [ ] Code coverage >= 80%
- [ ] No critical security issues
- [ ] Accessibility standards met
- [ ] Cross-browser compatible

#### Documentation
- [ ] Sprint Report hoàn thành
- [ ] Release notes cập nhật
- [ ] Known issues documented
- [ ] User documentation updated

#### Deployment
- [ ] Code deployed to staging
- [ ] Smoke tests pass
- [ ] Rollback plan ready
- [ ] Monitoring setup

### Checklist cho Release

#### Pre-Release
- [ ] All Sprint Increments integrated
- [ ] Full regression testing
- [ ] Performance testing
- [ ] Security audit
- [ ] User acceptance testing

#### Release
- [ ] Production deployment
- [ ] Database backup
- [ ] Monitoring active
- [ ] Support team notified
- [ ] Release announcement

#### Post-Release
- [ ] Monitor for issues
- [ ] Gather user feedback
- [ ] Update Product Backlog
- [ ] Retrospective meeting

## 5. Burndown Chart

### Sprint 1 Burndown
```
Story Points
18 |●
15 | ●
12 |  ●
 9 |   ●
 6 |    ●
 3 |     ●
 0 |______●
   D1 D2 D3 D4 D5 D6 D7
```

### Sprint 2 Burndown
```
Story Points
26 |●
22 | ●
18 |  ●
14 |   ●
10 |    ●
 6 |     ●
 2 |      ●
 0 |_______●
   D1 D2 D3 D4 D5 D6 D7 D8
```

### Velocity Chart
```
Story Points
30 |      ●
25 |  ●   |
20 | ●    |
15 |      |
10 |      |
 5 |      |
 0 |______|_____
   S1  S2  S3  S4
```

**Average Velocity:** 25.5 points/sprint

## 6. Kết luận

### Thành công
✅ **Product Backlog:** 20 items, 102/115 points hoàn thành (89%)
✅ **Sprint Backlog:** 4 sprints, 40 tasks, 100% hoàn thành
✅ **Increment:** 4 increments, tất cả đạt DoD
✅ **Velocity:** Ổn định 25-30 points/sprint

### Bài học
📌 Product Backlog cần được review và cập nhật liên tục
📌 Sprint Backlog phải realistic và achievable
📌 Definition of Done giúp đảm bảo chất lượng
📌 Increment phải demo được và có giá trị

### Khuyến nghị
💡 Tiếp tục maintain Product Backlog
💡 Refine DoD dựa trên kinh nghiệm
💡 Tăng automation testing
💡 Improve velocity estimation
