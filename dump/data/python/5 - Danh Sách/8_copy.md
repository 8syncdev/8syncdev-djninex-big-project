# Bài 8. Python - Sao chép Danh sách

Trong Python, một biến chỉ là một nhãn hoặc tham chiếu đến đối tượng trong bộ nhớ. Do đó, phép gán "lst1 = lst" đề cập đến cùng một đối tượng danh sách trong bộ nhớ. Hãy xem ví dụ sau:

```python
lst = [10, 20]
print("lst:", lst, "id(lst):", id(lst))
lst1 = lst
print("lst1:", lst1, "id(lst1):", id(lst1))
```

Kết quả sẽ là:

```
lst: [10, 20] id(lst): 1677677188288
lst1: [10, 20] id(lst1): 1677677188288
```

Do đó, nếu chúng ta cập nhật "lst", nó sẽ tự động phản ánh trong "lst1". Thay đổi lst[0] thành 100

```python
lst[0] = 100
print("lst:", lst, "id(lst):", id(lst))
print("lst1:", lst1, "id(lst1):", id(lst1))
```

Kết quả sẽ là:

```
lst: [100, 20] id(lst): 1677677188288
lst1: [100, 20] id(lst1): 1677677188288
```

Do đó, chúng ta có thể nói rằng "lst1" không phải là bản sao vật lý của "lst".

## Sao chép một Danh sách Python

Lớp list của Python có một phương thức copy() để tạo một bản sao vật lý mới của một đối tượng danh sách.

### Cú pháp

```python
lst1 = lst.copy()
```

Đối tượng danh sách mới sẽ có một giá trị id() khác nhau.

### Ví dụ về Sao chép Danh sách trong Python

#### Ví dụ 1

```python
lst = [10, 20]
lst1 = lst.copy()
print("lst:", lst, "id(lst):", id(lst))
print("lst1:", lst1, "id(lst1):", id(lst1))
```

Kết quả sẽ là:

```
lst: [10, 20] id(lst): 1677678705472
lst1: [10, 20] id(lst1): 1677678706304
```

Mặc dù hai danh sách có cùng dữ liệu, chúng có các giá trị id() khác nhau, do đó chúng là hai đối tượng khác nhau và "lst1" là một bản sao của "lst".

Nếu chúng ta cố gắng sửa đổi "lst", nó sẽ không phản ánh trong "lst1". Hãy xem ví dụ sau:

#### Ví dụ 2

```python
lst[0] = 100
print("lst:", lst, "id(lst):", id(lst))
print("lst1:", lst1, "id(lst1):", id(lst1))
```

Kết quả sẽ là:

```
lst: [100, 20] id(lst): 1677678705472
lst1: [10, 20] id(lst1): 1677678706304
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*