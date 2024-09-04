# Bài 04. Python - Chương Trình Hello World

Trong hướng dẫn này, chúng ta sẽ học cách viết một chương trình Hello World đơn giản bằng ngôn ngữ lập trình Python. Chương trình này sẽ sử dụng hàm print() tích hợp sẵn trong Python để in ra chuỗi.

## Chương Trình Hello World trong Python

In ra chuỗi "Hello World" là chương trình đầu tiên trong Python. Chương trình này không yêu cầu bất kỳ đầu vào nào từ người dùng, nó chỉ in ra văn bản trên màn hình đầu ra. Nó được sử dụng để kiểm tra xem phần mềm cần thiết để biên dịch và chạy chương trình đã được cài đặt đúng cách hay chưa.

## Các Bước

Dưới đây là các bước để viết một chương trình Python để in ra Hello World:

1. **Cài đặt Python:** Đảm bảo rằng Python đã được cài đặt trên hệ thống của bạn hoặc không. Nếu Python chưa được cài đặt, hãy cài đặt từ đây: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Chọn Trình Soạn Thảo Văn Bản hoặc Môi Trường Phát Triển (IDE) để viết mã.**
3. **Mở Trình Soạn Thảo Văn Bản hoặc IDE, tạo một tệp mới, và viết mã để in ra Hello World.**
4. **Lưu tệp với tên và phần mở rộng ".py".**
5. **Biên dịch/Chạy chương trình.**

## Chương Trình Python để In Ra Hello World

```python
# Mã Python để in ra "Hello World"
print("Hello World")
```

Trong mã trên, chúng ta viết hai dòng. Dòng đầu tiên là bình luận Python sẽ được bỏ qua bởi trình biên dịch Python, và dòng thứ hai là câu lệnh print() sẽ in ra thông điệp được chỉ định ("Hello World") trên màn hình đầu ra.

## Đầu Ra

```
Hello World
```

## Cách Viết và Thực Thi Chương Trình Hello World

### Sử dụng Chế Độ Lệnh Dịch Thông Thường của Python

Rất dễ dàng để hiển thị thông điệp Hello World bằng cách sử dụng trình dịch Python. Khởi chạy trình dịch Python từ một cửa sổ dòng lệnh của Hệ điều hành Windows và gõ lệnh print từ dấu nhắc Python như sau:

**Ví dụ:**

```
PS C:\> python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb 7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello World")
Hello World
```

Tương tự, thông điệp Hello World cũng được in ra trên Hệ điều hành Linux.

**Ví dụ:**

```
$ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello World")
Hello World
```

### Sử dụng Chế Độ Kịch Bản Dịch của Python

Trình dịch Python cũng hoạt động trong chế độ kịch bản. Mở bất kỳ trình soạn thảo văn bản nào, nhập văn bản sau đây và lưu với tên Hello.py

```python
print("Hello World")
```

Đối với Hệ điều hành Windows, mở cửa sổ dòng lệnh (CMD) và chạy chương trình như sau:

```
C:\>python hello.py
```

Điều này sẽ hiển thị đầu ra sau:

```
Hello World
```

Để chạy chương trình từ terminal Linux

```
$ python3 hello.py
```

Điều này sẽ hiển thị đầu ra sau:

```
Hello World
```

### Sử dụng Shebang #! trong Tập Lệnh Linux

Trong Linux, bạn có thể chuyển đổi một chương trình Python thành một tập lệnh tự chạy. Câu lệnh đầu tiên trong mã nên là một dòng Shebang #!. Nó phải chứa đường dẫn đến chương trình Python. Trong Linux, Python được cài đặt trong thư mục /usr/bin, và tên của chương trình thực thi là python3. Do đó, chúng ta thêm câu lệnh này vào tệp hello.py

```python
#!/usr/bin/python3

print("Hello World")
```

Bạn cũng cần cấp quyền thực thi cho tệp bằng cách sử dụng lệnh chmod +x

```
$ chmod +x hello.py
```

Sau đó, bạn có thể chạy chương trình với dòng lệnh sau:

```
$ ./hello.py
```

Điều này sẽ hiển thị đầu ra sau:

```
Hello World
```

## Câu Hỏi Thường Gặp (FAQs)

1. Tại sao chương trình đầu tiên được gọi là Hello World?
   - Đó chỉ là một chương trình đơn giản để kiểm tra cú pháp cơ bản và cấu hình trình biên dịch/phiên dịch của ngôn ngữ lập trình Python.

2. Có cần cài đặt Python để chạy chương trình Hello World không?
   - Có, việc cài đặt Python là cần thiết để chạy chương trình Hello World.

3. Làm thế nào để chạy một chương trình Python mà không cần cài đặt nó?
   - Python đã phát triển một môi trường trực tuyến nơi bạn có thể chạy mã của mình. Bạn có thể sử dụng trình biên dịch trực tuyến của Python để chạy chương trình Python của mình.

4. Sự khác biệt giữa Chương trình Đầu tiên và Chương trình Hello World trong Python là gì?
   - Không có sự khác biệt. Chương trình đầu tiên của Python thường được biết đến là chương trình Hello World.

5. Phương pháp/những phương pháp nào để in ra Hello World hoặc bất kỳ thông điệp nào khác?
   - Bạn có thể sử dụng các phương pháp sau:
     + Phương thức print()
     + Phương thức sys.stdout.write() bằng cách nhập mô-đun sys
     + Sử dụng f-string của Python

Đó là một bản tóm tắt về cách viết và thực thi chương trình Hello World trong Python cùng với một số câu hỏi thường gặp liên quan. Mỗi dòng code mới là một bước tiến mới trên con đường thành thạo Python. Chúc bạn thành công!

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*