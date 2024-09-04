# Bài 07. Python - Sắp Xếp Mảng

Module mảng của Python định nghĩa lớp mảng. Một đối tượng của lớp mảng tương tự như mảng trong Java hoặc C/C++. Khác với các chuỗi Python tích hợp sẵn, mảng là một tập hợp đồng nhất của chuỗi, số nguyên hoặc đối tượng float.

Lớp mảng không có bất kỳ hàm/phương thức nào để cung cấp một sắp xếp của các phần tử của nó. Tuy nhiên, chúng ta có thể đạt được điều này với một trong những phương pháp sau:

1. Sử dụng một thuật toán sắp xếp
2. Sử dụng phương thức sort() từ List
3. Sử dụng hàm sorted() tích hợp sẵn

Hãy thảo luận về mỗi phương pháp này một cách chi tiết.

## Sắp Xếp Mảng Sử Dụng Một Thuật Toán Sắp Xếp

Chúng ta sẽ thực hiện thuật toán sắp xếp bubble để có được mảng đã sắp xếp. Để làm điều này, chúng ta sử dụng hai vòng lặp lồng nhau và hoán đổi các phần tử để sắp xếp lại theo thứ tự.

### Ví dụ
Lưu mã sau bằng một trình soạn mã Python:

```python
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)
```

Nó sẽ tạo ra kết quả sau:

```python
array('i', [4, 5, 6, 9, 10, 15, 20])
```

## Sắp Xếp Mảng Sử Dụng Phương Thức sort() của List

Ngay cả khi mảng không có phương thức sort(), lớp List tích hợp sẵn của Python vẫn có một phương thức sort. Chúng ta sẽ sử dụng nó trong ví dụ tiếp theo.

Đầu tiên, khai báo một mảng và lấy một đối tượng danh sách từ đó, sử dụng phương thức tolist():

### Ví dụ
```python
a = arr.array('i', [10,5,15,4,6,20,9])
b=a.tolist()
```

Chúng ta có thể dễ dàng có được danh sách đã sắp xếp như sau:

```python
b.sort()
```

Tất cả những gì chúng ta cần làm là chuyển danh sách này trở lại thành một đối tượng mảng:

```python
a.fromlist(b)
```

Dưới đây là mã hoàn chỉnh:

```python
from array import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b=a.tolist()
b.sort()
a = arr.array('i')
a.fromlist(b)
print (a)
```

Nó sẽ tạo ra kết quả sau:

```python
array('i', [4, 5, 6, 9, 10, 15, 20])
```

## Sắp Xếp Mảng Sử Dụng Phương Thức sorted()

Phương pháp thứ ba để sắp xếp một mảng là sử dụng hàm sorted(), một hàm tích hợp sẵn.

Cú pháp của hàm sorted() như sau:

```python
sorted(iterable, reverse=False)
```

Hàm trả về một danh sách mới chứa tất cả các mục từ iterable theo thứ tự tăng dần. Đặt tham số reverse thành True để có thứ tự giảm dần của các mục.

Hàm sorted() có thể được sử dụng cùng với bất kỳ iterable nào. Mảng Python là một iterable vì nó là một tập hợp được chỉ mục. Do đó

, một mảng có thể được sử dụng làm tham số cho hàm sorted().

### Ví dụ
```python
from array import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print (a)
```

Nó sẽ tạo ra kết quả sau:

```python
array('i', [4, 5, 6, 9, 10, 15, 20])
```