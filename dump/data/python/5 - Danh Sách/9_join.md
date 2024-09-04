# Bài 9. Python - Kết hợp Danh sách

Trong Python, List được phân loại là một đối tượng loại chuỗi. Đó là một tập hợp các mục, có thể thuộc các loại dữ liệu khác nhau, với mỗi mục có một chỉ số vị trí bắt đầu từ 0. Bạn có thể sử dụng các cách khác nhau để kết hợp hai danh sách Python.

Tất cả các đối tượng loại chuỗi đều hỗ trợ toán tử nối (+), với đó hai danh sách có thể được kết hợp.

### Ví dụ

```python
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L3 = L1 + L2
print("Danh sách kết hợp:", L3)
```

Kết quả sẽ là:

```
Danh sách kết hợp: [10, 20, 30, 40, 'one', 'two', 'three', 'four']
```

Kết hợp Danh sách Python Bằng Cách Sử Dụng Toán Tử Nối Tăng Cường

Bạn cũng có thể sử dụng toán tử nối tăng cường với ký hiệu "+=" để thêm L2 vào L1

### Ví dụ

```python
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1 += L2
print("Danh sách kết hợp:", L1)
```

Kết quả sẽ là:

```
Danh sách kết hợp: [10, 20, 30, 40, 'one', 'two', 'three', 'four']
```

Kết quả tương tự có thể được thu được bằng cách sử dụng phương thức extend(). Ở đây, chúng ta cần mở rộng L1 để thêm các phần tử từ L2 vào đó.

```python
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print("Danh sách kết hợp:", L1)
```

Kết quả sẽ là:

```
Danh sách kết hợp: [10, 20, 30, 40, 'one', 'two', 'three', 'four']
```

Kết hợp Danh sách Python bằng cách Thêm Mục

Để thêm các mục từ một danh sách vào một danh sách khác, một giải pháp lặp cổ điển cũng hoạt động. Duyệt qua các mục của danh sách thứ hai với một vòng lặp for, và thêm từng mục vào đầu tiên.

### Ví dụ

```python
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']

for x in L2:
   L1.append(x)
   
print("Danh sách kết hợp:", L1)
```

Kết quả sẽ là:

```
Danh sách kết hợp: [10, 20, 30, 40, 'one', 'two', 'three', 'four']
```

Kết hợp Danh sách Python bằng Cách Sử Dụng Comprehension Danh sách

Một phương pháp phức tạp hơn để kết hợp hai danh sách là sử dụng comprehension danh sách, như đoạn mã sau:

### Ví dụ

```python
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L3 = [y for x in [L1, L2] for y in x]
print("Danh sách kết hợp:", L3)
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*