# Bài 0. Pyton - Chuỗi trong Python

Trong Python, một chuỗi là một chuỗi không thể thay đổi của các ký tự Unicode. Mỗi ký tự có một giá trị số duy nhất theo tiêu chuẩn UNICODE. Nhưng, chuỗi như một nguyên tắc, không có bất kỳ giá trị số nào ngay cả khi tất cả các ký tự đều là chữ số. Để phân biệt chuỗi khỏi số và các bộ nhận dạng khác, chuỗi các ký tự được bao quanh bằng dấu ngoặc đơn, kép hoặc ba dấu ngoặc kép trong biểu diễn chữ mạch của nó. Do đó, 1234 là một số (số nguyên) nhưng '1234' là một chuỗi.

### Tạo Chuỗi Python

Miễn là cùng một chuỗi ký tự được bao quanh, dấu ngoặc đơn, kép hoặc ba dấu ngoặc đơn không quan trọng. Do đó, các biểu diễn chuỗi sau là tương đương.

```python
>>> 'Welcome To 8SyncDev'
'Welcome To 8SyncDev'
>>> "Welcome To 8SyncDev"
'Welcome To 8SyncDev'
>>> '''Welcome To 8SyncDev'''
'Welcome To 8SyncDev'
>>> """Welcome To 8SyncDev"""
'Welcome To 8SyncDev'
```

Nhìn vào các câu lệnh trên, rõ ràng rằng Python lưu trữ chuỗi nội bộ như được bao quanh bằng dấu ngoặc đơn.

### Lấy Loại của Chuỗi Python

Một chuỗi trong Python là một đối tượng của lớp str. Điều này có thể được xác minh với hàm type().

```python
var = "Welcome To 8SyncDev"
print(type(var))
```

Nó sẽ tạo ra đầu ra sau:

```
<class 'str'>
```

### Dấu Ngoặc Đôi trong Chuỗi Python

Nếu bạn muốn nhúng một số văn bản trong dấu ngoặc kép như một phần của chuỗi, thì chính chuỗi đó nên được đặt trong dấu ngoặc đơn. Để nhúng một văn bản được trích dẫn bằng dấu ngoặc đơn, chuỗi nên được viết trong dấu ngoặc kép.

```python
var = 'Welcome to "Python Tutorial" from 8SyncDev'
print("var:", var)

var = "Welcome to 'Python Tutorial' from 8SyncDev"
print("var:", var)
```

### Dấu Ngoặc Ba

Để tạo một chuỗi bằng dấu ngoặc ba, bạn có thể sử dụng ba dấu ngoặc đơn hoặc ba dấu ngoặc kép - cả hai phiên bản đều tương tự.

```python
var = '''Welcome to 8SyncDev'''
print("var:", var)

var = """Welcome to 8SyncDev"""
print("var:", var)
```

### Chuỗi Đa Dòng Python

Chuỗi được bao quanh bằng ba dấu ngoặc kép hữu ích để tạo ra một chuỗi đa dòng.

```python
var = '''
Welcome To
Python Tutorial
from 8SyncDev
'''
print("var:", var)
```

Nó sẽ tạo ra đầu ra sau:

```
var:
Welcome To
Python Tutorial
from 8SyncDev
```

Một chuỗi là một loại dữ liệu không phải là số. Rõ ràng, chúng ta không thể sử dụng toán tử số học với các toán hạng chuỗi. Python sẽ ném ra TypeError trong trường hợp như vậy.

```python
>>> "Hello" - "World"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*