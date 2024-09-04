# Bài 6. Python - Phương thức Tuple

Trong Python, vì một tuple là không thể thay đổi, nên lớp tuple không định nghĩa các phương thức để thêm hoặc loại bỏ các mục. Lớp tuple chỉ định nghĩa hai phương thức.

## 1. tuple.count(obj)

Trả về số lần xuất hiện của obj trong tuple.

## 2. tuple.index(obj)

Trả về chỉ số thấp nhất trong tuple mà obj xuất hiện.

### Tìm Chỉ Số của Một Phần Tử trong Tuple

Phương thức index() của lớp tuple trả về chỉ số của sự xuất hiện đầu tiên của mục được cung cấp.

**Cú pháp**:

```python
tuple.index(obj)
```

**Giá trị trả về**:

Phương thức index() trả về một số nguyên, đại diện cho chỉ số của sự xuất hiện đầu tiên của "obj".

**Ví dụ**:

```python
tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("Chỉ số đầu tiên của 10:", x)
```

### Đếm Các Mục trong Tuple

Phương thức count() trong lớp tuple trả về số lần một đối tượng cụ thể xuất hiện trong tuple.

**Cú pháp**:

```python
tuple.count(obj)
```

**Giá trị trả về**:

Số lần xuất hiện của đối tượng. Phương thức count() trả về một số nguyên.

**Ví dụ**:

```python
tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("Số lần xuất hiện của 10:", c)
```

### Ví dụ

Kể cả nếu các mục trong tuple chứa biểu thức, chúng sẽ được đánh giá để lấy số lần đếm.

```python
Tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(0.25)
print ("Số lần xuất hiện của 10:", c)
```

### Kết luận

Các phương thức `count()` và `index()` của tuple giúp bạn thao tác và truy vấn dữ liệu trong các tuple một cách thuận tiện và hiệu quả.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*