# Bài 5. Python - Gộp Tuple

## Gộp Tuple trong Python

Trong Python, Tuple được phân loại là một đối tượng loại chuỗi (sequence type). Đó là một tập hợp các mục, có thể thuộc các kiểu dữ liệu khác nhau, với mỗi mục có chỉ số vị trí bắt đầu từ 0. Mặc dù định nghĩa này cũng áp dụng cho danh sách (list), có hai sự khác biệt chính giữa danh sách (list) và tuple. Đầu tiên, trong khi các mục được đặt trong dấu ngoặc vuông trong trường hợp của danh sách (ví dụ: [10,20,30,40]), thì tuple được tạo thành bằng cách đặt các mục trong dấu ngoặc đơn (ví dụ: (10,20,30,40)).

Trong Python, Tuple là một đối tượng không thể thay đổi (immutable). Do đó, không thể thay đổi nội dung của một tuple sau khi nó được tạo ra trong bộ nhớ.

Tuy nhiên, bạn có thể sử dụng các cách khác nhau để gộp hai tuple Python.

### Gộp Tuple trong Python

Tất cả các đối tượng loại chuỗi (sequence type) đều hỗ trợ toán tử nối (+), với đó hai tuple có thể được gộp.

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = T1 + T2
print ("Tuple đã gộp:", T3)
```

Kết quả:

```
Tuple đã gộp: (10, 20, 30, 40, 'one', 'two', 'three', 'four')
```

### Gộp Tuple trong Python sử dụng toán tử nối tăng cường

Bạn cũng có thể sử dụng toán tử nối tăng cường với ký hiệu "+=" để thêm T2 vào T1.

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T1 += T2
print ("Tuple đã gộp:", T1)
```

### Gộp Tuple trong Python bằng cách mở rộng Tuple

Kết quả tương tự có thể được đạt được bằng cách sử dụng phương thức extend(). Ở đây, chúng ta cần chuyển đổi hai đối tượng tuple thành danh sách (list), mở rộng để thêm các phần tử từ một danh sách vào danh sách khác, và sau đó chuyển đổi danh sách đã gộp thành một tuple.

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Tuple đã gộp:", T1)
```

### Gộp Tuple trong Python sử dụng phương thức sum()

Hàm sum() có sẵn trong Python cũng giúp trong việc nối các tuple. Chúng ta sử dụng một biểu thức

sum((t1, t2), ())

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Tuple đã gộp:", T3)
```

### Gộp Tuple trong Python sử dụng List Comprehension

Một cách tiếp cận phức tạp hơn để gộp hai tuple là sử dụng list comprehension.

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1, L2 = list

(T1), list(T2)
L3 = [y for x in [L1, L2] for y in x]
T3 = tuple(L3)
print ("Tuple đã gộp:", T3)
```

### Gộp Tuple trong Python sử dụng vòng lặp for

Bạn có thể chạy một vòng lặp for trên các phần tử trong tuple thứ hai, chuyển đổi mỗi phần tử thành một tuple chỉ chứa một phần tử và nối nó vào tuple đầu tiên với toán tử "+="

**Ví dụ**:

```python
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
    T1 += (t,)
print (T1)
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*