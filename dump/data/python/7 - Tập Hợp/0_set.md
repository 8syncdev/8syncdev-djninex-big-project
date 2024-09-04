# Bài 0. Python - Tập hợp (Sets)

Trong Python, một tập hợp là một trong các loại dữ liệu có sẵn. Trong toán học, tập hợp là một bộ sưu tập các đối tượng riêng biệt. Loại dữ liệu tập hợp là cách thức Python thực hiện một tập hợp. Các đối tượng trong một tập hợp có thể là bất kỳ loại dữ liệu nào.

Tập hợp trong Python cũng là một loại dữ liệu tập hợp như danh sách hoặc bộ. Tuy nhiên, nó không phải là một bộ sưu tập có thứ tự, tức là các mục trong một tập hợp không thể truy cập bằng chỉ số vị trí của chúng. Một đối tượng tập hợp là một bộ sưu tập của một hoặc nhiều đối tượng không thay đổi được bao gồm trong dấu ngoặc nhọn {}.

## Ví dụ

### Ví dụ 1

Dưới đây là một số ví dụ về các đối tượng tập hợp:

```python
s1 = {"Rohan", "Physics", 21, 69.75}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
print (s1)
print (s2)
print (s3)
print (s4)
```

Kết quả sẽ là:

```
{'Physics', 21, 'Rohan', 69.75}
{1, 2, 3, 4, 5}
{'a', 'd', 'c', 'b'}
{25.5, -55, True, (1+2j)}
```

### Ví dụ 2

Hàm set() cũng xây dựng một đối tượng tập hợp từ một đối tượng chuỗi (danh sách, bộ hoặc chuỗi).

```python
L1 = ["Rohan", "Physics", 21, 69.75]
s1 = set(L1)
T1 = (1, 2, 3, 4, 5)
s2 = set(T1)
string = "8SyncDev"
s3 = set(string)

print (s1)
print (s2)
print (s3)
```

Kết quả sẽ là:

```
{'Rohan', 69.75, 21, 'Physics'}
{1, 2, 3, 4, 5}
{'u', 'a', 'o', 'n', 'r', 's', 'T', 'P', 'i', 't', 'l'}
```

### Ví dụ 3

Tập hợp là một bộ sưu tập các đối tượng riêng biệt. Ngay cả khi bạn lặp lại một đối tượng trong tập hợp, chỉ có một bản sao được giữ lại trong đó.

```python
s2 = {1, 2, 3, 4, 5, 3,0, 1, 9}
s3 = {"a", "b", "c", "d", "b", "e", "a"}
print (s2)
print (s3)
```

Kết quả sẽ là:

```
{0, 1, 2, 3, 4, 5, 9}
{'a', 'b', 'd', 'c', 'e'}
```

### Ví dụ 4

Chỉ các đối tượng không thể thay đổi được có thể được sử dụng để tạo ra một đối tượng tập hợp. Bất kỳ kiểu số nào, chuỗi và bộ đều được phép, nhưng bạn không thể đặt một danh sách hoặc một từ điển trong một tập hợp.

```python
s1 = {1, 2, [3, 4, 5], 3,0, 1, 9}
print (s1)
s2 = {"Rohan", {"phy":50}}
print (s2)
```

Kết quả sẽ là:

```
   s1 = {1, 2, [3, 4, 5], 3,0, 1, 9}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
   s2 = {"Rohan", {"phy":50}}
        ^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'dict'
```

Python sẽ nâng TypeError với thông báo unhashable types 'list' hoặc 'dict'. Việc băm tạo ra một số duy nhất cho một mục không thay đổi mà cho phép tìm kiếm nhanh trong bộ nhớ của máy tính. Python có hàm hash() tích hợp. Hàm này không được hỗ trợ bởi danh sách hoặc từ điển.

Mặc dù các đối tượng không thể thay đổi không được lưu trữ trong một tập hợp, nhưng tập hợp chính nó là một đối tượng có thể thay đổi. Python có các toán tử đặc biệt để làm việc với các tập hợp, và có các phương thức khác nhau trong lớp tập hợp để thực hiện các thao tác thêm, loại bỏ, cập nhật trên các phần tử của một đối tượng tập hợp.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*