# Bài 03. Python - Xóa Phần Tử khỏi Mảng

Lớp mảng xác định hai phương thức giúp chúng ta loại bỏ một phần tử khỏi mảng. Nó có các phương thức remove() và pop().

## Xóa Sự Xuất Hiện Đầu Tiên

Phương thức remove() loại bỏ sự xuất hiện đầu tiên của một giá trị đã cho từ mảng.

### Cú Pháp
```python
array.remove(v)
```

#### Tham số
- **v**: Giá trị cần loại bỏ khỏi mảng.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 1, 4, 2])
a.remove(2)
print (a)
```

Kết quả sẽ là:

```
array('i', [1, 1, 4, 2])
```

## Xóa Phần Tử từ Chỉ Mục Cụ Thể

Phương thức pop() loại bỏ một phần tử tại chỉ mục được chỉ định từ mảng và trả về phần tử đã loại bỏ.

### Cú Pháp
```python
array.pop(i)
```

#### Tham số
- **i**: Chỉ mục của phần tử cần loại bỏ. Phương thức trả về phần tử tại vị trí i sau khi loại bỏ.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 1, 4, 2])
a.pop(2)
print (a)
```

Kết quả sẽ là:

```
array('i', [1, 2, 4, 2])
```