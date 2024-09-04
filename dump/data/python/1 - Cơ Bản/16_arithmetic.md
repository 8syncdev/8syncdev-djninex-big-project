# Bài 16. Python - Các Toán Tử Số Học

Trong Python, các số là loại dữ liệu được sử dụng phổ biến nhất. Python sử dụng các ký hiệu giống như các phép toán số học cơ bản mà mọi người đều quen thuộc, tức là "+" cho phép cộng, "-" cho phép trừ, "*" cho phép nhân (hầu hết các ngôn ngữ lập trình sử dụng "*" thay vì "x" như được sử dụng trong toán học / đại số), và "/" cho phép chia (một lần nữa cho "÷" được sử dụng trong Toán học).

Ngoài ra, Python định nghĩa một số toán tử số học khác. Chúng là "%" (Phần dư), "**" (Lũy thừa) và "//" (Chia lấy phần nguyên).

## Các Toán Tử Số Học Python

Các toán tử số học là các toán tử nhị phân vì chúng hoạt động trên hai toán hạng. Python hỗ trợ hoàn toàn phép tính hỗn hợp. Đó là, hai toán hạng có thể thuộc hai loại số khác nhau. Trong tình huống như vậy, Python mở rộng toán hạng hẹp hơn. Một đối tượng số nguyên hẹp hơn một đối tượng số thực, và số thực hẹp hơn số phức. Do đó, kết quả của phép toán số học giữa số nguyên và số thực là một số thực. Kết quả của số thực và một số phức là một số phức, tương tự, phép tính trên một số nguyên và một đối tượng số phức sẽ cho kết quả là một đối tượng số phức.

## Các Toán Tử Số Học Khác nhau trong Python

Dưới đây là bảng liệt kê tất cả các toán tử số học có sẵn trong Python:

| Toán tử | Tên         | Ví dụ        |
| ------- | ----------- | ------------ |
| +       | Cộng        | a + b = 30   |
| -       | Trừ         | a – b = -10  |
| *       | Nhân        | a * b = 200  |
| /       | Chia        | b / a = 2    |
| %       | Phần dư     | b % a = 0    |
| **      | Lũy thừa    | a**b =10**20 |
| //      | Chia lấy dư | 9//2 = 4     |

Hãy cùng tìm hiểu các toán tử này thông qua các ví dụ.

### Toán Tử Cộng (+)

Toán tử này được phát âm là "cộng", là một toán tử số học cơ bản. Nó cộng hai toán hạng số học ở hai bên và trả về kết quả cộng.

#### Ví dụ: Cộng Hai Số Nguyên

Trong ví dụ sau, hai biến số nguyên là các toán hạng cho toán tử "+".

```python
a=10
b=20
print ("Tổng của hai số nguyên:")
print ("a =",a,"b =",b,"tổng =",a+b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tổng của hai số nguyên
a = 10 b = 20 tổng = 30
```

#### Ví dụ: Cộng Số Nguyên và Số Thực

Cộng một số nguyên và một số thực sẽ cho kết quả là một số thực.

```python
a=10
b=20.5
print ("Tổng của số nguyên và số thực")
print ("a =",a,"b =",b,"tổng =",a+b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tổng của số nguyên và số thực
a = 10 b = 20.5 tổng = 30.5
```

#### Ví dụ: Cộng Hai Số Phức

Kết quả của việc thêm số thực vào số phức là một số phức.

```python
a=10+5j
b=20.5
print ("Tổng của số phức và số thực")
print ("a=",a,"b=",b,"tổng=",a+b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tổng của số phức và số thực
a= (10+5j) b= 20.5 tổng= (30.5+5j)
```

### Toán Tử Trừ (-)

Toán tử này, được biết đến như là "trừ", trừ toán hạng thứ hai khỏi toán hạng đầu tiên. Số kết quả là âm nếu toán hạng thứ hai lớn hơn.

#### Ví dụ: Trừ Hai Số Nguyên

Ví dụ đầu tiên cho thấy sự trừ của hai số nguyên.

```python
a=10
b=20
print ("Hiệu của hai số nguyên:")
print ("a =",a,"b =",b,"a-b =",a-b)
print ("a =",a,"b =",b,"b-a =",b-a)
```

Kết quả:

```
Hiệu của hai số nguyên
a = 10 b = 20 a-b = -10
a = 10 b = 20 b-a = 10
```

#### Ví dụ: Trừ Số Nguyên và Số Thực

Phép trừ của một số nguyên và một số thực tuân theo nguyên tắc tương tự.

```python
a=10
b=20.5
print ("Hiệu của python số nguyên và số thực")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)
```

Nó sẽ tạo ra đầu ra sau:

```
Hiệu của số nguyên và số thực
a= 10 b= 20.5 a-b= -10.5
a= 10 b= 20.5 b-a= 10.5
```

#### Ví dụ: Trừ Hai Số Phức

Trong phép trừ liên quan đến một số phức và một số thực, phần thực được sử dụng trong phép tính.

```python
a=10+5j
b=20.5
print ("Hiệu của số phức và số thực")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)
```

Nó sẽ tạo ra đầu ra sau:

```
Hiệu của số phức và số thực
a= (10+5j) b= 20.5 a-b= (-10.5+5j)
a= (10+5j) b= 20.5 b-a= (10.5-5j)
```

### Toán Tử Nhân (*)

Ký hiệu * (dấu hoa thị) được định nghĩa như một toán tử nhân trong Python (như trong nhiều ngôn ngữ). Nó trả về tích của hai toán hạng ở hai bên của nó. Nếu bất kỳ toán hạng nào là số âm, kết quả cũng là số âm. Nếu cả hai đều âm, kết quả là dương. Thay đổi thứ tự của các toán hạng không làm thay đổi kết quả.

#### Ví dụ: Nhân Hai Số Nguyên

```python
a=10
b=20
print ("Tích của hai số nguyên")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tích của hai số nguyên
a = 10 b = 20 a*b = 200
```

#### Ví dụ: Nhân Số Nguyên và Số Thực

Trong phép nhân, một toán hạng số thực có thể có một biểu thức thập phân tiêu chuẩn, hoặc một biểu thức khoa học.

```python
a=10
b=20.5
print ("Tích của số nguyên và số thực")
print ("a=",a,"b=",b,"a*b=",a*b)

a=-5.55
b=6.75E-3
print ("Tích của số thực và số thực")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tích của số nguyên và số thực
a = 10 b = 20.5 a-b = -10.5
Tích của số thực và số thực
a = -5.55 b = 0.00675 a*b = -0.037462499999999996
```

#### Ví dụ: Nhân Với Số Phức

Đối với phép nhân có một toán hạng số phức, toán hạng khác nhân cả phần thực và phần ảo.

```python
a=10+5j
b=20.5
print ("Tích của số phức và số thực")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Nó sẽ tạo ra đầu ra sau:

```
Tích của số phức và số thực
a = (10+5j) b = 20.5 a*b = (205+102.5j)
```

### Toán Tử Chia (/)

Toán tử "/" (dấu gạch chéo) thường được gọi là gạch chéo phía trước. Kết quả của toán tử chia là tử số (toán hạng bên trái) chia cho mẫu số (toán hạng bên phải). Số kết quả là âm nếu bất kỳ toán hạng nào là số âm. Vì vô cùng không thể được lưu trữ trong bộ nhớ, Python ném ra lỗi ZeroDivisionError nếu mẫu số là 0. Kết quả của toán tử chia trong Python luôn là một số thực, ngay cả khi cả hai toán hạng đều là số nguyên.

#### Ví dụ: Chia Hai Số Nguyên

```python
a=10
b=20
print ("Chia của hai số nguyên")
print ("a=",a,"b=",b,"a/b=",a/b)
print ("a=",a,"b=",b,"b/a=",b/a)
```

Nó sẽ tạo ra đầu ra sau:

```
Chia của hai số nguyên
a= 10 b= 20 a/b= 0.5
a= 10 b= 20 b/a= 2.0
```

#### Ví dụ: Chia Với Số Thực

Trong phép chia, một toán hạng số thực có thể có một biểu thức thập phân tiêu chuẩn, hoặc một biểu thức khoa học.

```python
a=10
b=-20.5
print ("Chia của số nguyên và số thực")
print ("a=",a,"b=",b,"a/b=",a/b)

a=-2.50
b=1.25E2
print ("Chia của số thực và số thực")
print ("a=",a,"b=",b,"a/b=",a/b)
```

Nó sẽ tạo ra đầu ra sau:

```
Chia của số nguyên và số thực
a= 10 b= -20.5 a/b= -0.4878048780487805
Chia của số thực và số thực Số nguyên và số thực
```python
a=10
b=20.5
print ("Hiệu của số nguyên và số thực")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)
```
Sẽ tạo ra đầu ra sau:

```
Hiệu của số nguyên và số thực
a= 10 b= 20.5 a-b= -10.5
a= 10 b= 20.5 b-a= 10.5
```

#### Ví dụ: Trừ Hai Số Phức

Trong phép trừ liên quan đến một số phức và một số thực, thành phần thực được sử dụng trong phép tính.

```python
a=10+5j
b=20.5
print ("Hiệu của số phức và số thực")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)
```

Nó sẽ tạo ra đầu ra sau:

```
Hiệu của số phức và số thực
a= (10+5j) b= 20.5 a-b= (-10.5+5j)
a= (10+5j) b= 20.5 b-a= (10.5-5j)
```

### Toán Tử Nhân (*)

Ký hiệu * (asterisk) được định nghĩa là toán tử nhân trong Python (như trong nhiều ngôn ngữ). Nó trả về tích của hai toán hạng ở hai bên. Nếu bất kỳ toán hạng nào là số âm, kết quả cũng là số âm. Nếu cả hai đều âm, kết quả là dương. Thay đổi thứ tự của các toán hạng không làm thay đổi kết quả.

#### Ví dụ: Nhân Hai Số Nguyên

```python
a=10
b=20
print ("Tích của hai số nguyên")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Sẽ tạo ra đầu ra sau:

```
Tích của hai số nguyên
a = 10 b = 20 a*b = 200
```

#### Ví dụ: Nhân Số Nguyên và Số Thực

Trong phép nhân, một toán hạng số thực có thể có một biểu diễn thập phân tiêu chuẩn hoặc một biểu diễn toán học.

```python
a=10
b=20.5
print ("Tích của số nguyên và số thực")
print ("a=",a,"b=",b,"a*b=",a*b)

a=-5.55
b=6.75E-3
print ("Tích của số thực và số thực")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Sẽ tạo ra đầu ra sau:

```
Tích của số nguyên và số thực
a = 10 b = 20.5 a-b = -10.5
Tích của số thực và số thực
a = -5.55 b = 0.00675 a*b = -0.037462499999999996
```

#### Ví dụ: Nhân Với Số Phức

Đối với phép nhân liên quan đến một toán hạng phức, toán hạng còn lại nhân cả phần thực và phần ảo.

```python
a=10+5j
b=20.5
print ("Tích của số phức và số thực")
print ("a =",a,"b =",b,"a*b =",a*b)
```

Sẽ tạo ra đầu ra sau:

```
Tích của số phức và số thực
a = (10+5j) b = 20.5 a*b = (205+102.5j)
```

### Toán Tử Chia (/)

Dấu "/" thường được gọi là dấu gạch chéo. Kết quả của toán tử chia là tử số (toán hạng trái) chia cho mẫu số (toán hạng phải). Số kết quả là âm nếu bất kỳ toán hạng nào là số âm. Vì vô hạn không thể được lưu trữ trong bộ nhớ, Python ném ra ZeroDivisionError nếu mẫu số là 0. Kết quả của toán tử chia trong Python luôn là một số thực, ngay cả khi cả hai toán hạng đều là số nguyên.

#### Ví dụ: Chia Hai Số Nguyên

```python
a=10
b=20
print ("Chia của hai số nguyên")
print ("a=",a,"b=",b,"a/b=",a/b)
print ("a=",a,"b=",b,"b/a=",b/a)
```

Sẽ tạo ra đầu ra sau:

```
Chia của hai số nguyên
a= 10 b= 20 a/b= 0.5
a= 10 b= 20 b/a= 2.0
```

#### Ví dụ: Chia Với Số Thực

Trong phép chia, một toán hạng số thực có thể có một biểu diễn thập phân tiêu chuẩn hoặc một biểu diễn toán học.

```python
a=10
b=-20.5
print ("Chia của số nguyên và số thực")
print ("a=",a,"b=",b,"a/b=",a/b)
a=-2.50
b=1.25E2
print ("Chia của số thực và số thực")
print ("a=",a,"b=",b,"a/b=",a/b)
```

Sẽ tạo ra đầu ra sau:

```
Chia của số nguyên và số thực
a= 10 b= -20.5 a/b= -0.4878048780487805
Chia của số thực và số thực
a= -2.50 b= 125.0 a/b= -0.02
```

#### Ví dụ: Chia Với Số Phức

Khi một trong các toán hạng là một số phức, phép chia giữa toán hạng còn lại và cả hai phần của đối tượng số phức (phần thực và ảo) đều xảy ra.

```python
a=7.5+7.5j
b=2.5
print ("Chia của số phức và số thực")
print ("a =",a,"b =",b,"a/b =",a/b)
print ("a =",a,"b =",b,"b/a =",b/a)
```

Sẽ tạo ra đầu ra sau:

```
Chia của số phức và số thực
a = (7.5+7.5j) b = 2.5 a/b = (3+3j)
a = (7.5+7.5j) b = 2.5 b/a = (0.16666666666666666-0.16666666666666666j)
```

Nếu tử số là 0, kết quả của phép chia luôn là 0 ngoại trừ khi mẫu số là 0, trong trường hợp này, Python ném ra ZeroDivisionError với thông báo lỗi Phép Chia Cho Không.

```python
a=0
b=2.5
print ("a=",a,"b=",b,"a/b=",a/b)
print ("a=",a,"b=",b,"b/a=",b/a)
```

Sẽ tạo ra đầu ra sau:

```
a= 0 b= 2.5 a/b= 0.0
Traceback (most recent call last):
  File "C:\Users\mlath\examples\example.py", line 20, in <module>
     print ("a=",a,"b=",b,"b/a=",b/a)
                                 ~^~
ZeroDivisionError: float division by zero
```

### Toán Tử Lấy Dư (%)

Python định nghĩa ký hiệu "%" được gọi là ký hiệu Phần Trăm, là toán tử Lấy Dư (hoặc phần dư). Nó trả về phần dư sau khi mẫu số chia tử số. Nó cũng có thể được gọi là toán tử dư dư. Kết quả của toán tử lấy dư là số còn lại sau khi chia tỷ lệ nguyên. Ví dụ, khi 10 chia 3, tỷ lệ là 3 và phần dư là 1. Do đó, 10%3 (thường được phát âm là 10 mod 3) kết quả là 1.

#### Ví dụ: Phép Lấy Dư Với Giá Trị Số Nguyên

Nếu cả hai toán hạng đều là số nguyên, giá trị phần dư là một số nguyên. Nếu tử số có thể chia hết, phần dư là 0. Nếu tử số nhỏ hơn mẫu số, phần dư bằng tử số. Nếu mẫu số là 0, Python ném ra ZeroDivisionError.

```python
a=10
b=2
print ("a=",a, "b=",b, "a%b=", a%b)
a=10
b=4
print ("a=",a, "b=",b, "a%b=", a%b)
print ("a=",a, "b=",b, "b%a=", b%a)
a=0
b=10
print ("a=",a, "b=",b, "a%b=", a%b)
print ("a=", a, "b=", b, "b%a=",b%a)
```

Sẽ tạo ra đầu ra sau:

```
a= 10 b= 2 a%b= 0
a= 10 b= 4 a%b= 2
a= 10 b= 4 b%a= 4
a= 0 b= 10 a%b= 0
Traceback (most recent call last):
  File "C:\Users\mlath\examples\example.py", line 13, in <module>
    print ("a=", a, "b=", b, "b%a=",b%a)
                                    ~^~
ZeroDivisionError: integer modulo by zero
```

#### Ví dụ: Phép Lấy Dư Với Giá Trị Số Thực

Nếu một trong các toán hạng là một số thực, giá trị mod luôn là số thực.

```python
a=10
b=2.5
print ("a=",a, "b=",b, "a%b=", a%b)
a=10
b=1.5
print ("a=",a, "b=",b, "a%b=", a%b)
a=7.7
b=2.5
print ("a=",a, "b=",b, "a%b=", a%b)
a=12.4
b=3
print ("a=",a, "b=",b, "a%b=", a%b)
```

Sẽ tạo ra đầu ra sau:

```
a= 10 b= 2.5 a%b= 0.0
a= 10 b= 1.5 a%b= 1.0
a= 7.7 b= 2.5 a%b= 0.20000000000000018
a= 12.4 b= 3 a%b= 0.40000000000000036
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
