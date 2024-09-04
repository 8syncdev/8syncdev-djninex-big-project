# Bài 5. Python - Lặp Qua Danh Sách

## Lặp Qua Các Phần Tử của Danh Sách

Bạn có thể duyệt qua các phần tử trong một danh sách bằng cấu trúc vòng lặp for của Python. Việc duyệt qua có thể được thực hiện, sử dụng danh sách như một bộ lặp hoặc với sự giúp đỡ của chỉ số.

### Cú Pháp

Danh sách Python cung cấp một đối tượng bộ lặp. Để lặp qua một danh sách, sử dụng câu lệnh for như sau:

```python
for obj in list:
   . . .
   . . .
```

### Ví dụ

Hãy xem ví dụ sau −

```python
lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print(num, end=' ')
```

#### Kết Quả

```
25 12 10 -21 10 100
```

## Lặp Qua Các Phần Tử của Danh Sách với Chỉ Số

Để lặp qua các phần tử trong một danh sách, hãy lấy đối tượng phạm vi các số nguyên từ "0" đến "len-1". Xem ví dụ sau:

### Ví dụ

```python
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print("lst[{}]: ".format(i), lst[i])
```

#### Kết Quả

```
lst[0]: 25
lst[1]: 12
lst[2]: 10
lst[3]: -21
lst[4]: 10
lst[5]: 100
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*