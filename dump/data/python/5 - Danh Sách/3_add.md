# Bài 3. Python - Thêm Phần Tử vào Danh Sách

## Thêm Phần Tử vào Danh Sách

Trong Python, có hai phương thức cơ bản để thêm phần tử vào danh sách hiện có: `append()` và `insert()`.

### Phương Thức `append()`

Phương thức `append()` được sử dụng để thêm một phần tử vào cuối của danh sách.

#### Ví dụ

```python
list1 = ["a", "b", "c", "d"]
print("Danh sách gốc: ", list1)
list1.append('e')
print("Danh sách sau khi thêm: ", list1)
```

#### Kết Quả

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi thêm: ['a', 'b', 'c', 'd', 'e']
```

### Phương Thức `insert()`

Phương thức `insert()` chèn một phần tử vào danh sách tại một vị trí cụ thể được chỉ định.

#### Ví dụ

```python
list1 = ["a", "b", "c", "d"]
print("Danh sách gốc: ", list1)
list1.insert(2, 'e')
print("Danh sách sau khi chèn: ", list1)
```

#### Kết Quả

```
Danh sách gốc: ['a', 'b', 'c', 'd']
Danh sách sau khi chèn: ['a', 'b', 'e', 'c', 'd']
```

Trong ví dụ này, chúng ta chèn phần tử 'e' vào danh sách `list1` tại vị trí có chỉ số là 2, và phần tử 'c' được dịch sang phải.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*