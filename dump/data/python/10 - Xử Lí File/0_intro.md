# Bài 00. Python - Xử Lý Tệp Trong Python

Khi sử dụng bất kỳ ứng dụng máy tính nào, đôi khi cần cung cấp dữ liệu. Dữ liệu được lưu trữ trong bộ nhớ chính của máy tính (RAM) cho đến khi ứng dụng đang chạy. Sau đó, nội dung bộ nhớ từ RAM sẽ bị xóa.

Chúng ta muốn lưu trữ nó theo cách sao cho có thể được truy xuất khi cần thiết trên một phương tiện lưu trữ liên tục như một tệp đĩa.

Python sử dụng các hàm input() và print() tích hợp để thực hiện các hoạt động nhập/ xuất tiêu chuẩn. Chương trình Python tương tác với các thiết bị IO thông qua các đối tượng dòng tiêu chuẩn stdin và stdout được xác định trong mô-đun sys.

Hàm input() đọc các byte từ một thiết bị dòng nhập tiêu chuẩn, tức là bàn phím. Do đó, cả hai câu lệnh sau đều đọc đầu vào từ người dùng.

```python
name = input()
# tương đương với
import sys
name = sys.stdin.readline()
```

Hàm print() gửi dữ liệu đến thiết bị dòng xuất tiêu chuẩn, tức là màn hình hiển thị. Đó là một hàm tiện ích mô phỏng phương thức write() của đối tượng stdout.

```python
print(name)
# tương đương với
import sys
sys.stdout.write(name)
```

Bất kỳ đối tượng nào tương tác với dòng nhập và dòng xuất được gọi là đối tượng Tệp. Hàm tích hợp open() của Python trả về một đối tượng tệp.

## Hàm open()

Hàm này tạo một đối tượng tệp, sẽ được sử dụng để gọi các phương thức hỗ trợ khác liên quan đến nó.

**Cú pháp**
```python
đối tượng tệp = open(tên_tệp [, chế_độ_truy_cập][, đệm])
```

Dưới đây là chi tiết về các tham số:

- `tên_tệp` − Đối số `tên_tệp` là một chuỗi chứa tên của tệp mà bạn muốn truy cập.

- `chế_độ_truy_cập` − `chế_độ_truy_cập` xác định chế độ mà tệp phải được mở, tức là đọc, ghi, thêm, v.v. Một danh sách hoàn chỉnh các giá trị có thể có được đưa ra dưới dạng bảng bên dưới. Đây là một tham số tùy chọn và chế độ truy cập tệp mặc định là đọc (r).

- `đệm` − Nếu giá trị `đệm` được đặt thành 0, không có việc đệm nào xảy ra. Nếu giá trị `đệm` được đặt thành 1, việc đệm dòng được thực hiện khi truy cập một tệp. Nếu bạn chỉ định giá trị `đệm` là một số nguyên lớn hơn 1, sau đó hành động đệm được thực hiện với kích thước đệm chỉ định. Nếu âm, kích thước đệm là mặc định của hệ thống (hành vi mặc định).

## Chế Độ Mở Tệp

Dưới đây là các chế độ mở tệp:

| Chế Độ | Mô Tả |
|--------|-------|
| `r`    | Mở tệp chỉ để đọc. Trình chỉ mục tệp được đặt ở đầu tệp. Đây là chế độ mặc định. |
| `rb`   | Mở tệp chỉ để đọc ở định dạng nhị phân. Trình chỉ mục tệp được đặt ở đầu tệp. Đây là chế độ mặc định. |
| `r+`   | Mở tệp để cả đọc và ghi. Trình chỉ mục tệp được đặt ở đầu tệp. |
| `rb+`  | Mở tệp để cả đọc và ghi ở định dạng nhị phân. Trình chỉ mục tệp được đặt ở đầu tệp. |
| `w`    | Mở tệp chỉ để ghi. Nếu tệp đã tồn tại, tệp sẽ bị ghi đè. Nếu tệp không tồn tại, tạo tệp mới để ghi. |
| `b`    | Mở tệp trong chế độ nhị phân |
| `t`    | Mở tệp trong chế độ văn bản (mặc định) |
| `+`    | Mở tệp để cập nhật (đọc và ghi) |
| `wb`   | Mở tệp chỉ để ghi ở định dạng nhị phân. Nếu tệp đã tồn tại, tệp sẽ bị ghi đè. Nếu tệp không tồn tại, tạo tệp mới để ghi. |
| `w+`   | Mở tệp để cả ghi và đọc. Nếu tệp đã tồn tại, tệp sẽ bị ghi đè. Nếu tệp không tồn tại, tạo tệp mới để đọc và ghi. |
| `wb+`  | Mở tệp để cả ghi và đọc ở định dạng nhị phân. Nếu tệp đã tồn tại, tệp sẽ bị ghi đè. Nếu tệp không tồn tại, tạo tệp mới để đọc và ghi. |
| `a`    | Mở tệp để thêm. Trình chỉ mục tệp được đặt ở cuối tệp. Nếu tệp không tồn tại, tạo tệp mới để thêm. |
| `ab`   | Mở tệp để thêm ở định dạng nhị phân. Trình chỉ mục tệp được đặt ở cuối tệp. Nếu tệp không tồn tại, tạo tệp mới để thêm. |
| `a+`   | Mở tệp để cả thêm và đọc. Trình chỉ mục tệp được đặt ở cuối tệp. Nếu tệp không tồn tại, tạo tệp mới để thêm và đọc. |
| `ab+`  | Mở tệp để cả thêm và đọc ở định dạng nhị phân. Trình chỉ mục tệp được đặt ở cuối tệp. Nếu tệp không tồn tại, tạo tệp mới để thêm và đọc. |
| `x`    | Mở để tạo mới, không ghi đè nếu tệp đã tồn tại |

Một khi một tệp đã được mở và bạn có một đối tượng tệp, bạn có thể lấy được các thông tin khác nhau liên quan đến tệp đó.

**Ví dụ**

```python
# Mở một tệp
fo = open("foo.txt", "wb")
print("Tên của tệp: ", fo.name)
print("Đã đóng hay chưa: ", fo.closed)
print("Chế độ mở: ", fo.mode)
fo.close()
```

Kết quả sẽ là:

```
Tên của tệp:  foo.txt
Đã đóng hay chưa:  False
Chế độ mở:  wb
```