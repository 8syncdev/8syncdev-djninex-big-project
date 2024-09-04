# Bài 11. Tài liệu Hướng dẫn về Các Loại Dữ Liệu và Ép Kiểu trong Python

## Giới thiệu

Trong lập trình, dữ liệu là một phần quan trọng và đóng vai trò quan trọng trong việc xử lý thông tin. Trong Python, các loại dữ liệu được sử dụng để định nghĩa loại dữ liệu mà ta sẽ lưu trữ trong một biến và xử lý trong chương trình. Dữ liệu được lưu trữ trong bộ nhớ của máy tính có thể là nhiều loại khác nhau, ví dụ: tuổi của một người được lưu trữ dưới dạng một giá trị số và địa chỉ của họ được lưu trữ dưới dạng các ký tự chữ và số.

## Loại Dữ Liệu trong Python

Python hỗ trợ nhiều loại dữ liệu tích hợp sẵn, bao gồm:

1. **Dữ liệu Số:** int, float, complex
2. **Dữ liệu Chuỗi:** str (kiểu dữ liệu dạng văn bản)
3. **Dữ liệu Dãy:** list, tuple, range
4. **Dữ liệu Nhị Phân:** bytes, bytearray, memoryview
5. **Dữ liệu Ánh Xạ:** dict
6. **Dữ liệu Boolean:** bool
7. **Dữ liệu Tập hợp:** set, frozenset
8. **Dữ liệu None:** NoneType

## Dữ Liệu Số trong Python

Dữ liệu số trong Python được sử dụng để lưu trữ các giá trị số. Có bốn loại số khác nhau trong Python:

- **int:** Số nguyên
- **float:** Số thực
- **complex:** Số phức

Ví dụ:

```python
var1 = 1       # int
var2 = True    # bool
var3 = 10.023  # float
var4 = 10+3j   # complex
```

## Dữ Liệu Chuỗi trong Python

Dữ liệu chuỗi trong Python là một chuỗi gồm một hoặc nhiều ký tự Unicode, được bao quanh bởi dấu nháy đơn, dấu nháy kép hoặc dấu nháy ba. Chuỗi trong Python là không thể thay đổi, có nghĩa là khi bạn thực hiện một phép toán trên chuỗi, bạn luôn tạo ra một đối tượng chuỗi mới cùng loại, thay vì biến đổi một chuỗi hiện tại.

```python
str1 = 'Hello World!'
```

## Dữ Liệu Dãy trong Python

Dãy trong Python là một tập hợp có thứ tự của các phần tử. Có ba loại dãy trong Python:

- **List:** Dãy có thể thay đổi
- **Tuple:** Dãy không thể thay đổi
- **Range:** Dãy số liên tục

Ví dụ:

```python
list1 = [1, 2, 3, 4, 5]     # list
tuple1 = (1, 2, 3, 4, 5)    # tuple
range1 = range(1, 6)        # range
```

## Dữ Liệu Nhị Phân trong Python

Dữ liệu nhị phân trong Python là cách biểu diễn dữ liệu dưới dạng một chuỗi các chữ số nhị phân, chỉ bao gồm các số 0 và 1. Python cung cấp ba cách khác nhau để biểu diễn dữ liệu nhị phân:

- **bytes:** Dữ liệu bytes không thể thay đổi
- **bytearray:** Dữ liệu bytearray có thể thay đổi
- **memoryview:** Dữ liệu memoryview

Ví dụ:

```python
bytes1 = b'Hello'           # bytes
bytearray1 = bytearray(b'Hello')  # bytearray
```

## Dữ Liệu Ánh Xạ trong Python

Dữ liệu ánh xạ trong Python là một cấu trúc dữ liệu dạng hash table. Mỗi phần tử trong ánh xạ được xác định bằng một cặp key:value. Trong Python, ánh xạ là một đối tượng của lớp dict.

```python
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}  # dict
```

## Dữ Liệu Boolean trong Python

Dữ liệu Boolean trong Python biểu diễn một trong hai giá trị: True hoặc False. Dữ liệu Boolean thường được sử dụng để kiểm tra điều kiện trong các biểu thức điều kiện.

```python
bool1 = True   # bool
bool2 = False  # bool
```

## Ép Kiểu Dữ Liệu trong Python

Đôi khi, bạn có thể cần thực hiện chuyển đổi giữa các loại dữ liệu Python. Để chuyển đổi dữ liệu giữa các loại khác nhau trong Python, bạn đơn giản sử dụng tên loại dữ liệu như một hàm.

Ví dụ:

```python
a = int(1)        # Ép kiểu thành số nguyên
b = float(2.2)    # Ép kiểu thành số thực
c = str(3.3)      # Ép kiểu thành chuỗi
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*