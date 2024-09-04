# Bài 1. Python - Truy Cập Các Phần Tử trong Danh Sách

## Truy Cập Các Phần Tử trong Danh Sách

Trong Python, một danh sách là một chuỗi. Mỗi đối tượng trong danh sách có thể truy cập bằng chỉ mục của nó. Chỉ mục bắt đầu từ 0. Chỉ mục cuối cùng trong danh sách là "length-1". Để truy cập các giá trị trong một danh sách, sử dụng dấu ngoặc vuông để cắt cùng với chỉ mục hoặc các chỉ mục để nhận giá trị có sẵn tại chỉ mục đó.

### Truy Cập Các Phần Tử trong Danh Sách Bằng Toán Tử Cắt

Toán tử cắt lấy một hoặc nhiều phần tử từ danh sách. Đặt chỉ mục vào dấu ngoặc vuông để lấy mục tại vị trí của nó.

```python
obj = list1[i]
```

#### Ví dụ

Xem ví dụ sau:

```python
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Phần tử ở chỉ mục 0 trong list1: ", list1[0])
print ("Phần tử ở chỉ mục 2 trong list2: ", list2[2])
```

Kết quả sẽ là:

```
Phần tử ở chỉ mục 0 trong list1: Rohan
Phần tử ở chỉ mục 2 trong list2: 3
```

### Truy Cập Các Phần Tử trong Danh Sách Bằng Chỉ Mục Âm

Python cho phép sử dụng chỉ mục âm với bất kỳ kiểu chuỗi nào. Chỉ mục "-1" tham chiếu đến phần tử cuối cùng trong danh sách.

#### Ví dụ

Hãy xem ví dụ khác:

```python
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Phần tử ở chỉ mục 0 trong list1: ", list1[-1])
print ("Phần tử ở chỉ mục 2 trong list2: ", list2[-3])
```

Kết quả sẽ là:

```
Phần tử ở chỉ mục 0 trong list1: d
Phần tử ở chỉ mục 2 trong list2: True
```

### Truy Cập Danh Sách Con từ Một Danh Sách

Toán tử cắt trích xuất một danh sách con từ danh sách ban đầu.

```
Sublist = list1[i:j]
```

#### Tham số

- i: chỉ mục của phần tử đầu tiên trong danh sách con.
- j: chỉ mục của phần tử tiếp theo sau phần tử cuối cùng trong danh sách con.

Điều này sẽ trả về một phần từ i đến (j-1) trong danh sách.

#### Ví dụ

Khi cắt, cả hai toán hạng "i" và "j" đều là tùy chọn. Nếu không sử dụng, "i" là 0 và "j" là phần tử cuối cùng trong danh sách. Chỉ mục âm có thể được sử dụng trong cắt. Hãy xem ví dụ sau:

```python
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Các phần tử từ chỉ mục 1 đến 2 trong list1: ", list1[1:3])
print ("Các phần tử từ chỉ mục 0 đến 1 trong list2: ", list2[0:2])
```

Kết quả sẽ là:

```
Các phần tử từ chỉ mục 1 đến 2 trong list1: ['b', 'c']
Các phần tử từ chỉ mục 0 đến 1 trong list2: [25.5, True]
```

#### Ví dụ

```python
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list4 = ["Rohan", "Physics", 21, 69.75]
list3 = [1, 2, 3, 4, 5]

print ("Các phần tử từ chỉ mục 1 đến cuối trong list1: ", list1[1:])
print ("Các phần tử từ chỉ mục 0 đến 1 trong list2: ", list2[:2])
print ("Các phần tử từ chỉ mục 2 đến cuối trong list3", list3[2:-1])
print ("Các phần tử từ chỉ mục 0 đến chỉ mục cuối cùng trong list4", list4[:])
```

Kết quả sẽ là:

```
Các phần tử từ chỉ mục 1 đến cuối trong list1: ['b', 'c', 'd']
Các phần tử từ chỉ mục 0 đến 1 trong list2: [25.5, True]
Các phần tử từ chỉ mục 2 đến cuối trong list3 [3, 4]
Các phần tử từ chỉ mục 0 đến chỉ mục cuối cùng trong list4 ['Rohan', 'Physics', 21, 69.75]
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*