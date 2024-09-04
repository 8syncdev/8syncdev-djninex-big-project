# Bài 3. Python - Thêm Mục vào Từ Điển

## Sử dụng Toán Tử
Toán tử "[]" (được sử dụng để truy cập giá trị được ánh xạ với một key trong từ điển) được sử dụng để cập nhật một cặp key-value hiện có cũng như thêm một cặp mới.

**Cú Pháp**:
```python
dict["key"] = val
```

Nếu key đã tồn tại trong đối tượng từ điển, giá trị của nó sẽ được cập nhật thành val. Nếu key không tồn tại trong từ điển, một cặp key-value mới sẽ được thêm vào.

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: ", marks)
marks['Laxman'] = 95
print ("Từ điển marks sau khi cập nhật: ", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật: {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật: {'Savita': 67, 'Imtiaz': 88, 'Laxman': 95, 'David': 49}
```

**Ví dụ**:

Tuy nhiên, một mục với key 'Krishnan' không có trong từ điển, do đó một cặp key-value mới được thêm vào.

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: ", marks)
marks['Krishan'] = 74
print ("Từ điển marks sau khi cập nhật: ", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật: {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật: {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49, 'Krishan': 74}
```

## Sử dụng Phương Thức update()
Bạn có thể sử dụng phương thức `update()` trong lớp dict theo ba cách khác nhau:

### Cập Nhật với Từ Điển Khác
Trong trường hợp này, đối số của phương thức `update()` là một từ điển khác. Giá trị của các key phổ biến trong cả hai từ điển được cập nhật. Đối với các key mới, cặp key-value được thêm vào từ điển hiện tại.

**Cú Pháp**:
```python
d1.update(d2)
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks.update(marks1)
print ("Từ điển marks sau khi cập nhật: \n", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

### Cập Nhật với Iterable
Nếu đối số của phương thức `update()` là một danh sách hoặc bộ các tuple có hai phần tử, một mục cho mỗi phần tử sẽ được thêm vào từ điển hiện tại, hoặc được cập nhật nếu key đã tồn tại.

**Cú Pháp**:
```python
d1.update([(k1, v1), (k2, v2)])
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks1 = [("Sharad",

 51), ("Mushtaq", 61), ("Laxman", 89)]
marks.update(marks1)
print ("Từ điển marks sau khi cập nhật: \n", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

### Cập Nhật với Các Đối Số Từ Khóa
Phiên bản thứ ba của phương thức `update()` chấp nhận một danh sách các đối số từ khóa trong định dạng tên=giá trị. Các cặp key-value mới được thêm vào, hoặc giá trị của key hiện có được cập nhật.

**Cú Pháp**:
```python
d1.update(k1=v1, k2=v2)
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks.update(Sharad = 51, Mushtaq = 61, Laxman = 89)
print ("Từ điển marks sau khi cập nhật: \n", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

## Sử Dụng Toán Tử Unpack
Ký hiệu "**" được đặt trước một đối tượng từ điển giải nén nó thành một danh sách các tuple, mỗi tuple với key và value. Hai đối tượng dict được giải nén và kết hợp lại với nhau để thu được một từ điển mới.

**Cú Pháp**:
```python
d3 = {**d1, **d2}
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("Từ điển marks sau khi cập nhật: \n", newmarks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

## Sử Dụng Toán Tử Union (|)
Python giới thiệu "|" (ký hiệu đường ống) làm toán tử union cho các toán hạng từ điển. Nó cập nhật các key đã tồn tại trong đối tượng dict bên trái và thêm các cặp key-value mới để trả về một đối tượng dict mới.

**Cú Pháp**:
```python
d3 = d1 | d2
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("Từ điển marks sau khi cập nhật: \n", newmarks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Sav

ita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

## Sử Dụng Toán Tử "|=" (|)
Toán tử "|=" là một toán tử Union được bổ sung. Nó thực hiện cập nhật trong chỗ trên toán tử từ điển ở bên trái bằng cách thêm các key mới trong toán tử từ điển ở bên phải, và cập nhật các key đã tồn tại.

**Cú Pháp**:
```python
d1 |= d2
```

**Ví dụ**:

```python
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Từ điển marks trước khi cập nhật: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("Từ điển marks sau khi cập nhật: \n", marks)
```

Kết quả sẽ là:

```
Từ điển marks trước khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Từ điển marks sau khi cập nhật:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*