# Bài 24. Python - Chú thích

## Giới thiệu về Chú thích trong Python

Chú thích trong một chương trình máy tính là một phần văn bản được đặt ra để giải thích hoặc mô tả trong mã nguồn và không được xem xét bởi trình biên dịch/trình thông dịch khi tạo mã ngôn ngữ máy. Việc sử dụng chú thích một cách phong phú trong chương trình nguồn giúp mọi người hiểu rõ hơn về cú pháp, cách sử dụng và logic của thuật toán vv., miễn là nó được chú thích một cách đẹp mắt.

## Chú thích trong Python

Chú thích trong Python giúp mã nguồn trở nên dễ hiểu hơn và chúng hoàn toàn bị bỏ qua bởi trình thông dịch, điều này có nghĩa là bạn có thể cung cấp bất kỳ số lượng chú thích nào bạn muốn trong chương trình của mình để làm cho nó trở nên dễ đọc và giải thích hơn.

Python hỗ trợ hai loại chú thích:

### Chú thích trên một dòng

Trong một kịch bản Python, ký hiệu # đánh dấu sự bắt đầu của dòng chú thích. Nó có hiệu quả cho đến cuối dòng trong trình soạn thảo. Nếu # là ký tự đầu tiên của dòng, toàn bộ dòng sẽ được coi là một chú thích và trình thông dịch sẽ bỏ qua nó.

**Ví dụ về Chú thích trên Một Dòng trong Python:**

```python
# Đây là một chú thích
print("Xin chào thế giới")

# Nếu # được sử dụng ở giữa một dòng, văn bản trước nó là một biểu thức Python hợp lệ, trong khi văn bản sau nó được coi là chú thích.

print("Bạn khỏe không?")  # Đây cũng là một chú thích nhưng sau một câu lệnh.
```

### Chú thích trên Nhiều Dòng

Trong Python, không có quy định để viết chú thích trên nhiều dòng, hoặc một chú thích dạng khối. (Như trong C/C++, nơi nhiều dòng bên trong /* .. */ được xem là chú thích trên nhiều dòng).

Mỗi dòng nên có ký tự # ở đầu để được đánh dấu là chú thích trong Python và đó là cách bạn có thể tạo chú thích trên nhiều dòng trong Python.

**Ví dụ về Chú thích trên Nhiều Dòng trong Python:**

```python
#
# Đây là một chú thích trên nhiều dòng
# có thể trải dài qua nhiều dòng.
#
print("Xin chào thế giới")

"""
Đây là một chú thích trên nhiều dòng
có thể trải dài qua nhiều dòng.
"""
print("Xin chào thế giới")
```

### Chú thích với Docstring

Docstring Python cung cấp một cách thuận tiện để cung cấp tài liệu trợ giúp với các module Python, hàm, lớp và phương thức. Docstring sau đó sẽ được truy cập thông qua thuộc tính __doc__.

**Ví dụ về Chú thích với Docstring trong Python:**

```python
def add(a, b):
    """Hàm để cộng giá trị của a và b"""
    return a + b

print(add.__doc__)
```

Kết quả sẽ là:

```
Hàm để cộng giá trị của a và b
```

Việc sử dụng chú thích trong Python giúp mã nguồn trở nên dễ hiểu hơn và chúng hoàn toàn được bỏ qua bởi trình thông dịch. Điều này có nghĩa là bạn có thể cung cấp bất kỳ số lượng chú thích nào bạn muốn trong chương trình của mình để làm cho nó dễ đọc và rõ ràng hơn.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
