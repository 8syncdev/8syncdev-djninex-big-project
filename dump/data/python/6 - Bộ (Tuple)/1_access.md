# Bài 1. Python - Truy cập các mục Tuple

Trong Python, Tuple là một chuỗi. Mỗi đối tượng trong tuple có thể được truy cập bằng chỉ mục của nó. Chỉ mục bắt đầu từ "0". Chỉ mục của phần tử cuối cùng trong tuple là "length-1". Để truy cập giá trị trong các tuple, sử dụng dấu ngoặc vuông để cắt cùng với chỉ mục hoặc các chỉ mục để nhận giá trị có sẵn tại chỉ mục đó.

Toán tử lát cắt rút ra một hoặc nhiều mục từ tuple.

```python
obj = tup1[i]
```

Ví dụ:

```python
tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)

print ("Item tại chỉ mục 0 trong tup1: ", tup1[0])
print ("Item tại chỉ mục 2 trong tup2: ", tup2[2])
```

Sẽ cho ra kết quả sau:

```
Item tại chỉ mục 0 trong tup1: Rohan
Item tại chỉ mục 2 trong tup2: 3
```

Truy cập các mục Tuple với Chỉ mục Âm
Python cho phép sử dụng chỉ mục âm với bất kỳ kiểu dữ liệu chuỗi nào. Chỉ mục "-1" đề cập đến mục cuối cùng trong tuple.

Ví dụ:

```python
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
print ("Item tại chỉ mục 0 trong tup1: ", tup1[-1])
print ("Item tại chỉ mục 2 trong tup2: ", tup2[-3])
```

Sẽ cho ra kết quả sau:

```
Item tại chỉ mục 0 trong tup1: d
Item tại chỉ mục 2 trong tup2: True
```

Trích xuất một Tuple con từ một Tuple
Toán tử lát cắt rút ra một tuple con từ tuple gốc.

```python
Subtup = tup1[i:j]
```

Tham số:

- i − chỉ mục của mục đầu tiên trong subtup.
- j − chỉ mục của mục tiếp theo sau mục cuối cùng trong subtup.

Điều này sẽ trả về một lát cắt từ mục thứ i đến (j-1) từ tup1.

Ví dụ:

```python
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)

print ("Các mục từ chỉ mục 1 đến 2 trong tup1: ", tup1[1:3])
print ("Các mục từ chỉ mục 0 đến 1 trong tup2: ", tup2[0:2])
```

Sẽ cho ra kết quả sau:

```
Các mục từ chỉ mục 1 đến 2 trong tup1: ('b', 'c')
Các mục từ chỉ mục 0 đến 1 trong tup2: (25.5, True)
```

Truy cập phạm vi các mục Tuple với Chỉ mục Âm
Khi lát cắt, cả hai toán hạng "i" và "j" đều là tùy chọn. Nếu không được sử dụng, "i" là 0 và "j" là mục cuối cùng trong tuple. Chỉ mục âm có thể được sử dụng trong lát cắt. Xem ví dụ sau:

```python
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)
tup4 = ("Rohan", "Physics", 21, 69.75)
tup3 = (1, 2, 3, 4, 5)

print ("Các mục từ chỉ mục 1 đến cuối cùng trong tup1: ", tup1[1:])
print ("Các mục từ chỉ mục 0 đến 1 trong tup2: ", tup2[:2])
print ("Các mục từ chỉ mục 2 đến cuối cùng trong tup3", tup3[2:-1])
print ("Các mục từ chỉ mục 0 đến chỉ mục cuối cùng trong tup4", tup4[:])
```

Sẽ cho ra kết quả sau:

```
Các mục từ chỉ mục 1 đến cuối cùng trong tup1: ('b', 'c', 'd')
Các mục từ chỉ mục 0 đến 1 trong tup2: (25.5, True)
Các mục từ chỉ mục 2 đến cuối cùng trong tup3: (3, 4)
Các mục từ chỉ mục 0 đến chỉ mục cuối cùng trong tup4: ('Rohan', 'Physics', 21, 69.75)
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*