# Bài 01. Python - Truy Cập Phần Tử của Mảng

Vì đối tượng mảng hoạt động rất giống như một chuỗi, bạn có thể thực hiện các thao tác chỉ mục và cắt mảnh với nó.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3])
# chỉ mục
print (a[1])
# cắt mảnh
print (a[1:])
```

## Thay Đổi Phần Tử của Mảng

Bạn có thể gán giá trị cho một phần tử trong mảng giống như bạn gán giá trị cho một phần tử trong một danh sách.

### Ví dụ
```python
import array as arr
a = arr.array('i', [1, 2, 3])
a[1] = 20
print (a[1])
```

Ở đây, bạn sẽ nhận được "20" là kết quả đầu ra. Tuy nhiên, Python không cho phép gán giá trị của bất kỳ loại nào khác ngoài loại được sử dụng khi tạo một mảng. Phép gán sau đây sẽ gây ra TypeError.

```python
import array as arr
a = arr.array('i', [1, 2, 3])
# gán giá trị
a[1] = 'A'
```

Nó sẽ tạo ra kết quả sau:

```
TypeError: 'str' object cannot be interpreted as an integer
```