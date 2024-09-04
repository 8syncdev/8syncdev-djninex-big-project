# Bài 5. Python - Đối số Tùy ý

Có thể bạn muốn định nghĩa một hàm có thể chấp nhận số lượng đối số tùy ý hoặc biến. Hơn nữa, số lượng đối số tùy ý có thể là đối số theo vị trí hoặc từ khóa.

Một đối số được tiền tố bằng một dấu sao (*) cho các đối số theo vị trí tùy ý.

Một đối số được tiền tố bằng hai dấu sao (**) cho các đối số từ khóa tùy ý.

### Ví dụ về Đối số Tùy ý

Dưới đây là một ví dụ về đối số tùy ý hoặc biến chiều dài theo vị trí −

```python
# Tổng các số
def add(*args):
   s = 0
   for x in args:
      s += x
   return s

result = add(10, 20, 30, 40)
print(result)

result = add(1, 2, 3)
print(result)
```

Biến args được tiền tố bằng "*" lưu trữ tất cả các giá trị được truyền cho nó. Ở đây, args trở thành một tuple. Chúng ta có thể chạy một vòng lặp qua các mục của nó để cộng các số.

Kết quả sẽ là:

```
100
6
```

### Đối số Bắt Buộc Với Đối số Tùy ý

Cũng có thể có một hàm với một số đối số bắt buộc trước dãy số lượng biến giá trị.

### Ví dụ

```python
# Trung bình của bài kiểm tra đầu tiên và tốt nhất của các bài kiểm tra tiếp theo
def avg(first, *rest):
   second = max(rest)
   return (first + second) / 2

result = avg(40, 30, 50, 25)
print(result)
```

Cuộc gọi sau đến hàm avg() truyền giá trị đầu tiên cho đối số bắt buộc đầu tiên, và các giá trị còn lại cho một tuple có tên là rest. Sau đó, chúng ta tìm giá trị tối đa và sử dụng nó để tính trung bình.

Kết quả sẽ là:

```
45.0
```

### Đối số Tùy ý Từ Khóa (**kwargs)

Nếu một biến trong danh sách đối số có hai dấu sao (*) được tiền tố cho nó, hàm có thể chấp nhận số lượng đối số từ khóa tùy ý. Biến trở thành một từ điển các cặp từ khóa: giá trị.

### Ví dụ

Dưới đây là một ví dụ về một hàm với các đối số từ khóa tùy ý. Hàm addr() có một đối số **kwargs có thể chấp nhận bất kỳ số lượng phần tử địa chỉ nào như tên, thành phố, số điện thoại, mã pin, v.v. Bên trong hàm, từ điển kwargs của các cặp khóa từ khóa: giá trị được duyệt qua sử dụng phương thức items().

```python
def addr(**kwargs):
   for k, v in kwargs.items():
      print("{}:{}".format(k, v))

print("pass two keyword args")
addr(Name="John", City="Mumbai")
print("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
```

Kết quả sẽ là:

```
pass two keyword args
Name:John
City:Mumbai
pass four keyword args
Name:Raam
City:Mumbai
ph_no:9123134567
PIN:400001
```

### Nhiều Đối số Với Đối số Tùy ý Từ Khóa

Nếu hàm sử dụng các loại đối số kết hợp, các đối số từ khóa tùy ý phải đứng sau các đối số theo vị trí, theo từ khóa và các đối số theo vị trí tùy ý trong danh sách đối số.

### Ví dụ

Hãy tưởng tượng một trường hợp trong đó môn khoa học và toán học là bắt buộc, ngoài ra học sinh có thể chọn bất kỳ số lượng môn học tự chọn nào.

Dưới đây là định nghĩa của một hàm percent() trong đó điểm số trong khoa học và điểm số được lưu trữ trong các đối số tùy ý **optional.

```python
def percent(math, sci, **optional):
   print("maths:", math)
   print("sci:", sci)
   s = math + sci
   for k, v in optional.items():
      print("{}:{}".format(k, v))
      s += v
   return s / (len(optional) + 2)

result = percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print("percentage:", result)
```

Kết quả sẽ là:

```
maths: 80
sci: 75
Eng:70
Hist:65
Geo:72
percentage: 72.4
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*