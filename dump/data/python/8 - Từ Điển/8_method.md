# Bài 8. Python - Các Phương Thức của Từ Điển trong Python

Trong Python, một từ điển là một đối tượng của lớp dict tích hợp, được định nghĩa các phương thức sau:

1. **`dict.clear()`**: Xóa tất cả các phần tử của từ điển `dict`.
2. **`dict.copy()`**: Trả về một bản sao nông của từ điển `dict`.
3. **`dict.fromkeys(seq, value)`**: Tạo một từ điển mới với các khóa từ `seq` và các giá trị được đặt thành `value`.
4. **`dict.get(key, default=None)`**: Đối với khóa `key`, trả về giá trị hoặc `default` nếu `key` không có trong từ điển.
5. **`dict.has_key(key)`**: Trả về `True` nếu một khóa cụ thể có sẵn trong từ điển, nếu không, trả về `False`.
6. **`dict.items()`**: Trả về một danh sách các cặp tuple (khóa, giá trị) của từ điển.
7. **`dict.keys()`**: Trả về danh sách các khóa của từ điển `dict`.
8. **`dict.pop(key)`**: Xóa phần tử với khóa được chỉ định khỏi từ điển.
9. **`dict.popitem()`**: Xóa cặp key-value được chèn cuối cùng.
10. **`dict.setdefault(key, default=None)`**: Tương tự như `get()`, nhưng sẽ đặt `dict[key]=default` nếu `key` chưa tồn tại trong `dict`.
11. **`dict.update(dict2)`**: Thêm các cặp key-value của từ điển `dict2` vào `dict`.
12. **`dict.values()`**: Trả về danh sách các giá trị của từ điển `dict`.