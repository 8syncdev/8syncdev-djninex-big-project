# Bài 2. Python - Thay Đổi Các Phần Tử trong Danh Sách

## Thay Đổi Các Phần Tử trong Danh Sách

Danh sách là một loại dữ liệu có thể thay đổi được (mutable) trong Python. Điều này có nghĩa là, nội dung của danh sách có thể được thay đổi tại chỗ, sau khi đối tượng được lưu trong bộ nhớ. Bạn có thể gán một giá trị mới tại một chỉ mục nhất định trong danh sách.

### Cú Pháp

```python
list1[i] = giá_trị_mới
```

#### Ví dụ

Trong đoạn mã sau, chúng ta thay đổi giá trị tại chỉ mục 2 của danh sách đã cho.

```python
list3 = [1, 2, 3, 4, 5]
print ("Danh sách gốc ", list3)
list3[2] = 10
print ("Danh sách sau khi thay đổi giá trị tại chỉ mục 2: ", list3)
```

Kết quả sẽ là:

```
Danh sách gốc [1, 2, 3, 4, 5]
Danh sách sau khi thay đổi giá trị tại chỉ mục 2: [1, 2, 10, 4, 5]
```

### Thay Đổi Các Phần Tử Liên Tiếp trong Danh Sách

Bạn có thể thay thế nhiều phần tử liên tiếp trong một danh sách bằng một danh sách con khác.

#### Ví dụ

Trong đoạn mã sau, các phần tử tại chỉ mục 1 và 2 được thay thế bằng các phần tử trong một danh sách con khác.

```python
list1 = ["a", "b", "c", "d"]

print ("Danh sách gốc: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2

print ("Danh sách sau khi thay đổi bằng danh sách con: ", list1)
```

Kết quả sẽ là:

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi thay đổi bằng danh sách con: ['a', 'Y', 'Z', 'd']
```

### Thay Đổi Một Dãy Các Phần Tử trong Danh Sách

Nếu danh sách con nguồn có nhiều hơn các phần tử trong phần cắt cần thay thế, các phần tử thêm vào trong nguồn sẽ được chèn vào. Xem đoạn mã dưới đây −

#### Ví dụ

```python
list1 = ["a", "b", "c", "d"]
print ("Danh sách gốc: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("Danh sách sau khi thay đổi bằng danh sách con: ", list1)
```

Kết quả sẽ là:

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi thay đổi bằng danh sách con: ['a', 'X', 'Y', 'Z', 'd']
```

#### Ví dụ

Nếu danh sách con mà một phần của danh sách gốc sẽ được thay thế, có ít hơn các phần tử, các phần tử phù hợp sẽ được thay thế và phần còn lại của danh sách gốc sẽ bị loại bỏ.

Trong đoạn mã sau, chúng ta cố gắng thay thế "b" và "c" bằng "Z" (ít hơn một phần tử so với các phần tử cần thay thế). Điều này dẫn đến Z thay thế b và c bị loại bỏ.

```python
list1 = ["a", "b", "c", "d"]
print ("Danh sách gốc: ", list1)
list2 = ['Z']
list1[1:3] = list2
print ("Danh sách sau khi thay đổi bằng danh sách con: ", list1)
```

Kết quả sẽ là:

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi thay đổi bằng danh sách con: ['a', 'Z', 'd']
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*