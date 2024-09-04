# Bài 10.1. Python break Statement

Câu lệnh break trong Python được sử dụng để kết thúc vòng lặp hiện tại và tiếp tục thực thi tại câu lệnh tiếp theo, tương tự như câu lệnh break truyền thống trong C.

Cách sử dụng phổ biến nhất cho câu lệnh break trong Python là khi một điều kiện bên ngoài được kích hoạt yêu cầu một thoát nhanh chóng từ một vòng lặp. Câu lệnh break có thể được sử dụng trong cả các vòng lặp while và for trong Python.

Nếu bạn đang sử dụng các vòng lặp lồng nhau trong Python, câu lệnh break sẽ dừng việc thực thi của vòng lặp nằm bên trong nhất và bắt đầu thực thi dòng lệnh tiếp theo sau khối mã.

### Cú pháp của câu lệnh break

Cú pháp cho câu lệnh break trong Python là như sau:


```python
break
```

### Ví dụ về câu lệnh break

#### Ví dụ 1: Thể hiện việc sử dụng câu lệnh break trong Python

```python
for letter in 'Python':     # Ví dụ 1
   if letter == 'h':
      break
   print ('Chữ hiện tại :', letter)
  
var = 10                    # Ví dụ 2
while var > 0:              
   print ('Giá trị biến hiện tại :', var)
   var = var -1
   if var == 5:
      break

print ("Tạm biệt!")
```

Kết quả khi chạy mã trên sẽ là:

```
Chữ hiện tại : P
Chữ hiện tại : y
Chữ hiện tại : t
Chữ hiện tại : o
Chữ hiện tại : n
Giá trị biến hiện tại : 10
Giá trị biến hiện tại : 9
Giá trị biến hiện tại : 8
Giá trị biến hiện tại : 7
Giá trị biến hiện tại : 6
Tạm biệt!
```

#### Ví dụ 2: Kiểm tra một số trong danh sách

```python
no = int(input('Nhập một số: '))
numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
   if num == no:
      print('Số được tìm thấy trong danh sách')
      break
else:
   print('Số không được tìm thấy trong danh sách')
```

Kết quả khi chạy mã trên sẽ là:

```
Nhập một số: 33
Số được tìm thấy trong danh sách
Nhập một số: 5
Số không được tìm thấy trong danh sách
```

#### Ví dụ 3: Kiểm tra số nguyên tố

```python
num = 37
print("Số: ", num)
for x in range(2, num):
   if num % x == 0:
      print("{} không phải là số nguyên tố".format(num))
      break
else:
   print("{} là số nguyên tố".format(num))
```

Kết quả khi chạy mã trên sẽ là:

```
Số: 37
37 là số nguyên tố
```

Gán các giá trị khác cho num để kiểm tra xem nó có phải là số nguyên tố hay không.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*