# Bài 0. Python - Tuple (Bộ)

Trong Python, Tuple là một trong những kiểu dữ liệu có sẵn. Một Tuple Python là một chuỗi các mục được phân tách bằng dấu phẩy, được đặt trong dấu ngoặc đơn (). Các mục trong Tuple Python không nhất thiết phải cùng loại dữ liệu.

Dưới đây là một số ví dụ về Tuple Python:

```python
tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)
```

Trong Python, Tuple là một kiểu dữ liệu chuỗi. Đó là một bộ sưu tập các mục được sắp xếp. Mỗi mục trong Tuple có một chỉ mục vị trí duy nhất, bắt đầu từ 0.

Trong C/C++/Java, các phần tử mảng phải cùng loại. Tuy nhiên, Tuple Python có thể chứa các đối tượng khác nhau về kiểu dữ liệu.

Tuple Python và danh sách đều là các chuỗi. Một khác biệt chính giữa hai loại này là, danh sách Python có thể thay đổi, trong khi Tuple không thể thay đổi. Mặc dù bạn có thể truy cập vào bất kỳ mục nào trong Tuple bằng cách sử dụng chỉ mục của nó và không thể sửa đổi, xóa hoặc thêm.

### Các Phép Toán Tuple Python

Trong Python, Tuple là một chuỗi. Do đó, chúng ta có thể nối hai tuple với toán tử + và nối nhiều bản sao của một tuple với toán tử "*". Các toán tử thành viên "in" và "not in" hoạt động với đối tượng tuple.

| Biểu thức Python      | Kết quả                      | Mô tả           |
| --------------------- | ---------------------------- | --------------- |
| (1, 2, 3) + (4, 5, 6) | (1, 2, 3, 4, 5, 6)           | Nối             |
| ('Hi!',) * 4          | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | Lặp lại         |
| 3 in (1, 2, 3)        | True                         | Tính thành viên |

Lưu ý rằng ngay cả khi chỉ có một đối tượng trong một Tuple, bạn phải đặt một dấu phẩy sau nó. Nếu không, nó sẽ được xem xét là một chuỗi.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*