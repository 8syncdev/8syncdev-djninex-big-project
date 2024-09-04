# Bài 2. Python - Thêm Các Phần Tử vào Tập Hợp

Mặc dù một tập hợp chỉ chứa các đối tượng không thể thay đổi, nhưng tập hợp chính nó là có thể thay đổi. Chúng ta có thể thêm các phần tử mới vào tập hợp bằng cách sử dụng một trong các cách sau đây:

## Thêm Các Phần Tử vào Tập Hợp

Phương thức `add()` trong lớp set thêm một phần tử mới vào tập hợp. Nếu phần tử đã có trong tập hợp, thì không có thay đổi nào trong tập hợp.

**Cú Pháp:**
```python
set.add(obj)
```

**Tham Số:**
- `obj` − một đối tượng của bất kỳ loại không thể thay đổi nào.

### Ví dụ

```python
lang1 = {"C", "C++", "Java", "Python"}
lang1.add("Golang")
print(lang1)
```

Kết quả sẽ là:

```
{'Python', 'C', 'Golang', 'C++', 'Java'}
```

## Thêm Tập Hợp Sử Dụng Phương thức `update()`

Phương thức `update()` của lớp set bao gồm các mục của tập hợp được chỉ định dưới dạng đối số. Nếu các phần tử trong tập hợp khác có một hoặc nhiều phần tử đã tồn tại, chúng sẽ không được bao gồm.

**Cú Pháp:**
```python
set.update(obj)
```

**Tham Số:**
- `obj` − một tập hợp hoặc một đối tượng chuỗi (list, tuple, string).

### Ví dụ

```python
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print(lang1)
```

Kết quả sẽ là:

```
{'Python', 'Java', 'C', 'C#', 'PHP', 'Perl', 'C++'}
```

## Thêm Bất Kỳ Đối Tượng Chuỗi Nào Như Các Phần Tử của Tập Hợp

Phương thức `update()` cũng chấp nhận bất kỳ đối tượng chuỗi nào là đối số. Ở đây, một tuple là đối số cho phương thức `update()`.

### Ví dụ

```python
lang1 = {"C", "C++", "Java", "Python"}
lang2 = ("PHP", "C#", "Perl")
lang1.update(lang2)
print(lang1)
```

Kết quả sẽ là:

```
{'Java', 'Perl', 'Python', 'C++', 'C#', 'C', 'PHP'}
```

**Lưu Ý:** Bạn cũng có thể sử dụng phương thức `union()` hoặc phương thức `|` để thực hiện phép hợp các tập hợp.

Trong Python, tập hợp là một loại dữ liệu mạnh mẽ cho việc làm việc với các tập hợp các mục duy nhất, và có nhiều cách để thêm các mục vào một tập hợp một cách linh hoạt.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*