# Bài 08. Python - Gộp Mảng

Trong Python, mảng là một tập hợp đồng nhất của các loại dữ liệu được tích hợp sẵn của Python như chuỗi, số nguyên hoặc đối tượng float. Tuy nhiên, mảng chính nó không phải là một loại dữ liệu tích hợp sẵn, thay vào đó, chúng ta cần sử dụng lớp mảng trong module mảng tích hợp sẵn của Python.

## Gộp Mảng bằng Cách Thêm Các Phần Tử
Để gộp hai mảng, chúng ta có thể làm điều đó bằng cách thêm mỗi mục từ một mảng vào mảng khác.

Dưới đây là hai mảng Python:

```python
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
```

Chạy một vòng lặp for trên mảng "b". Lấy mỗi số từ "b" và thêm nó vào mảng "a" với câu lệnh vòng lặp sau:

```python
for i in range(len(b)):
   a.append(b[i])
```

Mảng "a" bây giờ chứa các phần tử từ "a" cũng như "b".

### Ví dụ: Gộp Hai Mảng bằng Cách Thêm Các Phần Tử
Dưới đây là mã hoàn chỉnh.

```python
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
for i in range(len(b)):
   a.append(b[i])
print (a, b)
```

Nó sẽ tạo ra kết quả sau:

```
array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])
```

## Gộp Mảng bằng Cách Chuyển Đổi thành Đối Tượng Danh Sách
Sử dụng một phương pháp khác để gộp hai mảng, đầu tiên chuyển đổi các mảng thành các đối tượng danh sách.

```python
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x=a.tolist()
y=b.tolist()
```

Các đối tượng danh sách có thể được nối với toán tử '+'.

```python
z=x+y
```

Nếu danh sách "z" được chuyển đổi lại thành một mảng, bạn sẽ có một mảng đại diện cho các mảng đã gộp.

```python
a.fromlist(z)
```

### Ví dụ: Gộp Hai Mảng bằng Cách Chuyển Đổi thành Đối Tượng Danh Sách
Dưới đây là mã hoàn chỉnh.

```python
from array import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x=a.tolist()
y=b.tolist()
z=x+y
a=arr.array('i')
a.fromlist(z)
print (a)
```

## Gộp Mảng Bằng Cách Sử Dụng Phương Thức extend()
Chúng ta cũng có thể sử dụng phương thức extend() từ lớp List để thêm các phần tử từ một danh sách vào một danh sách khác.

Đầu tiên, chuyển đổi mảng thành một danh sách và sau đó gọi phương thức extend() để hợp nhất hai danh sách.

### Ví dụ: Gộp Hai Mảng Bằng Cách Sử Dụng Phương Thức extend()
```python
from array import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
a.extend(b)
print (a)
```

Nó sẽ tạo ra kết quả sau:

```
array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])
```