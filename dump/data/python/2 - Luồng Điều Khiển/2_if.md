# Bài 2. Python - Mệnh đề if

Trong Python, mệnh đề if thực hiện việc thực thi có điều kiện. Nó chứa một biểu thức logic để so sánh dữ liệu và quyết định được đưa ra dựa trên kết quả của sự so sánh đó.

## Cú pháp của Mệnh đề if

```python
if biểu_thức:
   câu_lệnh(s)
```

Nếu biểu thức logic đánh giá thành TRUE, thì khối câu lệnh bên trong mệnh đề if sẽ được thực thi. Nếu biểu thức logic đánh giá thành FALSE, thì tập hợp câu lệnh đầu tiên sau khi kết thúc của mệnh đề if sẽ được thực thi.

## Sơ đồ luồng của Mệnh đề if (Flowchart)

![Sơ đồ luồng của Mệnh đề if trong Python](../../../assets/if-else/OIG1.jpg)

## Ví dụ về Mệnh đề if trong Python

Hãy xem xét một ví dụ về một khách hàng có được giảm giá 10% nếu số tiền mua hàng của anh ấy là > 1000; nếu không, thì không có giảm giá nào được áp dụng. Sơ đồ luồng dưới đây cho thấy toàn bộ quá trình ra quyết định.

![Sơ đồ luồng của Mệnh đề if](../../../assets/if-else/OIG1.hwWs.jpg)

Trong Python, trước tiên chúng ta thiết lập một biến giảm giá thành 0 và chấp nhận số tiền làm đầu vào từ người dùng.

Sau đó đến mệnh đề có điều kiện nếu số tiền > 1000. Đặt dấu : bắt đầu khối có điều kiện trong đó giảm giá được tính toán. Rõ ràng, giảm giá hoặc không, câu lệnh tiếp theo mặc định sẽ in số tiền - giảm giá. Nếu áp dụng, nó sẽ được trừ, nếu không, nó là 0.

```python
discount = 0
amount = 1200

# Kiểm tra giá trị số tiền
if amount > 1000:
   discount = amount * 10 / 100

print("amount =", amount - discount)
```

Ở đây số tiền là 1200, do đó giảm giá 120 được trừ. Khi thực thi mã, bạn sẽ nhận được đầu ra sau đây:

```
amount = 1080.0
```

Thay đổi biến amount thành 800 và chạy lại mã. Lần này, không có giảm giá nào được áp dụng. Và, bạn sẽ nhận được đầu ra sau đây:

```
amount = 800
```

Đây là một số ví dụ về cách sử dụng mệnh đề if trong Python để thực hiện các hành động dựa trên điều kiện cụ thể.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*