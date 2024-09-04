# Bài 1. Python - Truy cập Các Phần Tử trong Tập Hợp

Vì tập hợp không phải là một loại dữ liệu chuỗi, nên các mục của nó không thể được truy cập một cách cá nhân vì chúng không có chỉ số vị trí (như trong danh sách hoặc bộ). Các mục của tập hợp cũng không có một khóa (như trong từ điển) để truy cập. Bạn chỉ có thể duyệt qua các mục của tập hợp bằng cách sử dụng vòng lặp for.

## Ví dụ

### Ví dụ 1

```python
langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print(lang)
```

Kết quả sẽ là:

```
Python
C
C++
Java
```

### Kiểm tra Sự Tồn Tại của Phần Tử Trong Tập Hợp

Toán tử thành viên của Python cho phép bạn kiểm tra xem một mục cụ thể có sẵn trong tập hợp hay không. Hãy xem ví dụ sau:

### Ví dụ 2

```python
langs = {"C", "C++", "Java", "Python"}
print("PHP" in langs)
print("Java" in langs)
```

Kết quả sẽ là:

```
False
True
```

Như vậy, bạn không thể truy cập các phần tử của tập hợp một cách trực tiếp nhưng có thể sử dụng vòng lặp for để duyệt qua chúng và sử dụng các toán tử thành viên để kiểm tra sự tồn tại của một phần tử trong tập hợp.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*