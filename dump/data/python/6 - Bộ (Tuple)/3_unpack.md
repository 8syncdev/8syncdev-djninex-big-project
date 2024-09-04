# Bài 3. Python - Giải nén các phần tử của Tuple

Thuật ngữ "giải nén" đề cập đến quá trình phân tích các phần tử tuple thành các biến riêng lẻ. Trong Python, dấu ngoặc đơn là các dấu phân cách mặc định cho một biểu diễn chữ của đối tượng chuỗi.

Các câu lệnh sau để khai báo một tuple là giống nhau.

```python
t1 = (x,y)
t1 = x,y
type (t1)
<class 'tuple'>
```

Ví dụ:

Để lưu trữ các phần tử tuple trong các biến riêng lẻ, hãy sử dụng nhiều biến trên bên trái của toán tử gán, như được thể hiện trong ví dụ sau:

```python
tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", y, "z: ", z)
```

Sẽ cho ra kết quả sau:

```
x: 10 y: 20 z: 30
```

Đó là cách mà tuple được giải nén thành các biến riêng lẻ.

Trong ví dụ trên, số lượng biến bên trái của toán tử gán bằng số phần tử trong tuple. Điều gì sẽ xảy ra nếu số lượng không bằng số phần tử?

# ValueError Khi Giải nén một Tuple

Nếu số lượng biến nhiều hơn hoặc ít hơn so với độ dài của tuple, Python sẽ ném ra một ValueError.

Ví dụ:

```python
tup1 = (10,20,30)
x, y = tup1
x, y, p, q = tup1
```

Sẽ cho ra kết quả sau:

```
  x, y = tup1
  ^^^^
ValueError: too many values to unpack (expected 2)
  x, y, p, q = tup1
  ^^^^^^^^^^
ValueError: not enough values to unpack (expected 4, got 3)
```

# Giải nén các phần tử của Tuple Sử Dụng Dấu * (Asterisk)

Trong trường hợp như vậy, ký hiệu "*" được sử dụng để giải nén. Tiền tố "*" cho "y", như được thể hiện dưới đây −

## Ví dụ 1

```python
tup1 = (10,20,30)
x, *y = tup1
print ("x: ", x, "y: ", y)
```

Sẽ cho ra kết quả sau:

```
x: 10 y: [20, 30]
```

Giá trị đầu tiên trong tuple được gán cho "x", và phần còn lại được gán cho "y" và trở thành một danh sách.

## Ví dụ 2

Trong ví dụ này, tuple chứa 6 giá trị và các biến để giải nén là 3. Chúng ta thêm "*" vào biến thứ hai.

```python
tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ", x, "y: ", y, "z: ", z)
```

Sẽ cho ra kết quả sau:

```
x: 10 y: [20, 30, 40, 50] z: 60
```

Ở đây, giá trị được giải nén trong "x" và "z" trước, và sau đó các giá trị còn lại được gán cho "y" dưới dạng một danh sách.

## Ví dụ 3

Điều gì sẽ xảy ra nếu chúng ta thêm "*" vào biến đầu tiên?

```python
tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ", x, "y: ", y, "z: ", z)
```

Sẽ cho ra kết quả sau:

```
x: [10, 20, 30, 40] y: 50 z: 60
```

Ở đây, một lần nữa, tuple được giải nén sao cho các biến riêng lẻ lấy giá trị trước, để lại các giá trị còn lại cho danh sách "x".

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*