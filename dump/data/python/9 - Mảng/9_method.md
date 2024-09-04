# Bài 09. Python - Phương Thức Mảng

## Phương Thức `array.reverse()`

Giống như các loại chuỗi, lớp array cũng hỗ trợ phương thức `reverse()` để sắp xếp lại các phần tử theo thứ tự ngược lại.

### Cú pháp
```python
array.reverse()
```

### Tham số
Phương thức này không có tham số.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
a.reverse()
print(a)
```

Kết quả sẽ là:

```
array('i', [5, 4, 3, 2, 1])
```

## Phương Thức `array.count()`

Phương thức `count()` trả về số lần một phần tử cụ thể xuất hiện trong mảng.

### Cú pháp
```python
array.count(v)
```

### Tham số
- `v`: Giá trị cần đếm số lần xuất hiện.

### Giá trị trả về
Phương thức `count()` trả về một số nguyên tương ứng với số lần `v` xuất hiện trong mảng.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
c = a.count(2)
print("Số lần xuất hiện của 2:", c)
```

Kết quả sẽ là:

```
Số lần xuất hiện của 2: 3
```

## Phương Thức `array.index()`

Phương thức `index()` trong lớp array tìm vị trí xuất hiện đầu tiên của một phần tử cụ thể trong mảng.

### Cú pháp
```python
array.index(v)
```

### Tham số
- `v`: Giá trị cần tìm vị trí.

### Ví dụ
```python
a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
c = a.index(2)
print("Vị trí xuất hiện đầu tiên của 2:", c)
```

Kết quả sẽ là:

```
Vị trí xuất hiện đầu tiên của 2: 1
```

## Phương Thức `array.fromlist()`

Phương thức `fromlist()` nối các phần tử từ một danh sách Python vào đối tượng mảng.

### Cú pháp
```python
array.fromlist(l)
```

### Tham số
- `l`: Danh sách các phần tử sẽ được nối vào mảng. Tất cả các phần tử trong danh sách phải có cùng kiểu dữ liệu với mảng.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
lst = [6, 7, 8, 9, 10]
a.fromlist(lst)
print(a)
```

Kết quả sẽ là:

```
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

## Phương Thức `array.tofile()`

Phương thức `tofile()` trong lớp array ghi tất cả các phần tử (dưới dạng giá trị máy) trong mảng vào đối tượng tệp.

### Cú pháp
```python
array.tofile(f)
```

### Tham số
- `f`: Đối tượng tệp thu được từ hàm `open()`. Tệp cần mở trong chế độ `wb`.

### Ví dụ
```python
import array as arr
f = open('list.txt', 'wb')
arr.array("i", [10, 20, 30, 40, 50]).tofile(f)
f.close()
```

Sau khi chạy mã trên, một tệp có tên "list.txt" sẽ được tạo trong thư mục hiện tại.

## Phương Thức `array.fromfile()`

Phương thức `fromfile()` đọc một tệp nhị phân và nối một số lượng phần tử đã chỉ định vào đối tượng mảng.

### Cú pháp
```python
array.fromfile(f, n)
```

### Tham số
- `f`: Đối tượng tệp đang tham chiếu đến một tệp đĩa đã mở trong chế độ `rb`.
- `n`: Số lượng phần tử cần được nối vào mảng.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
f = open("list.txt", "rb")
a.fromfile(f, 5)
print(a)
```

Kết quả sẽ là:

```
array('i', [1, 2, 3, 4, 5, 10, 20, 30, 40, 50])
```