# Bài 4. Python - Xóa Phần Tử trong Danh Sách

## Xóa Phần Tử trong Danh Sách

Trong Python, các phương thức của lớp list như remove() và pop() đều có thể xóa một phần tử từ danh sách. Sự khác biệt giữa chúng là remove() loại bỏ đối tượng được chỉ định, trong khi pop() loại bỏ một phần tử tại chỉ số đã cho.

### Xóa Phần Tử Được Chỉ Định

Phương thức remove() loại bỏ phần tử được chỉ định khỏi danh sách.

#### Ví dụ

```python
list1 = ["Rohan", "Physics", 21, 69.75]
print("Danh sách gốc: ", list1)

list1.remove("Physics")
print("Danh sách sau khi xóa: ", list1)
```

#### Kết Quả

```
Danh sách gốc: ['Rohan', 'Physics', 21, 69.75]
Danh sách sau khi xóa: ['Rohan', 21, 69.75]
```

### Xóa Phần Tử Được Chỉ Định Bằng Chỉ Số

Phương thức pop() loại bỏ phần tử được chỉ định khỏi danh sách dựa trên chỉ số đã cho.

#### Ví dụ

```python
list2 = [25.50, True, -55, 1+2j]
print("Danh sách gốc: ", list2)
list2.pop(2)
print("Danh sách sau khi loại bỏ: ", list2)
```

#### Kết Quả

```
Danh sách gốc: [25.5, True, -55, (1+2j)]
Danh sách sau khi loại bỏ: [25.5, True, (1+2j)]
```

### Xóa Phần Tử Được Chỉ Định Sử Dụng Từ Khóa `del`

Python có từ khóa "del" loại bỏ bất kỳ đối tượng Python nào khỏi bộ nhớ.

#### Ví dụ

Chúng ta có thể sử dụng "del" để xóa một phần tử từ danh sách. Hãy xem ví dụ sau:

```python
list1 = ["a", "b", "c", "d"]
print("Danh sách gốc: ", list1)
del list1[2]
print("Danh sách sau khi xóa: ", list1)
```

#### Kết Quả

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi xóa: ['a', 'b', 'd']
```

### Xóa Các Phần Tử Liên Tiếp

Bạn có thể xóa một loạt các phần tử liên tiếp từ một danh sách bằng toán tử slice. Hãy xem ví dụ sau:

#### Ví dụ

```python
list2 = [25.50, True, -55, 1+2j]
print("Danh sách trước khi xóa: ", list2)
del list2[0:2]
print("Danh sách sau khi xóa: ", list2)
```

#### Kết Quả

```
Danh sách trước khi xóa: [25.5, True, -55, (1+2j)]
Danh sách sau khi xóa: [-55, (1+2j)]
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*