# Bài 7. Python - Sắp xếp Danh sách

## Phương thức sort() của List trong Python

Phương thức sort() của lớp list sắp xếp lại các mục theo thứ tự tăng dần hoặc giảm dần bằng cách sử dụng cơ chế sắp xếp theo thứ tự từ điển. Việc sắp xếp được thực hiện trên chính chúng trong cùng một đối tượng danh sách và nó không trả về một đối tượng mới.

### Cú pháp

```python
list1.sort(key, reverse)
```

### Tham số

- **Key**: Hàm được áp dụng cho từng mục trong danh sách. Giá trị trả về được sử dụng để thực hiện sắp xếp. Tùy chọn.
  
- **Reverse**: Giá trị boolean. Nếu được đặt thành True, sắp xếp sẽ được thực hiện theo thứ tự giảm dần. Tùy chọn.

### Giá trị trả về

Phương thức này trả về None.

### Sắp xếp các mục trong danh sách theo thứ tự chữ cái

Phương thức sort() sắp xếp các mục của danh sách theo thứ tự chữ cái.

#### Ví dụ

```python
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print("Danh sách trước khi sắp xếp:", list1)
list1.sort()
print("Danh sách sau khi sắp xếp:", list1)

print("Sắp xếp giảm dần")

list2 = [10, 16, 9, 24, 5]
print("Danh sách trước khi sắp xếp:", list2)
list2.sort()
print("Danh sách sau khi sắp xếp:", list2)
```

Đầu ra sẽ là:

```
Danh sách trước khi sắp xếp: ['physics', 'Biology', 'chemistry', 'maths']
Danh sách sau khi sắp xếp: ['Biology', 'chemistry', 'maths', 'physics']
Sắp xếp giảm dần
Danh sách trước khi sắp xếp: [10, 16, 9, 24, 5]
Danh sách sau khi sắp xếp: [5, 9, 10, 16, 24]
```

### Sắp xếp các mục trong danh sách với str.lower()

Trong ví dụ này, phương thức str.lower() được sử dụng làm tham số key trong phương thức sort().

#### Ví dụ

```python
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print("Danh sách trước khi sắp xếp:", list1)
list1.sort(key=str.lower)
print("Danh sách sau khi sắp xếp:", list1)
```

Đầu ra sẽ là:

```
Danh sách trước khi sắp xếp: ['Physics', 'biology', 'Biomechanics', 'psychology']
Danh sách sau khi sắp xếp: ['biology', 'Biomechanics', 'Physics', 'psychology']
```

### Sắp xếp các mục trong danh sách với Hàm gọi lại

Hàm do người dùng xác định cũng có thể được sử dụng làm tham số key trong phương thức sort().

#### Ví dụ

```python
def myfunction(x):
   return x % 10

list1 = [17, 23, 46, 51, 90]
print("Danh sách trước khi sắp xếp:", list1)
list1.sort(key=myfunction)
print("Danh sách sau khi sắp xếp:", list1)
```

Đầu ra sẽ là:

```
Danh sách trước khi sắp xếp: [17, 23, 46, 51, 90]
Danh sách sau khi sắp xếp: [90, 51, 23, 46, 17]
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*