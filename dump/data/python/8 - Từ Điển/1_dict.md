# Bài 1. Python - Truy Cập Các Mục của Từ Điển

Trong Python, bạn có thể sử dụng toán tử "[ ]" để truy xuất giá trị được liên kết với một key cụ thể trong đối tượng từ điển, mặc dù từ điển không phải là một chuỗi vì các phần tử trong từ điển không được đánh chỉ mục.

**Ví dụ 1**:

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Thủ đô của Gujarat là: ", capitals['Gujarat'])
print ("Thủ đô của Karnataka là: ", capitals['Karnataka'])
```

Kết quả sẽ là:

```
Thủ đô của Gujarat là: Gandhinagar
Thủ đô của Karnataka là: Bengaluru
```

**Ví dụ 2**:
Python sẽ gây ra một KeyError nếu key được đưa vào trong dấu ngoặc vuông không có trong đối tượng từ điển.

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Thủ đô của Haryana là: ", capitals['Haryana'])
```

Nó sẽ gây ra một lỗi KeyError.

**Sử dụng Phương thức get()**:

Phương thức get() trong lớp dict của Python trả về giá trị được ánh xạ với key đã cho.

**Cú pháp**:

```python
val = dict.get("key")
```

**Tham số**:

- `key`: Một đối tượng không thay đổi được sử dụng làm key trong đối tượng từ điển.

**Giá trị Trả về**:

Phương thức get() trả về đối tượng được ánh xạ với key đã cho.

**Ví dụ 3**:

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Thủ đô của Gujarat là: ", capitals.get('Gujarat'))
print ("Thủ đô của Karnataka là: ", capitals.get('Karnataka'))
```

Kết quả sẽ là:

```
Thủ đô của Gujarat là: Gandhinagar
Thủ đô của Karnataka là: Bengaluru
```

**Ví dụ 4**:

Khác với toán tử "[]", phương thức get() không gây ra lỗi nếu key không được tìm thấy; nó trả về None.

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Thủ đô của Haryana là: ", capitals.get('Haryana'))
```

Kết quả sẽ là:

```
Thủ đô của Haryana là: None
```

**Ví dụ 5**:

Phương thức get() chấp nhận một đối số chuỗi tùy chọn. Nếu nó được cung cấp và nếu key không được tìm thấy, chuỗi này sẽ trở thành giá trị trả về.

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Thủ đô của Haryana là: ", capitals.get('Haryana', 'Không tìm thấy'))
```

Kết quả sẽ là:

```
Thủ đô của Haryana là: Không tìm thấy
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*