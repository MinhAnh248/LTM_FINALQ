# PHÂN CÔNG VAI TRÒ SCRUM - NHÓM 8

## Thông tin nhóm
- **Tên nhóm:** Nhóm 8
- **Môn học:** CS434S - Công Cụ & Phương Pháp Thiết Kế - Quản Lý (Phần Mềm)
- **Giảng viên:** Hồ Lê Viết Nin
- **Số thành viên:** 6 người
- **Thời gian:** 01/11/2024 - 13/12/2024 (7 tuần)

## 1. Product Owner (Chủ sở hữu sản phẩm)

### Thành viên: Ngô Thành Lâm
**MSSV:** 28211151896

**Trách nhiệm chính:**
- ✅ Quản lý Product Backlog (danh sách yêu cầu)
- ✅ Ưu tiên các tính năng phát triển
- ✅ Đảm bảo sản phẩm đáp ứng nhu cầu người dùng
- ✅ Chấp nhận kết quả sau mỗi Sprint
- ✅ Liên lạc với stakeholders

**Công việc cụ thể:**
1. Xác định 15 chức năng chính của hệ thống
2. Ưu tiên phát triển:
   - Sprint 1: Đăng nhập/Đăng ký (Foundation)
   - Sprint 2: Giao dịch, Danh mục (Core)
   - Sprint 3: Thống kê, Vay nợ, Tiết kiệm (Advanced)
   - Sprint 4: Admin, Bảo mật (Security)
3. Review và chấp nhận deliverables
4. Thu thập feedback từ người dùng
5. Điều chỉnh Product Backlog khi cần

**Chức năng phụ trách code:**
- Quản lý lịch sử các khoản chi tiêu
- Quản lý chi tiêu theo nhóm người dùng

## 2. Scrum Master (Người hướng dẫn Scrum)

### Thành viên: Vũ Đức Nguyên
**MSSV:** 28211105499

**Trách nhiệm chính:**
- ✅ Đảm bảo nhóm tuân thủ quy trình Scrum
- ✅ Tổ chức các cuộc họp Scrum
- ✅ Loại bỏ trở ngại cho nhóm
- ✅ Hỗ trợ Product Owner quản lý Backlog
- ✅ Coaching nhóm về Agile/Scrum

**Công việc cụ thể:**
1. Tổ chức Daily Standup (15 phút/ngày)
2. Tổ chức Sprint Planning (đầu Sprint)
3. Tổ chức Sprint Review (cuối Sprint)
4. Tổ chức Sprint Retrospective
5. Quản lý Trello board
6. Giải quyết conflicts trong nhóm
7. Theo dõi velocity và burndown chart
8. Code review và merge pull requests

**Chức năng phụ trách code:**
- Thống kê chi tiêu
- Phương pháp để quản lý chi tiêu

## 3. Development Team (Nhóm phát triển)

### 3.1. Backend Developer Lead

**Thành viên:** Nguyễn Quốc Vũ
**MSSV:** 28211152396

**Trách nhiệm:**
- ✅ Thiết kế kiến trúc backend
- ✅ Phát triển API endpoints
- ✅ Quản lý database
- ✅ Bảo mật hệ thống

**Công việc:**
- Setup Flask project structure
- Thiết kế database schema
- Implement JWT authentication
- Develop REST APIs
- Code review backend

**Chức năng phụ trách:**
- Tính toán số dư tài khoản
- Đưa ra cảnh báo khi vượt mức chi tiêu

### 3.2. Frontend Developer Lead

**Thành viên:** Trần Văn Thành
**MSSV:** 28211154302

**Trách nhiệm:**
- ✅ Thiết kế giao diện người dùng
- ✅ Implement responsive design
- ✅ Tích hợp với backend API
- ✅ UX/UI optimization

**Công việc:**
- Thiết kế UI/UX với Figma
- Develop HTML/CSS/JavaScript
- Implement responsive layout
- API integration
- Cross-browser testing

**Chức năng phụ trách:**
- Lập kế hoạch tiết kiệm
- Quản lý nợ

### 3.3. Full-stack Developer 1

**Thành viên:** Phan Công Sỹ
**MSSV:** 28211132240

**Trách nhiệm:**
- ✅ Phát triển cả backend và frontend
- ✅ Tích hợp các module
- ✅ Testing và debugging

**Công việc:**
- Develop features end-to-end
- Write unit tests
- Integration testing
- Bug fixing
- Documentation

**Chức năng phụ trách:**
- Ghi chép các khoản thu nhập
- Đặt giới hạn chi tiêu

### 3.4. Full-stack Developer 2

**Thành viên:** Phạm Văn Nguyên Ngọc
**MSSV:** 28214635406

**Trách nhiệm:**
- ✅ Phát triển tính năng
- ✅ Database management
- ✅ API development

**Công việc:**
- Implement business logic
- Database queries optimization
- API endpoints development
- Testing
- Code documentation

**Chức năng phụ trách:**
- Tạo ngân sách các loại quỹ
- Lời nhắc hẹn đóng tiền và thông báo

## 4. Bảng phân công chi tiết

| STT | MSSV | Thành viên | Vai trò Scrum | Chức năng code | Tỷ lệ |
|-----|------|------------|---------------|----------------|-------|
| 1 | 28211151896 | Ngô Thành Lâm | Product Owner | Quản lý lịch sử chi tiêu, Quản lý nhóm | 17.5% |
| 2 | 28211105499 | Vũ Đức Nguyên | Scrum Master | Thống kê, Phương pháp quản lý | 16.5% |
| 3 | 28211152396 | Nguyễn Quốc Vũ | Backend Lead | Tính số dư, Cảnh báo vượt mức | 16.5% |
| 4 | 28211154302 | Trần Văn Thành | Frontend Lead | Kế hoạch tiết kiệm, Quản lý nợ | 16.5% |
| 5 | 28211132240 | Phan Công Sỹ | Full-stack Dev 1 | Thu nhập, Giới hạn chi tiêu | 16.5% |
| 6 | 28214635406 | Phạm Văn Nguyên Ngọc | Full-stack Dev 2 | Ngân sách quỹ, Nhắc nhở | 16.5% |

## 5. Quy trình làm việc

### Daily Standup (Hàng ngày - 15 phút)
**Thời gian:** 9:00 AM
**Người chủ trì:** Scrum Master (Vũ Đức Nguyên)

**Format:**
```
Mỗi thành viên trả lời 3 câu hỏi:
1. Hôm qua tôi đã làm gì?
2. Hôm nay tôi sẽ làm gì?
3. Có trở ngại gì không?
```

### Sprint Planning (Đầu mỗi Sprint - 2-4 giờ)
**Người chủ trì:** Product Owner + Scrum Master

**Nội dung:**
1. Product Owner trình bày Product Backlog
2. Team chọn items cho Sprint
3. Ước lượng effort (story points)
4. Phân công công việc
5. Tạo Sprint Backlog

### Sprint Review (Cuối Sprint - 1-2 giờ)
**Người chủ trì:** Product Owner

**Nội dung:**
1. Demo các tính năng hoàn thành
2. Product Owner chấp nhận/từ chối
3. Thu thập feedback
4. Cập nhật Product Backlog

### Sprint Retrospective (Cuối Sprint - 1 giờ)
**Người chủ trì:** Scrum Master

**Nội dung:**
1. Điều gì tốt trong Sprint?
2. Điều gì cần cải thiện?
3. Hành động cải tiến cho Sprint sau?

## 6. Công cụ sử dụng

### Quản lý dự án
- **Trello:** Quản lý tasks, Sprint Backlog
- **Google Meet:** Daily Standup, Sprint meetings
- **Zalo/Telegram:** Giao tiếp hàng ngày

### Development
- **Git/GitHub:** Version control, code review
- **VS Code:** IDE chính
- **Postman:** Test API
- **Figma:** Thiết kế UI/UX

### Documentation
- **Google Docs:** Tài liệu dự án
- **Draw.io:** Vẽ biểu đồ UML
- **Markdown:** README, documentation

## 7. Quy tắc làm việc

### Git Workflow
```
1. Tạo branch từ develop: feature/ten-chuc-nang
2. Code và commit thường xuyên
3. Push lên GitHub
4. Tạo Pull Request
5. Code review (ít nhất 1 người)
6. Merge vào develop
7. Deploy lên main khi Sprint kết thúc
```

### Code Review
- Mỗi PR cần ít nhất 1 approval
- Review trong vòng 24h
- Comment constructive
- Test trước khi approve

### Definition of Done
- [ ] Code hoàn thành
- [ ] Unit test pass
- [ ] Code review approved
- [ ] Tích hợp thành công
- [ ] Không có bug critical
- [ ] Documentation cập nhật
- [ ] Demo cho Product Owner

## 8. Kết quả đạt được

### Metrics
- **Velocity trung bình:** 25 story points/sprint
- **Code coverage:** 80%+
- **Bug rate:** <5 bugs/sprint
- **On-time delivery:** 95%

### Thành công
✅ Hoàn thành 100% chức năng (15/15)
✅ Đúng deadline (7 tuần)
✅ Chất lượng code tốt
✅ Không có bug nghiêm trọng
✅ Team work hiệu quả

### Bài học
📌 Scrum giúp phát triển nhanh và linh hoạt
📌 Daily standup tăng sự phối hợp
📌 Code review cải thiện chất lượng
📌 Trello giúp quản lý công việc tốt
📌 Git workflow giảm conflicts

## 9. Liên hệ

**Product Owner:** Ngô Thành Lâm - 28211151896
**Scrum Master:** Vũ Đức Nguyên - 28211105499

**Email nhóm:** nhom8.cs434@gmail.com
**GitHub:** https://github.com/nhom8-cs434/quan-ly-chi-tieu
