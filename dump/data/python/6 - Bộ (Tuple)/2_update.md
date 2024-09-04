# Bài 2. Python - Cập nhật Tuple

Trong Python, tuple là một kiểu dữ liệu không thay đổi. Một đối tượng không thay đổi không thể được sửa đổi sau khi nó được tạo trong bộ nhớ.

Ví dụ:

Nếu chúng ta cố gắng gán một giá trị mới cho một mục tuple bằng toán tử lát cắt, Python sẽ ném ra TypeError. Xem ví dụ sau:

```python
tup1 = ("a", "b", "c", "d")
tup1[2] = 'Z'
print ("tup1: ", tup1)
```

Sẽ cho ra kết quả sau:

```
Traceback (most recent call last):
 File "C:\Users\mlath\examples\main.py", line 2, in <module>
  tup1[2] = 'Z'
  ~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

Do đó, không thể cập nhật một tuple. Do đó, lớp tuple không cung cấp các phương thức để thêm, chèn, xóa, sắp xếp các mục từ một đối tượng tuple, giống như lớp list.

Thay đổi Giá trị của Tuple trong Python
Bạn có thể sử dụng một cách làm phụ để cập nhật một tuple. Sử dụng hàm list(), chuyển đổi tuple thành một danh sách, thực hiện các hoạt động thêm/ chèn/xóa mong muốn và sau đó phân tích cú pháp danh sách trở lại thành đối tượng tuple.

Ví dụ:

Ở đây, chúng tôi chuyển đổi tuple thành một danh sách, cập nhật một mục hiện có, thêm một mục mới và sắp xếp danh sách. Danh sách được chuyển đổi trở lại thành đối tượng tuple.

```python
tup1 = ("a", "b", "c", "d")
print ("Tuple trước khi cập nhật", tup1, "id(): ", id(tup1))

list1 = list(tup1)
list1[2]='F'
list1.append('Z')
list1.sort()
print ("danh sách đã cập nhật", list1)

tup1 = tuple(list1)
print ("Tuple sau khi cập nhật", tup1, "id(): ", id(tup1))
```

Sẽ cho ra kết quả sau:

```
Tuple trước khi cập nhật ('a', 'b', 'c', 'd') id(): 2295023084192
danh sách đã cập nhật ['F', 'Z', 'a', 'b', 'd']
Tuple sau khi cập nhật ('F', 'Z', 'a', 'b', 'd') id(): 2295021518128
```

Tuy nhiên, lưu ý rằng id() của tup1 trước và sau khi cập nhật là khác nhau. Điều này có nghĩa là một đối tượng tuple mới được tạo ra và đối tượng tuple ban đầu không được sửa đổi tại chỗ.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*