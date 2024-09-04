# Bài 2. Python - Thay Đổi Các Mục của Từ Điển

Ngoài cách biểu diễn từ điển bằng cách đặt các cặp key:value phân tách bằng dấu phẩy trong dấu ngoặc nhọn, chúng ta có thể tạo đối tượng từ điển bằng hàm tích hợp sẵn `dict()`.

**Tạo Đối Tượng Từ Điển Rỗng**

Sử dụng hàm `dict()` mà không có đối số nào tạo ra một đối tượng từ điển rỗng. Nó tương đương với việc không đặt gì giữa các dấu ngoặc nhọn.

**Ví dụ**:

```python
d1 = dict()
d2 = {}
print ('d1: ', d1)
print ('d2: ', d2)
```

Kết quả sẽ là:

```
d1: {}
d2: {}
```

**Tạo Đối Tượng Từ Điển từ Danh Sách hoặc Bộ Các Tuple**

Hàm `dict()` xây dựng một từ điển từ một danh sách hoặc bộ các tuple có hai phần tử. Phần tử đầu tiên trong một tuple được xem xét là key và phần thứ hai là giá trị tương ứng.

**Ví dụ**:

```python
d1=dict([('a', 100), ('b', 200)])
d2 = dict((('a', 'one'), ('b', 'two')))
print ('d1: ', d1)
print ('d2: ', d2)
```

Kết quả sẽ là:

```
d1: {'a': 100, 'b': 200}
d2: {'a': 'one', 'b': 'two'}
```

**Tạo Đối Tượng Từ Điển từ Các Đối Số Từ Khóa**

Hàm `dict()` có thể nhận bất kỳ số lượng đối số từ khóa nào với các cặp tên=giá trị. Nó trả về một đối tượng từ điển với tên là key và liên kết nó với giá trị tương ứng.

**Ví dụ**:

```python
d1=dict(a= 100, b=200)
d2 = dict(a='one', b='two')
print ('d1: ', d1)
print ('d2: ', d2)
```

Kết quả sẽ là:

```
d1: {'a': 100, 'b': 200}
d2: {'a': 'one', 'b': 'two'}
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*