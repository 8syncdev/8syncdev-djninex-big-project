# Bài 25. Python - Nhập Dữ liệu từ Người Dùng

## Giới thiệu về Nhập Dữ liệu từ Người Dùng trong Python

Trong chương này, chúng ta sẽ tìm hiểu cách Python nhận dữ liệu đầu vào từ người dùng từ bảng điều khiển và hiển thị kết quả trên cùng một bảng điều khiển.

Mọi ứng dụng máy tính đều nên có một cơ chế để nhận đầu vào từ người dùng khi nó đang chạy. Điều này làm cho ứng dụng trở nên tương tác. Tùy thuộc vào cách phát triển, một ứng dụng có thể chấp nhận đầu vào từ người dùng dưới dạng văn bản nhập vào từ bảng điều khiển (sys.stdin), một giao diện đồ họa hoặc một giao diện dựa trên web.

## Hàm Nhập Dữ liệu từ Người Dùng trong Python

Python cung cấp cho chúng ta hai hàm tích hợp sẵn để đọc đầu vào từ bàn phím.

1. Hàm input()
2. Hàm raw_input() (trong Python 2.7)

## Hàm input() trong Python

Khi bộ thông dịch gặp phải hàm input(), nó sẽ chờ đợi người dùng nhập dữ liệu từ luồng đầu vào tiêu chuẩn (bàn phím) cho đến khi phím Enter được nhấn. Các ký tự nhập có thể được lưu trữ trong một biến chuỗi để sử dụng sau này.

## Cú pháp của hàm input() trong Python:

```python
var = input()
```

## Ví dụ về Hàm input() trong Python:

```python
name = input()
city = input()

print("Xin chào, Tên tôi là", name)
print("Tôi đến từ", city)
```

Trong ví dụ này, các biến `name` và `city` sẽ chứa dữ liệu mà người dùng nhập vào từ bàn phím.

## Hàm raw_input() trong Python

Hàm raw_input() hoạt động tương tự như hàm input(), nhưng nó chỉ có sẵn trong Python 2.7 và đã được đổi tên thành input() trong Python 3.6.

## Cú pháp của hàm raw_input() trong Python:

```python
var = raw_input([prompt text])
```

## Ví dụ về Hàm raw_input() trong Python:

```python
name = raw_input("Nhập tên của bạn: ")
city = raw_input("Nhập tên thành phố: ")

print("Xin chào, Tên tôi là", name)
print("Tôi đến từ", city)
```

Trong ví dụ này, hàm `raw_input()` sẽ hiển thị thông điệp nhắc người dùng trước khi nhập dữ liệu.

## Nhận Dữ liệu Số Trong Python

Chúng ta cũng có thể nhận dữ liệu số từ người dùng trong Python bằng cách sử dụng hàm `input()` và sau đó chuyển đổi đầu vào thành số nguyên hoặc số thực.

## Ví dụ:

```python
width = int(input("Nhập chiều rộng: "))
height = int(input("Nhập chiều cao: "))

area = width * height
print("Diện tích hình chữ nhật = ", area)
```

Trong ví dụ này, chúng ta nhập chiều rộng và chiều cao từ người dùng và tính diện tích của hình chữ nhật. Để chuyển đổi đầu vào từ dạng chuỗi thành số nguyên, chúng ta sử dụng hàm `int()`.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
