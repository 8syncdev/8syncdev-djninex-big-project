# Bài 27. Python - Booleans

Trong Python, bool là một loại con của kiểu int. Một đối tượng bool có hai giá trị có thể là True hoặc False, và nó được khởi tạo bằng các từ khóa True và False của Python.

## Ví dụ

```python
a = True
b = False
print(type(a), type(b))
```

Output:

```
<class 'bool'> <class 'bool'>
```

Một đối tượng bool được chấp nhận làm đối số cho các hàm chuyển đổi kiểu. Với True là đối số, hàm int() trả về 1, float() trả về 1.0; trong khi đối với False, chúng trả về 0 và 0.0 tương ứng. Chúng ta có một phiên bản một đối số của hàm complex().

Nếu đối số là một đối tượng phức tạp, nó được xem như phần thực, thiết lập hệ số ảo thành 0.

## Ví dụ

```python
a = int(True)
print("bool to int:", a)
a = float(False)
print("bool to float:", a)
a = complex(True)
print("bool to complex:", a)
```

Kết quả khi chạy mã này sẽ như sau:

```
bool to int: 1
bool to float: 0.0
bool to complex: (1+0j)
```

# Biểu thức Boolean trong Python

Biểu thức boolean trong Python là một biểu thức mà đánh giá thành một giá trị Boolean. Nó gần như luôn luôn liên quan đến một toán tử so sánh. Trong ví dụ dưới đây, chúng ta sẽ thấy làm thế nào các toán tử so sánh có thể cho chúng ta các giá trị Boolean. Phương thức bool() được sử dụng để trả về giá trị đúng hoặc sai của một biểu thức.

Cú pháp: bool([x])

Trả về True nếu X đánh giá thành True, ngược lại trả về False.

Nếu không có tham số, nó trả về False.

Dưới đây là các ví dụ sử dụng các chuỗi số và các giá trị Boolean làm tham số cho hàm bool. Kết quả được trả về là true hoặc false tùy thuộc vào tham số.

## Ví dụ

```python
# Kiểm tra True
a = True
print(bool(a))

# Kiểm tra False
a = False
print(bool(a))

# Kiểm tra 0
a = 0.0
print(bool(a))

# Kiểm tra 1
a = 1.0
print(bool(a))

# Kiểm tra sự bằng nhau
a = 5
b = 10
print(bool(a == b))

# Kiểm tra None
a = None
print(bool(a))

# Kiểm tra một chuỗi rỗng
a = ()
print(bool(a))

# Kiểm tra một mapping rỗng
a = {}
print(bool(a))

# Kiểm tra một chuỗi không rỗng
a = '8 Sync Dev'
print(bool(a))
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*