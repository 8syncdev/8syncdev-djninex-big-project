# Bài 15. Python - Các Toán Tử

## Giới thiệu
Các toán tử trong Python là những ký hiệu đặc biệt (đôi khi được gọi là từ khóa) được sử dụng để thực hiện các phép toán phổ biến trên một hoặc nhiều toán hạng (giá trị, biến hoặc biểu thức).

Python hỗ trợ các loại toán tử sau:

- Toán tử số học
- Toán tử so sánh (tương đối)
- Toán tử gán
- Toán tử logic
- Toán tử bitwise (bit)
- Toán tử thành viên
- Toán tử nhận diện

Chúng ta sẽ xem xét từng loại toán tử một.

## Toán tử Số học Python

Toán tử số học được sử dụng để thực hiện các phép toán cơ bản như cộng, trừ, nhân, chia, vv.

Giả sử biến `a` chứa giá trị 10 và biến `b` chứa giá trị 20, sau đó:

| Toán tử | Tên             | Ví dụ           |
| ------- | --------------- | --------------- |
| +       | Cộng            | `a + b = 30`    |
| -       | Trừ             | `a - b = -10`   |
| *       | Nhân            | `a * b = 200`   |
| /       | Chia            | `b / a = 2`     |
| %       | Chia lấy dư     | `b % a = 0`     |
| **      | Lũy thừa        | `a**b = 10**20` |
| //      | Chia lấy nguyên | `9//2 = 4`      |

Ví dụ về Toán tử Số học Python:

```python
a = 21
b = 10
c = 0

c = a + b
print("a: {} b: {} a+b: {}".format(a, b, c))

c = a - b
print("a: {} b: {} a-b: {}".format(a, b, c))

c = a * b
print("a: {} b: {} a*b: {}".format(a, b, c))

c = a / b
print("a: {} b: {} a/b: {}".format(a, b, c))

c = a % b
print("a: {} b: {} a%b: {}".format(a, b, c))

a = 2
b = 3
c = a**b 
print("a: {} b: {} a**b: {}".format(a, b, c))

a = 10
b = 5
c = a//b 
print("a: {} b: {} a//b: {}".format(a, b, c))
```

Kết quả:

```
a: 21 b: 10 a+b: 31
a: 21 b: 10 a-b: 11
a: 21 b: 10 a*b: 210
a: 21 b: 10 a/b: 2.1
a: 21 b: 10 a%b: 1
a: 2 b: 3 a**b: 8
a: 10 b: 5 a//b: 2
```

## Toán tử So sánh (Tương đối) Python

Toán tử so sánh so sánh các giá trị ở hai bên và quyết định mối quan hệ giữa chúng.

Giả sử biến `a` chứa giá trị 10 và biến `b` chứa giá trị 20, sau đó:

| Toán tử | Tên               | Ví dụ                 |
| ------- | ----------------- | --------------------- |
| ==      | Bằng              | `(a == b)` không đúng |
| !=      | Không bằng        | `(a != b)` đúng       |
| >       | Lớn hơn           | `(a > b)` không đúng  |
| <       | Nhỏ hơn           | `(a < b)` đúng        |
| >=      | Lớn hơn hoặc bằng | `(a >= b)` không đúng |
| <=      | Nhỏ hơn hoặc bằng | `(a <= b)` đúng       |

Ví dụ về Toán tử So sánh Python:

```python
a = 21
b = 10

if (a == b):
   print("Dòng 1 - a bằng b")
else:
   print("Dòng 1 - a không bằng b")

if (a != b):
   print("Dòng 2 - a không bằng b")
else:
   print("Dòng 2 - a bằng b")

if (a < b):
   print("Dòng 3 - a nhỏ hơn b")
else:
   print("Dòng 3 - a không nhỏ hơn b")

if (a > b):
   print("Dòng 4 - a lớn hơn b")
else:
   print("Dòng 4 - a không lớn hơn b")

a, b = b, a  # Giá trị của a và b đã đổi. a trở thành 10, b trở thành 21

if (a <= b):
   print("Dòng 5 - a nhỏ hơn hoặc bằng b")
else:
   print("Dòng 5 - a không nhỏ hơn hoặc bằng b")

if (b >= a):
   print("Dòng 6 - b lớn hơn hoặc bằng b")
else:
   print("Dòng 6 - b không lớn hơn hoặc bằng b")
```

Kết quả:

```
Dòng 1 - a không bằng b
Dòng 2 - a không bằng b
Dòng 3 - a không nhỏ hơn b
Dòng 4 - a lớn hơn b
Dòng 5 - a nhỏ hơn hoặc bằng b
Dòng 6 - b lớn hơn hoặc bằng a
```


## Toán tử Gán Python

Toán tử gán được sử dụng để gán giá trị cho các biến. Bảng dưới đây liệt kê tất cả các toán tử gán trong Python:

| Toán tử | Ví dụ     | Tương đương  |
| ------- | --------- | ------------ |
| =       | `a = 10`  | `a = 10`     |
| +=      | `a += 30` | `a = a + 30` |
| -=      | `a -= 15` | `a = a - 15` |
| *=      | `a *= 10` | `a = a * 10` |
| /=      | `a /= 5`  | `a = a / 5`  |
| %=      | `a %= 5`  | `a = a % 5`  |
| **=     | `a **= 4` | `a = a ** 4` |
| //=     | `a //= 5` | `a = a // 5` |
| &=      | `a &= 5`  | `a = a & 5`  |
| \|=     | `a \|= 5` | `a = a \| 5` |
| ^=      | `a ^= 5`  | `a = a ^ 5`  |
| >>=     | `a >>= 5` | `a = a >> 5` |
| <<=     | `a <<= 5` | `a = a << 5` |

Ví dụ về Toán tử Gán Python:

```python
a = 21
b = 10
c = 0
print("a: {} b: {} c : {}".format(a, b, c))

c = a + b
print("a: {}  c = a + b: {}".format(a, c))

c += a
print("a: {} c += a: {}".format(a, c))

c *= a
print("a: {} c *= a: {}".format(a, c))

c /= a
print("a: {} c /= a : {}".format(a, c))

c = 2
print("a: {} b: {} c : {}".format(a, b, c))
c %= a
print("a: {} c %= a: {}".format(a, c))

c **= a
print("a: {} c **= a: {}".format(a, c))

c //= a
print("a: {} c //= a: {}".format(a, c))
```

Kết quả:

```
a: 21 b: 10 c : 0
a: 21  c = a + b: 31
a: 21 c += a: 52
a: 21 c *= a: 1092
a: 21 c /= a : 52.0
a: 21 b: 10 c : 2
a: 21 c %= a: 2
a: 21 c **= a: 2097152
a: 21 c //= a: 99864
```

## Toán tử Bitwise Python

Toán tử Bitwise hoạt động trên các bit và thực hiện các phép toán bit từng bit. Những toán tử này được sử dụng để so sánh các số nhị phân.

Python hỗ trợ các toán tử Bitwise sau:

| Toán tử | Tên       | Ví dụ    |
| ------- | --------- | -------- |
| &       | AND       | `a & b`  |
| \|      | OR        | `a \| b` |
| ^       | XOR       | `a ^ b`  |
| ~       | NOT       | `~a`     |
| <<      | Dịch trái | `a << 3` |
| >>      | Dịch phải | `a >> 3` |

Ví dụ về Toán tử Bitwise Python:

```python
a = 20            
b = 10            

print('a =', a, ':', bin(a), 'b =', b, ':', bin(b))
c = 0

c = a & b        
print("Kết quả của AND là ", c, ':', bin(c))

c = a | b     
print("Kết quả của OR là ", c, ':', bin(c))

c = a ^ b        
print("Kết quả của XOR là ", c, ':', bin(c))

c = ~a           
print("Kết quả của NOT là ", c, ':', bin(c))

c = a << 2       
print("Kết quả của Dịch trái là ", c, ':', bin(c))

c = a >> 2       
print("Kết quả của Dịch phải là ", c, ':', bin(c))
```

Kết quả:

```
a = 20 : 0b10100 b = 10 : 0b1010
Kết quả của AND là  0 : 0b0
Kết quả của OR là  30 : 0b11110
Kết quả của XOR là  30 : 0b11110
Kết quả của NOT là  -21 : -0b10101
Kết quả của Dịch trái là  80 : 0b1010000
Kết quả của Dịch phải là  5 : 0b101
```

## Toán tử Logic Python

Toán tử logic Python được sử dụng để kết hợp hai hoặc nhiều điều kiện và kiểm tra kết quả cuối cùng. Có ba toán tử logic sau được hỗ trợ bởi ngôn ngữ Python:

| Toán tử | Tên | Ví dụ     |
| ------- | --- | --------- |
| and     | AND | `a and b` |
| or      | OR  | `a or b`  |
| not     | NOT | `not(a)`  |

Ví dụ về Toán tử Logic Python:

```python
var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))
```

Kết quả:

```
True
True
False
```

## Toán tử Thành viên Python

Toán tử thành viên của Python kiểm tra sự tồn tại của một biến trong một chuỗi, như chuỗi, danh sách hoặc tuple. Có hai toán tử thành viên như sau:

| Toán tử | Mô tả                                                                | Ví dụ        |
| ------- | -------------------------------------------------------------------- | ------------ |
| in      | Trả về True nếu nó tìm thấy một biến trong chuỗi được chỉ định       | `a in b`     |
| not in  | Trả về True nếu nó không tìm thấy một biến trong chuỗi được chỉ định | `a not in b` |

Ví dụ về Toán tử Thành viên Python:

```python
a = 10
b = 20
list = [1, 2, 3, 4, 5]

print("a:", a, "b:", b, "list:", list)

if (a in list):
   print("a có trong danh sách đã cho")
else:
   print("a không có trong danh sách đã cho")

if (b not in list):
   print("b không có trong danh sách đã cho")
else:
   print("b có trong danh sách đã cho")

c = b / a
print("c:", c, "list:", list)

if (c in list):
   print("c có trong danh sách đã cho")
else:
    print("c không có trong danh sách đã cho")
```

Kết quả:

```
a: 10 b: 20 list: [1, 2, 3, 4, 5]
a không có trong danh sách đã cho
b không có trong danh sách đã cho
c có trong danh sách đã cho
```

## Toán tử Nhận diện Python

Toán tử nhận diện so sánh các vị trí bộ nhớ của hai đối tượng. Có hai toán tử nhận diện như sau:

| Toán tử | Mô tả                                                        | Ví dụ        |
| ------- | ------------------------------------------------------------ | ------------ |
| is      | Trả về True nếu cả hai biến đều trỏ đến cùng một đối tượng   | `a is b`     |
| is not  | Trả về True nếu cả hai biến không trỏ đến cùng một đối tượng | `a is not b` |

Ví dụ về Toán tử Nhận diện Python:

```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)
```

Kết quả:

```
True
False
False
True
```

## Ưu Tiên Toán Tử Python

Bảng dưới đây liệt kê tất cả các toán tử từ ưu tiên cao nhất đến thấp nhất.

| STT | Toán tử                                    | Mô tả                                    |
| --- | ------------------------------------------ | ---------------------------------------- |
| 1   | **                                         | Lũy thừa                                 |
| 2   | ~ + -                                      | Bù 1, dấu âm, dấu dương                  |
| 3   | * / % //                                   | Nhân, chia, chia lấy dư, chia lấy nguyên |
| 4   | + -                                        | Cộng, trừ                                |
| 5   | >> <<                                      | Dịch trái, dịch phải                     |
| 6   | &                                          | AND                                      |
| 7   | ^ \|                                       | XOR, OR                                  |
| 8   | <= < > >=                                  | So sánh                                  |
| 9   | == !=                                      | So sánh                                  |
| 10  | = %= /= //= -= += *= **= <<= >>= &= \|= ^= | Gán                                      |
| 11  | is is not                                  | Nhận diện                                |
| 12  | in not in                                  | Thành viên                               |
| 13  | not or and                                 | Logic                                    |

Đây là tài liệu về các toán tử trong Python. Hy vọng nó hữu ích cho bạn!


Trên đây là tài liệu chi tiết về các toán tử trong Python, được viết bằng tiếng Việt với định dạng đẹp và tổ chức cấu trúc rõ ràng. 

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn!*
