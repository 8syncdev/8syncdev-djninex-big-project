# Bài 02. Python - Thêm Phần Tử vào Mảng

## Thêm Phần Tử vào Mảng

Phương thức append() thêm một phần tử mới vào cuối mảng đã cho.

### Cú Pháp
```python
array.append(v)
```

#### Tham số
- **v**: Giá trị mới được thêm vào cuối mảng. Giá trị mới phải cùng loại dữ liệu như đối số datatype được sử dụng khi khai báo đối tượng mảng.

### Ví dụ: Thêm Phần Tử vào Mảng
```python
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)
```

Kết quả sẽ là:

```
array('i', [1, 2, 3, 10])
```

## Thêm Phần Tử vào Chỉ Mục Cụ Thể của Mảng

Lớp mảng cũng xác định phương thức insert(). Có thể chèn một phần tử mới vào chỉ mục được chỉ định.

### Cú Pháp
```python
array.insert(i, v)
```

#### Tham số
- **i**: Chỉ mục mà giá trị mới sẽ được chèn vào.
- **v**: Giá trị sẽ được chèn vào. Phải là kiểu dữ liệu của mảng.

### Ví dụ: Thêm Phần Tử vào Chỉ Mục Cụ Thể của Mảng
```python
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)
```

Kết quả sẽ là:

```
array('i', [1, 20, 2, 3])
```

## Thêm Phần Tử từ Chuỗi Khác vào Mảng

Phương thức extend() trong lớp mảng nối thêm tất cả các phần tử từ một mảng khác cùng loại mã typecode.

### Cú Pháp
```python
array.extend(x)
```

#### Tham số
- **x**: Đối tượng của lớp array.array.

### Ví dụ: Mở Rộng Mảng
```python
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)
```

Kết quả sẽ là:

```
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```