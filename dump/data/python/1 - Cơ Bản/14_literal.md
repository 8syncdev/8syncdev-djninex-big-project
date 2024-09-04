# Bài 14. Python - Các Kiểu Chữ Số

**1. Giới Thiệu về Các Kiểu Chữ Số trong Python**

Các kiểu chữ số hoặc hằng số trong Python là cách biểu diễn một giá trị cố định trong mã nguồn. Khác với biến, các hằng số (123, 4.3, "Hello") là các giá trị tĩnh hoặc bạn có thể nói là các hằng số không thay đổi trong suốt hoạt động của chương trình hoặc ứng dụng. Ví dụ, trong câu lệnh gán sau:

```python
x = 10
```

Ở đây, 10 là một hằng số là giá trị số, được lưu trữ trực tiếp trong bộ nhớ. Tuy nhiên, trong Python, bạn có thể khai báo một hằng số bằng cách sử dụng từ khoá const. Điều này đảm bảo rằng giá trị của hằng số không thay đổi trong suốt quá trình chạy của chương trình.

```python
y = x*2
```

Ở đây, ngay cả khi biểu thức tính toán ra 20, nó không được thêm vào mã nguồn một cách trực tiếp. Bạn cũng có thể khai báo một đối tượng int bằng hàm `int()` tích hợp sẵn. Tuy nhiên, đây cũng là một cách khởi tạo gián tiếp và không phải là sử dụng các hằng số.

```python
x = int(10)
```

**2. Các Loại Kiểu Chữ Số trong Python**

Python cung cấp các hằng số sau sẽ được giải thích trong bài hướng dẫn này:

- Kiểu Chữ Số Nguyên
- Kiểu Chữ Số Phẩy Động
- Kiểu Chữ Số Phức
- Kiểu Chữ Số Chuỗi
- Kiểu Chữ Số Danh Sách
- Kiểu Chữ Số Tuple
- Kiểu Chữ Số Từ Điển

**3. Kiểu Chữ Số Nguyên Python**

Bất kỳ biểu diễn nào chỉ bao gồm các ký tự số (0 đến 9) sẽ tạo ra một đối tượng kiểu int. Đối tượng được khai báo như vậy có thể được tham chiếu bằng một biến bằng toán tử gán.

**Ví dụ: Biểu Diễn Số Thập Phân**

```python
x = 10
y = -25
z = 0
```

**Ví dụ: Biểu Diễn Số Bát Phân**

Python cho phép một số nguyên được biểu diễn dưới dạng số bát phân hoặc số thập lục phân. Một biểu diễn số học với chỉ tám ký tự số (0 đến 7) nhưng được tiền tố bởi 0o hoặc 0O là một số bát phân trong Python.

```python
x = 0O34
```

**Ví dụ: Biểu Diễn Số Thập Lục Phân**

Tương tự, một chuỗi các ký tự thập lục phân (0 đến 9 và a đến f), tiền tố bởi 0x hoặc 0X đại diện cho một số nguyên dưới dạng thập lục phân trong Python.

```python
x = 0X1C
```

**Ví dụ: Biểu Diễn Số Thập Phân và Thập Lục Phân**

Tuy nhiên, có thể lưu ý rằng, ngay cả khi bạn sử dụng biểu diễn số học bát phân hoặc thập lục phân, Python nội bộ xem xét chúng như là kiểu int.

```python
# Sử dụng biểu diễn bát phân
x = 0O34
print("0O34 trong bát phân là", x, type(x))
# Sử dụng biểu diễn thập lục phân
x = 0X1c
print("0X1c trong Thập lục phân là", x, type(x))
```

Khi bạn chạy mã này, nó sẽ tạo ra đầu ra sau:

```
0O34 trong bát phân là 28 <class 'int'>
0X1c trong Thập lục phân là 28 <class 'int'>
```

**4. Kiểu Chữ Số Phẩy Động Python**

Một số phẩy động bao gồm một phần nguyên và một phần thập phân. Theo quy ước, một ký tự dấu chấm thập phân (.) phân tách hai phần này trong biểu diễn hằng số của một số thực.

**Ví dụ: Kiểu Chữ Số Phẩy Động**

```python
x = 25.55
y = 0.05
z = -12.2345
```

Đối với một số thực quá lớn hoặc quá nhỏ, trong đó số chữ số trước hoặc sau dấu thập phân là nhiều hơn, một biểu diễn khoa học được sử dụng cho biểu diễn hằng số ngắn gọn. Ký hiệu E hoặc e được theo sau bởi số nguyên dương hoặc số nguyên âm, đến sau phần nguyên.

**Ví dụ: Kiểu Chữ Số Phẩy Động Biểu Diễn Khoa Học**

Ví dụ, số 1.23E05 tương đương với 123000.00. Tương tự, 1.23e-2 tương đương với 0.0123.

```python
# Sử dụng biểu diễn phẩy động thông thường
x = 1.23
print("1.23 trong kiểu chữ số phẩy động thông thường là", x, type(x))
# Sử dụng biểu diễn khoa học
x = 1.23E5
print("1.23E5 trong biểu diễn khoa học là", x, type(x))
x = 1.23E-2
print("1.23E-2 trong biểu diễn khoa học là", x, type(x))
```

Ở đây, bạn sẽ nhận được đầu ra sau:

```
1.23 trong kiểu chữ số phẩy động thông thường là 1.23 <class 'float'>
1.23E5 trong biểu diễn khoa học là 123000.0 <class 'float'>
1.23E-2 trong biểu diễn khoa học là 0.0123 <class 'float'>
```

**5. Kiểu Chữ Số Phức Python**

Một số phức bao gồm một phần thực và một phần ảo. Phần ảo là bất kỳ số nào (nguyên hoặc phẩy động) nhân với căn bậc hai của "-1" (√ −1). Trong biểu diễn hằng số, (−1−−−√
) được biểu diễn bởi "j" hoặc "J". Do đó, một biểu diễn hằng số phức có dạng x+yj.

**Ví dụ: Biểu Diễn Kiểu Chữ Số Phức**

```python
# Sử dụng biểu diễn hằng số phức
x = 2+3j
print("2+3j trong biểu diễn kiểu chữ số phức là", x, type(x))
y = 2.5+4.6j
print("2.5+4.6j trong biểu diễn kiểu chữ số phức là", x, type(x))
```

Mã này sẽ tạo ra đầu ra sau:

```
2+3j trong biểu diễn kiểu chữ số phức là (2+3j) <class 'complex'>
2.5+4.6j trong biểu diễn kiểu chữ số phức là (2+3j) <class 'complex'>
```

**6. Kiểu Chữ Số Chuỗi Python**

Một đối tượng chuỗi là một trong các loại dữ liệu dãy trong Python. Đó là một dãy không thể thay đổi của các điểm mã Unicode. Điểm mã là một số tương ứng với một ký tự theo tiêu chuẩn Unicode. Chuỗi là các đối tượng của lớp 'str' tích hợp sẵn của Python.

Chuỗi chữ số được viết bằng cách bao bọc một chuỗi các ký tự trong dấu nháy đơn ('hello'), dấu nháy kép ("hello") hoặc ba dấu nháy ('''hello''' hoặc """hello""").

**Ví dụ: Biểu Diễn Kiểu Chữ Số Chuỗi**

```python
var1 = 'hello'
print("'hello' trong dấu nháy đơn là:", var1, type(var1))
var2 = "hello"
print('"hello" trong dấu nháy kép là:', var1, type(var1))
var3 = '''hello'''
print("'''hello''' trong ba dấu nháy là:", var1, type(var1))
var4 = """hello"""
print('"""hello""" trong ba dấu nháy là:', var1, type(var1))
```

Ở đây, bạn sẽ nhận được đầu ra sau:

```
'hello' trong dấu nháy đơn là: hello <class 'str'>
"hello" trong dấu nháy kép là: hello <class 'str'>
'''hello''' trong ba dấu nháy là: hello <class 'str'>
"""hello""" trong ba dấu nháy là: hello <class 'str'>
```

**Ví dụ: Biểu Diễn Kiểu Chữ Số Chuỗi Với Dấu Nháy Đôi Trong Chuỗi**

Nếu cần nhúng dấu nháy kép là một phần của chuỗi, chuỗi chính phải được đặt trong dấu nháy đơn. Ngược lại, nếu văn bản có dấu nháy đơn cần được nhúng, chuỗi phải được viết trong dấu nháy kép.

```python
var1 = 'Welcome to "Python Tutorial" from 8 Sync Dev'
print(var1)
var2 = "Welcome to 'Python Tutorial' from 8 Sync Dev"
print(var2)
```

Nó sẽ tạo ra đầu ra sau:

```
Welcome to "Python Tutorial" from 8 Sync Dev
Welcome to 'Python Tutorial' from 8 Sync Dev
```

**7. Kiểu Chữ Số Danh Sách Python**

Đối tượng danh sách trong Python là một bộ sưu tập các đối tượng của các kiểu dữ liệu khác nhau. Danh sách là một bộ sưu tập được sắp xếp các mục không nhất thiết cùng loại. Các đối tượng cá nhân trong bộ sưu tập có thể được truy cập bằng chỉ số bắt đầu từ không.

Biểu diễn hằng số của một đối tượng danh sách được thực hiện với một hoặc nhiều mục được phân tách bằng dấu phẩy và được bao bọc trong dấu ngoặc vuông [].

**Ví dụ: Biểu Diễn Kiểu Chữ Số Danh Sách**

```python
L1 = [1, "Ravi", 75.50, True]
print(L1, type(L1))
```

Nó sẽ tạo ra đầu ra sau:

```
[1, 'Ravi', 75.5, True] <class 'list'>
```

**8. Kiểu Chữ Số Tuple Python**

Đối tượng tuple trong Python là một bộ sưu tập các đối tượng của các kiểu dữ liệu khác nhau. Tuple là một bộ sưu tập được sắp xếp các mục không nhất thiết cùng loại. Các đối tượng cá nhân trong bộ sưu tập có thể được truy cập bằng chỉ số bắt đầu từ không.

Biểu diễn hằng số của một đối tượng tuple được thực hiện với một hoặc nhiều mục được phân tách bằng dấu phẩy và được bao bọc trong dấu ngoặc đơn ().

**Ví dụ: Biểu Diễn Kiểu Chữ Số Tuple**

```python
T1 = (1, "Ravi", 75.50, True)
print(T1, type(T1))
```

Nó sẽ tạo ra đầu ra sau:

```
(1, 'Ravi', 75.5, True) <class 'tuple'>
```

**Ví dụ: Biểu Diễn Kiểu Chữ Số Tuple Không Có Dấu Ngoặc Đơn**

Dấu phân cách mặc định cho chuỗi Python là dấu ngoặc đơn, có nghĩa là một chuỗi phân tách bằng dấu phẩy mà không có dấu ngoặc đơn cũng tạo ra một tuple.

```python
T1 = 1, "Ravi", 75.50, True
print(T1, type(T1))
```

Ở đây, bạn cũng sẽ nhận được đầu ra:

```
(1, 'Ravi', 75.5, True) <class 'tuple'>
```

**9. Kiểu Chữ Số Từ Điển Python**

Giống như danh sách hoặc tuple, từ điển cũng là một kiểu dữ liệu bộ sưu tập. Tuy nhiên, nó không phải là một chuỗi. Đó là một bộ sưu tập không có thứ tự của các mục, mỗi mục là một cặp khóa-giá trị. Giá trị được gán cho khóa bằng dấu ":". Một hoặc nhiều cặp khóa:giá trị phân tách bằng dấu phẩy được đặt trong dấu ngoặc nhọn để tạo ra một đối tượng từ điển.

**Ví dụ: Biểu Diễn Kiểu Chữ Số Từ Điển**

```python
capitals = {"USA": "New York", "France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
numbers = {1: "one", 2: "Two", 3: "three", 4: "four"}
points = {"p1": (10, 10), "p2": (20, 20)}

print(capitals, type(capitals))
print(numbers, type(numbers))
print(points, type(points))
```

Đối tượng từ điển có thể sử dụng một đối tượng không thay đổi làm khóa. Số, chuỗi hoặc tuple có thể được sử dụng làm khóa. Một khóa không thể xuất hiện nhiều hơn một lần trong một bộ sưu tập. Nếu một khóa xuất hiện nhiều lần, chỉ có khóa cuối cùng được giữ lại. Giá trị có thể là bất kỳ kiểu dữ liệu nào. Một giá trị có thể được gán cho nhiều hơn một khóa. Ví dụ:

```python
staff = {"Krishna": "Officer", "Rajesh": "Manager", "Ragini": "officer", "Anil": "Clerk", "Kavita": "Manager"}
```

Hy vọng rằng những giải thích trên đã giúp bạn hiểu rõ về các loại kiểu chữ số trong Python. 

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*