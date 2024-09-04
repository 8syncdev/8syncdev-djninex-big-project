# Bài 4. Python - Đối số theo Vị trí

Danh sách các biến được khai báo trong dấu ngoặc đơn tại thời điểm định nghĩa một hàm là các đối số hình thức. Một hàm có thể được định nghĩa với bất kỳ số lượng đối số hình thức nào.

Khi gọi một hàm:

- Tất cả các đối số là bắt buộc
- Số lượng đối số thực phải bằng số lượng đối số hình thức.
- Các đối số hình thức là vị trí. Chúng nhận các giá trị theo thứ tự được định nghĩa.
- Kiểu của các đối số phải khớp nhau.
- Tên của các đối số hình thức và thực tế không cần phải giống nhau.

### Ví dụ về Đối số theo Vị trí

```python
def add(x, y):
   z = x + y
   print("x={} y={} x+y={}".format(x, y, z))

a = 10
b = 20
add(a, b)
```

Kết quả sẽ là:

```
x=10 y=20 x+y=30
```

Ở đây, hàm add() có hai đối số hình thức, cả hai đều là số. Khi các số nguyên 10 và 20 được truyền vào. Biến a lấy giá trị 10 và b lấy giá trị 20, theo thứ tự được khai báo. Hàm add() hiển thị tổng.

Python cũng sẽ tạo ra lỗi khi số lượng đối số không khớp. Hãy chỉ đưa ra một đối số và kiểm tra kết quả.

```
add(b)
TypeError: add() missing 1 required positional argument: 'y'
```

Hãy truyền nhiều hơn số lượng đối số hình thức và kiểm tra kết quả −

```
add(10, 20, 30)
TypeError: add() takes 2 positional arguments but 3 were given
```

Kiểu dữ liệu của các đối số thực và hình thức tương ứng phải khớp nhau. Thay đổi a thành một giá trị chuỗi và kiểm tra kết quả.

```python
a = "Hello"
b = 20
add(a, b)
```

Nó sẽ tạo ra kết quả sau:

```
z = x + y
    ~^~
TypeError: can only concatenate str (not "int") to str
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*