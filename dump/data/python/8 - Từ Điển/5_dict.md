# Bài 5. Python - Đối Tượng Xem Từ Điển trong Python

Trong Python, các phương thức items(), keys() và values() của lớp dict trả về các đối tượng xem (view objects). Các xem này được cập nhật động mỗi khi có bất kỳ thay đổi nào trong nội dung của đối tượng từ điển gốc của chúng.

## Phương Thức items()

Phương thức items() trả về một đối tượng dict_items xem. Nó chứa một danh sách các bộ, mỗi bộ được tạo thành từ các cặp key, value tương ứng.

**Cú Pháp:**
```python
obj = dict.items()
```

**Giá Trị Trả Về:**
Phương thức items() trả về đối tượng dict_items, đó là một xem động của các bộ (key, value).

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
obj = numbers.items()
print('Kiểu của obj: ', type(obj))
print(obj)
print("Cập nhật từ điển numbers")
numbers.update({50: "Fifty"})
print("Xem được cập nhật tự động")
print(obj)
```

Kết quả:
```
Kiểu của obj:  <class 'dict_items'>
dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty')])
Cập nhật từ điển numbers
Xem được cập nhật tự động
dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty'), (50, 'Fifty')])
```

## Phương Thức keys()

Phương thức keys() của lớp dict trả về đối tượng dict_keys, đó là một danh sách của tất cả các key được xác định trong từ điển. Đây là một đối tượng xem, vì nó được cập nhật tự động mỗi khi có bất kỳ hành động cập nhật nào được thực hiện trên đối tượng từ điển.

**Cú Pháp:**
```python
obj = dict.keys()
```

**Giá Trị Trả Về:**
Phương thức keys() trả về đối tượng dict_keys, đó là một xem của các keys trong từ điển.

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
obj = numbers.keys()
print('Kiểu của obj: ', type(obj))
print(obj)
print("Cập nhật từ điển numbers")
numbers.update({50: "Fifty"})
print("Xem được cập nhật tự động")
print(obj)
```

Kết quả:
```
Kiểu của obj:  <class 'dict_keys'>
dict_keys([10, 20, 30, 40])
Cập nhật từ điển numbers
Xem được cập nhật tự động
dict_keys([10, 20, 30, 40, 50])
```

## Phương Thức values()

Phương thức values() trả về một xem của tất cả các giá trị có trong từ điển. Đối tượng là kiểu dict_values, được cập nhật tự động.

**Cú Pháp:**
```python
obj = dict.values()
```

**Giá Trị Trả Về:**
Phương thức values() trả về một xem dict_values của tất cả các giá trị có trong từ điển.

**Ví dụ:**
```python
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
obj = numbers.values()
print('Kiểu của obj: ', type(obj))
print(obj)
print("Cập nhật từ điển numbers")
numbers.update({50: "Fifty"})
print("Xem được cập nhật tự động")
print(obj)
```

Kết quả:
```
Kiểu của obj:  <class 'dict_values'>
dict_values(['Ten', 'Twenty', 'Thirty', 'Forty'])
Cập nhật từ điển numbers
Xem được cập nhật tự động
dict_values(['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty'])
```

Các phương thức items(), keys() và values() cho phép bạn truy cập vào dữ liệu trong từ điển một cách linh hoạt và tiện lợi, đồng thời tự động cập nhật các xem của chúng khi có sự thay đổi trong từ điển gốc.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*