# Bài 4. Python - Định Dạng Chuỗi trong Python

Định dạng chuỗi là quá trình xây dựng một biểu diễn chuỗi một cách linh hoạt bằng cách chèn giá trị của các biểu thức số học vào một chuỗi đã tồn tại. Toán tử ghép chuỗi của Python không chấp nhận một toán hạng không phải là chuỗi. Do đó, Python cung cấp các kỹ thuật định dạng chuỗi sau:

1. Sử dụng toán tử % cho sự thay thế
2. Sử dụng phương thức format() của lớp str
3. Sử dụng cú pháp f-string
4. Sử dụng lớp String Template

## Sử Dụng Toán Tử % cho Sự Thay Thế

Toán tử % cho phép thay thế các giá trị trong một chuỗi bằng các giá trị đã cho. Đây là cách cũ nhưng vẫn được sử dụng phổ biến.

**Ví dụ**

```python
name = "John"
age = 30
print("Tên của tôi là %s và tôi %d tuổi." % (name, age))
```

Kết quả sẽ là:

```
Tên của tôi là John và tôi 30 tuổi.
```

## Sử Dụng Phương Thức format() của Lớp str

Phương thức format() cho phép định dạng một chuỗi bằng cách chèn các giá trị được chỉ định trong chuỗi.

**Ví dụ**

```python
name = "Alice"
age = 25
print("Tên của tôi là {} và tôi {} tuổi.".format(name, age))
```

Kết quả sẽ là:

```
Tên của tôi là Alice và tôi 25 tuổi.
```

## Sử Dụng Cú Pháp f-string

f-string là một cú pháp mới trong Python (bắt đầu từ Python 3.6) cho phép thực hiện định dạng chuỗi một cách nhanh chóng và dễ dàng.

**Ví dụ**

```python
name = "Emma"
age = 35
print(f"Tên của tôi là {name} và tôi {age} tuổi.")
```

Kết quả sẽ là:

```
Tên của tôi là Emma và tôi 35 tuổi.
```

## Sử Dụng Lớp String Template

Lớp String Template cung cấp một cách khác để thực hiện định dạng chuỗi bằng cách chèn các giá trị được chỉ định trong chuỗi.

**Ví dụ**

```python
from string import Template

name = "Sophia"
age = 40
template = Template("Tên của tôi là $name và tôi $age tuổi.")
print(template.substitute(name=name, age=age))
```

Kết quả sẽ là:

```
Tên của tôi là Sophia và tôi 40 tuổi.
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*