# Bài 4. Hướng dẫn Sử dụng Câu lệnh if Lồng nhau trong Python

## Mục đích

Tài liệu này mô tả cách sử dụng câu lệnh if lồng nhau trong Python. Câu lệnh if lồng nhau cho phép chúng ta kiểm tra các điều kiện nằm trong các điều kiện khác.

## Cú pháp

Cú pháp của câu lệnh if lồng nhau sẽ như sau:

```python
if biểu_thức1:
    # Khối mã
    if biểu_thức2:
        # Khối mã
    elif biểu_thức3:
        # Khối mã
    else:
        # Khối mã
elif biểu_thức4:
    # Khối mã
else:
    # Khối mã
```

## Ví dụ

Hãy xem một ví dụ để hiểu cách hoạt động của câu lệnh if lồng nhau.

```python
num = 8
print("num = ", num)
if num % 2 == 0:
    if num % 3 == 0:
        print("Chia hết cho 3 và 2")
    else:
        print("Chia hết cho 2 nhưng không chia hết cho 3")
else:
    if num % 3 == 0:
        print("Chia hết cho 3 nhưng không chia hết cho 2")
    else:
        print("Không chia hết cho cả 2 và 3")
```

Khi mã trên được thực thi, nó sẽ tạo ra kết quả sau:

```
num = 8
Chia hết cho 2 nhưng không chia hết cho 3
num = 15
Chia hết cho 3 nhưng không chia hết cho 2
num = 12
Chia hết cho 3 và 2
num = 5
Không chia hết cho cả 2 và 3
```

Trong ví dụ này, chúng ta kiểm tra xem số `num` có chia hết cho 2 hay không. Nếu có, chúng ta tiếp tục kiểm tra xem `num` có chia hết cho 3 không. Tùy thuộc vào kết quả của các điều kiện, chúng ta in ra thông điệp tương ứng.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*