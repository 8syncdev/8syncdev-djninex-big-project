# Bài 4. Python - Xóa các Phần Tử trong Từ Điển Python

Trong Python, có một số cách để xóa các phần tử khỏi một từ điển (dictionary). Dưới đây là các phương pháp thường được sử dụng:

## Sử Dụng Từ Khóa `del`

Từ khóa `del` của Python được sử dụng để xóa một phần tử từ một từ điển.

**Cú pháp:**
```python
del dict['key']
```

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print("Từ điển numbers trước khi xóa: \n", numbers)
del numbers[20]
print("Từ điển numbers sau khi xóa: \n", numbers)
```

Kết quả:
```
Từ điển numbers trước khi xóa:
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
Từ điển numbers sau khi xóa:
 {10: 'Ten', 30: 'Thirty', 40: 'Forty'}
```

## Sử Dụng Phương Thức `pop()`

Phương thức `pop()` của lớp `dict` gây ra việc loại bỏ một phần tử với key đã chỉ định khỏi từ điển.

**Cú Pháp:**
```python
val = dict.pop(key)
```

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print("Từ điển numbers trước khi pop: \n", numbers)
val = numbers.pop(20)
print("Từ điển numbers sau khi pop: \n", numbers)
print("Giá trị pop: ", val)
```

Kết quả:
```
Từ điển numbers trước khi pop: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
Từ điển numbers sau khi pop: 
 {10: 'Ten', 30: 'Thirty', 40: 'Forty'}
Giá trị pop:  Twenty
```

## Sử Dụng Phương Thức `popitem()`

Phương thức `popitem()` trong lớp `dict` không nhận bất kỳ đối số nào. Nó loại bỏ cặp key-value được chèn cuối cùng và trả về nó dưới dạng một bộ giá trị.

**Cú Pháp:**
```python
val = dict.popitem()
```

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print("Từ điển numbers trước khi pop: \n", numbers)
val = numbers.popitem()
print("Từ điển numbers sau khi pop: \n", numbers)
print("Giá trị pop: ", val)
```

Kết quả:
```
Từ điển numbers trước khi pop: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
Từ điển numbers sau khi pop: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty'}
Giá trị pop:  (40, 'Forty')
```

## Sử Dụng Phương Thức `clear()`

Phương thức `clear()` trong lớp `dict` loại bỏ tất cả các phần tử từ đối tượng từ điển và trả về một đối tượng trống.

**Cú Pháp:**
```python
dict.clear()
```

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print("Từ điển numbers trước khi clear: \n", numbers)
numbers.clear()
print("Từ điển numbers sau khi clear: \n", numbers)
```

Kết quả:
```
Từ điển numbers trước khi clear: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
Từ điển numbers sau khi clear: 
 {}
```

Các phương thức và từ khóa này cho phép bạn linh hoạt trong việc xóa và quản lý các phần tử trong từ điển Python.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*