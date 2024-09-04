# Bài 3. Python - Xóa Các Phần Tử của Tập Hợp

Trong Python, lớp `set` cung cấp các phương thức khác nhau để loại bỏ một hoặc nhiều phần tử từ một đối tượng tập hợp.

## Xóa Các Phần Tử của Tập Hợp

### Phương thức `remove()`

Phương thức `remove()` loại bỏ phần tử được chỉ định khỏi tập hợp, nếu nó tồn tại trong đó. Tuy nhiên, nếu không tồn tại, nó sẽ gây ra lỗi KeyError.

**Cú Pháp:**
```python
set.remove(obj)
```

**Tham Số:**
- `obj` − một đối tượng bất biến.

**Ví dụ:**
```python
lang1 = {"C", "C++", "Java", "Python"}
print("Tập hợp trước khi xóa: ", lang1)
lang1.remove("Java")
print("Tập hợp sau khi xóa: ", lang1)
lang1.remove("PHP")  # KeyError: 'PHP'
```

### Phương thức `discard()`

Phương thức `discard()` trong lớp set tương tự như phương thức `remove()`. Sự khác biệt duy nhất là nó không gây ra lỗi nếu đối tượng cần loại bỏ không tồn tại trong tập hợp.

**Cú Pháp:**
```python
set.discard(obj)
```

**Tham Số:**
- `obj` − Một đối tượng bất biến.

**Ví dụ:**
```python
lang1 = {"C", "C++", "Java", "Python"}
print("Tập hợp trước khi loại bỏ C++: ", lang1)
lang1.discard("C++")
print("Tập hợp sau khi loại bỏ C++: ", lang1)
print("Tập hợp trước khi loại bỏ PHP: ", lang1)
lang1.discard("PHP")
print("Tập hợp sau khi loại bỏ PHP: ", lang1)
```

### Phương thức `pop()`

Phương thức `pop()` trong lớp set loại bỏ một phần tử tùy ý khỏi tập hợp. Phần tử bị loại bỏ sẽ được trả về bởi phương thức. Loại bỏ từ một tập hợp rỗng sẽ gây ra lỗi KeyError.

**Cú Pháp:**
```python
obj = set.pop()
```

**Giá trị Trả về:**
Phương thức `pop()` trả về đối tượng được loại bỏ từ tập hợp.

**Ví dụ:**
```python
lang1 = {"C", "C++"}
print("Tập hợp trước khi loại bỏ: ", lang1)
obj = lang1.pop()
print("Đối tượng đã bị loại bỏ: ", obj)
print("Tập hợp sau khi loại bỏ: ", lang1)
obj = lang1.pop()
obj = lang1.pop()
```

### Phương thức `clear()`

Phương thức `clear()` trong lớp set loại bỏ tất cả các phần tử trong tập hợp, tạo ra một tập hợp trống.

**Cú Pháp:**
```python
set.clear()
```

**Ví dụ:**
```python
lang1 = {"C", "C++", "Java", "Python"}
print(lang1)
print("Sau khi sử dụng clear():")
lang1.clear()
print(lang1)
```

## Kết Luận

Trên đây là một số phương thức trong Python để loại bỏ các phần tử từ một tập hợp. Các phương thức này rất hữu ích trong quá trình làm việc với dữ liệu trong Python.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*