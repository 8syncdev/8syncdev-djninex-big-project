# Hướng Dẫn Đảo Ngược Mảng trong Python

## Mục Lục
1. Giới Thiệu
2. Các Phương Pháp Đảo Ngược Mảng
   - Sử Dụng Phép Cắt (Slicing)
   - Sử Dụng Phương Thức `reverse()`
   - Sử Dụng Phương Thức `reversed()`
   - Sử Dụng Vòng Lặp `for`

## 1. Giới Thiệu
Đảo ngược mảng là việc sắp xếp lại các phần tử của mảng theo thứ tự ngược lại. Mặc dù Python không có kiểu dữ liệu mảng tích hợp sẵn, nhưng thư viện chuẩn của Python có mô-đun `array` giúp tạo ra các tập hợp đồng nhất của kiểu chuỗi, số nguyên hoặc số thực.

## 2. Các Phương Pháp Đảo Ngược Mảng

### Sử Dụng Phép Cắt (Slicing)
Phép cắt là quá trình trích xuất một phần của mảng trong các chỉ số xác định. Sử dụng phép cắt `[::1]` để đảo ngược mảng.

#### Ví Dụ
```python
import array as arr

# Tạo mảng
numericArray = arr.array('i', [88, 99, 77, 55, 66])

print("Mảng ban đầu:", numericArray)
revArray = numericArray[::-1]
print("Mảng sau khi đảo ngược:", revArray)
```
**Kết quả:**
```
Mảng ban đầu: array('i', [88, 99, 77, 55, 66])
Mảng sau khi đảo ngược: array('i', [66, 55, 77, 99, 88])
```

### Sử Dụng Phương Thức `reverse()`
Phương thức `reverse()` là một phương thức của lớp `list`. Do đó, chúng ta phải chuyển đổi mảng thành danh sách, sau đó gọi phương thức `reverse()`, và cuối cùng chuyển đổi lại thành mảng.

#### Ví Dụ
```python
import array as arr

# Tạo mảng
numericArray = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
print("Mảng trước khi đảo ngược:", numericArray)

# Chuyển đổi mảng thành danh sách
newArray = numericArray.tolist()

# Đảo ngược danh sách
newArray.reverse()

# Tạo mảng mới từ danh sách đã đảo ngược
revArray = arr.array('i', newArray)
print("Mảng sau khi đảo ngược:", revArray)
```
**Kết quả:**
```
Mảng trước khi đảo ngược: array('i', [10, 5, 15, 4, 6, 20, 9])
Mảng sau khi đảo ngược: array('i', [9, 20, 6, 4, 15, 5, 10])
```

### Sử Dụng Phương Thức `reversed()`
Phương thức `reversed()` trả về một đối tượng lặp lại các phần tử của mảng theo thứ tự ngược lại.

#### Ví Dụ
```python
import array as arr

# Tạo mảng
numericArray = arr.array('i', [12, 10, 14, 16, 20, 18])
print("Mảng trước khi đảo ngược:", numericArray)

# Đảo ngược mảng
newArray = list(reversed(numericArray))

# Tạo mảng mới từ danh sách đã đảo ngược
revArray = arr.array('i', newArray)
print("Mảng sau khi đảo ngược:", revArray)
```
**Kết quả:**
```
Mảng trước khi đảo ngược: array('i', [12, 10, 14, 16, 20, 18])
Mảng sau khi đảo ngược: array('i', [18, 20, 16, 14, 10, 12])
```

### Sử Dụng Vòng Lặp `for`
Sử dụng vòng lặp `for` để duyệt qua các phần tử của mảng theo thứ tự ngược lại và thêm từng phần tử vào một mảng mới.

#### Ví Dụ
```python
import array as arr

a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
b = arr.array('i')

for i in range(len(a) - 1, -1, -1):
    b.append(a[i])

print("Mảng ban đầu:", a)
print("Mảng sau khi đảo ngược:", b)
```
**Kết quả:**
```
Mảng ban đầu: array('i', [10, 5, 15, 4, 6, 20, 9])
Mảng sau khi đảo ngược: array('i', [9, 20, 6, 4, 15, 5, 10])
```

