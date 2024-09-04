# Bài 00. Python - Mảng

Mảng là một cấu trúc dữ liệu có thể chứa một số lượng cố định các phần tử và các phần tử này phải cùng loại dữ liệu. Hầu hết các cấu trúc dữ liệu sử dụng mảng để triển khai các thuật toán của chúng. Dưới đây là các thuật ngữ quan trọng để hiểu về khái niệm của Mảng.

## 1. Phần Tử (Element)
Mỗi phần tử được lưu trữ trong một mảng được gọi là một phần tử.

## 2. Chỉ Số (Index)
Mỗi vị trí của một phần tử trong một mảng có một chỉ số số học, được sử dụng để xác định phần tử.

## 3. Biểu Diễn Mảng
Mảng có thể được khai báo theo nhiều cách khác nhau trong các ngôn ngữ khác nhau. Dưới đây là một minh họa.

![](../../../assets/array/array_declaration.jpg)

### Khai Báo Mảng
Dựa trên minh họa trên, sau đây là những điểm quan trọng cần xem xét.

- Chỉ số bắt đầu từ 0.
- Độ dài của mảng là 10, có nghĩa là nó có thể lưu trữ 10 phần tử.
- Mỗi phần tử có thể được truy cập qua chỉ số của nó. Ví dụ, chúng ta có thể truy cập vào phần tử tại chỉ số 6 như 9.

## 4. Các Thao Tác Cơ Bản
Dưới đây là các thao tác cơ bản được hỗ trợ bởi một mảng.

- **Duyệt (Traverse)**: In ra tất cả các phần tử của mảng một cách tuần tự.
- **Chèn (Insertion)**: Thêm một phần tử tại chỉ số đã cho.
- **Xóa (Deletion)**: Xóa một phần tử tại chỉ số đã cho.
- **Tìm Kiếm (Search)**: Tìm kiếm một phần tử sử dụng chỉ số đã cho hoặc giá trị của phần tử.
- **Cập Nhật (Update)**: Cập nhật một phần tử tại chỉ số đã cho.

## 5. Mảng trong Python
Các kiểu dữ liệu tiêu chuẩn của Python như list, tuple và string là các chuỗi. Một đối tượng chuỗi là một tập hợp có thứ tự các mục. Mỗi mục được đặc trưng bằng chỉ số tăng dần bắt đầu từ số 0. Hơn nữa, các mục trong một chuỗi không nhất thiết phải cùng loại dữ liệu. Nói cách khác, một danh sách hoặc tuple có thể bao gồm các mục của các loại dữ liệu khác nhau.

Điều này khác biệt với khái niệm của một mảng trong C hoặc C++. Trong C/C++, một mảng cũng là một tập hợp có chỉ số của các mục, nhưng các mục phải cùng loại dữ liệu. Trong C/C++, bạn có một mảng các số nguyên hoặc số thực, hoặc chuỗi, nhưng bạn không thể có một mảng với một số phần tử thuộc loại số nguyên và một số thuộc loại khác. Một mảng trong C/C++ do đó là một tập hợp đồng nhất của các loại dữ liệu.

Thư viện tiêu chuẩn của Python có một mô-đun mảng. Lớp mảng trong đó cho phép bạn xây dựng một mảng của ba loại cơ bản, số nguyên, số thực và ký tự Unicode.

### Cú Pháp
Cú pháp tạo mảng là:

```python
import array
obj = array.array(typecode[, initializer])
```

#### Tham số
- **typecode**: Ký tự typecode được sử dụng để tạo mảng.
- **initializer**: mảng được khởi tạo từ giá trị tùy chọn, phải là một danh sách, một đối tượng giống như bytes hoặc có thể lặp lại qua các phần tử của loại thích hợp.

#### Kiểu Trả Về
Constructor array() trả về một đối tượng của lớp array.array.

### Ví dụ
```python
import array as arr

# Tạo một mảng với kiểu số nguyên
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# Tạo một mảng với kiểu ký tự
a = arr.array('u', 'BAT')
print (type(a), a)

# Tạo một mảng với kiểu số thực
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)
```

Kết quả sẽ là:
```python
<class 'array.array'> array('i', [1, 2, 3])
<class 'array.array'> array('u', 'BAT')
<class 'array.array'> array('d', [1.1, 2.2, 3.3])
```

Mảng là các kiểu chuỗi và hoạt động rất giống như danh sách, trừ việc kiểu đối tượng được lưu trữ trong chúng được hạn chế.

Loại mảng Python được quyết định bởi một ký tự Typecode duy nhất. Các mã loại và kiểu dữ liệu Python dự định của mảng được liệt kê dưới đây:

| typecode | Kiểu dữ liệu Python | Kích thước byte |
|----------|---------------------|------------------|
| 'b'      | số nguyên có dấu   | 1                |
| 'B'      | số nguyên không dấu| 1                |
| 'u'      | ký tự Unicode       | 2                |
| 'h'      | số nguyên có dấu   | 2                |
| 'H'      | số nguyên không dấu| 2                |
| 'i'      | số nguyên có dấu   | 2                |
| 'I'      | số nguyên không dấu| 2                |
| 'l'      | số nguyên có dấu   | 4                |
| 'L'      | số nguyên không dấu| 4                |
| 'q'      | số nguyên có dấu   | 8                |
| 'Q'      | số nguyên không dấu| 8                |
| 'f'      | số thực động        | 4                |
| 'd'      | số thực động        | 8                |

Trước khi xem xét các thao tác mảng khác nhau, hãy tạo và in một mảng bằng Python. Mã dưới đây tạo một mảng có tên là array1.

```python
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
 print(x)
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau:

```python
10
20
30
40
50
```

## Truy Cập Phần Tử Mảng
Chúng ta có thể truy cập từng phần tử của một mảng bằng cách sử dụng chỉ số của phần tử đó. Mã dưới đây cho thấy cách

```python
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau, cho thấy phần tử được chèn vào vị trí chỉ số 1.

```python
10
30
```

## Thao Tác Chèn (Insertion)
Thao tác chèn là để chèn một hoặc nhiều phần tử dữ liệu vào một mảng. Dựa trên yêu cầu, một phần tử mới có thể được thêm vào đầu, cuối hoặc bất kỳ chỉ số đã cho nào của mảng.

Ở đây, chúng tôi thêm một phần tử dữ liệu vào giữa mảng bằng phương thức insert() tích hợp của Python.

```python
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
 print(x)
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau, cho thấy phần tử được chèn vào vị trí chỉ số 1.

```python
10
60
20
30
40
50
```

## Thao Tác Xóa (Deletion)
Xóa đề cập đến việc loại bỏ một phần tử hiện có khỏi mảng và tổ chức lại tất cả các phần tử của mảng.

Ở đây, chúng tôi loại bỏ một phần tử dữ liệu ở giữa mảng bằng phương thức remove() tích hợp của Python.

```python
from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
   print(x)
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau, cho thấy phần tử được loại bỏ từ mảng.

```python
10
20
30
50
```

## Thao Tác Tìm Kiếm (Search)
Bạn có thể thực hiện tìm kiếm một phần tử mảng dựa trên giá trị hoặc chỉ số của nó. Ở đây, chúng ta tìm kiếm một phần tử dữ liệu bằng cách sử dụng phương thức index() tích hợp của Python.

```python
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau, cho thấy chỉ số của phần tử. Nếu giá trị không có trong mảng thì chương trình sẽ trả về một lỗi.

```python
3
```

## Thao Tác Cập Nhật (Update)
Thao tác cập nhật đề cập đến việc cập nhật một phần tử hiện có từ mảng tại một chỉ số đã cho. Ở đây, chúng ta chỉ đơn giản là gán một giá trị mới cho chỉ số mong muốn mà chúng ta muốn cập nhật.

```python
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)
```

### Kết Quả
Khi chúng ta biên dịch và thực thi chương trình trên, nó sẽ tạo ra kết quả sau, cho thấy giá trị mới tại chỉ số 2.

```python
10
20
80
40
50
```