# Bài 5. Python - Câu lệnh Match-Case

## Giới thiệu

Trước phiên bản 3.10 của Python, Python thiếu một tính năng tương tự như switch-case trong C hoặc C++. Trong Python 3.10, một kỹ thuật phù hợp gọi là match-case đã được giới thiệu, tương tự như cấu trúc switch-case có sẵn trong C/C++/Java v.v.

## Câu lệnh Match-Case trong Python

Một câu lệnh match-case trong Python nhận một biểu thức và so sánh giá trị của nó với các mẫu liên tiếp được đưa ra dưới dạng một hoặc nhiều khối case. Việc sử dụng tương tự hơn với phù hợp mẫu trong các ngôn ngữ như Rust hoặc Haskell hơn là một câu lệnh switch trong C hoặc C++. Chỉ có mẫu đầu tiên phù hợp được thực thi. Cũng có thể trích xuất các thành phần (phần tử chuỗi hoặc thuộc tính đối tượng) từ giá trị vào các biến.

Việc sử dụng cơ bản của match-case là so sánh một biến với một hoặc nhiều giá trị.

## Cú pháp

Dưới đây là cú pháp của câu lệnh match-case trong Python:

```python
match biến:
   case 'mẫu 1': câu lệnh 1
   case 'mẫu 2': câu lệnh 2
   ...
   case 'mẫu n': câu lệnh n
```

## Ví dụ

Dưới đây là một ví dụ về cách sử dụng câu lệnh match-case:

```python
def ngay_trong_tuan(n):
   match n:
      case 0: return "Thứ Hai"
      case 1: return "Thứ Ba"
      case 2: return "Thứ Tư"
      case 3: return "Thứ Năm"
      case 4: return "Thứ Sáu"
      case 5: return "Thứ Bảy"
      case 6: return "Chủ Nhật"
      case _: return "Số ngày không hợp lệ"
print(ngay_trong_tuan(3))
print(ngay_trong_tuan(6))
print(ngay_trong_tuan(7))
```

Khi mã trên được thực thi, nó sẽ tạo ra kết quả sau:

```
Thứ Năm
Chủ Nhật
Số ngày không hợp lệ
```

## Kết luận

Câu lệnh match-case trong Python là một công cụ mạnh mẽ để kiểm tra nhiều trường hợp và thực thi các hành động phù hợp dựa trên giá trị của biến. Nó cung cấp một cú pháp rõ ràng và dễ hiểu để xử lý các tình huống phù hợp.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
