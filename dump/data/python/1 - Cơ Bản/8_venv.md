# Bài 08. Python - Môi Trường Ảo

Trong hướng dẫn này, chúng ta sẽ tìm hiểu về các môi trường ảo trong Python và cách tạo và kích hoạt một môi trường ảo để xây dựng một ứng dụng Python.

## Môi Trường Ảo Python

Môi trường ảo Python tạo ra một cài đặt Python ảo bên trong một thư mục dự án. Người dùng sau đó có thể cài đặt và quản lý các gói Python cho mỗi dự án. Điều này cho phép người dùng có thể cài đặt các gói và sửa đổi môi trường Python của họ mà không sợ làm hỏng các gói được cài đặt trong các môi trường khác.

### Môi Trường Ảo trong Python là gì?

Một môi trường ảo Python là:

- Được xem như là một thứ không cần thiết.
- Được sử dụng để chứa một bản cụ thể của trình thông dịch Python và các thư viện và tập lệnh phần mềm cần thiết để hỗ trợ một dự án.
- Được chứa trong một thư mục, thông thường được đặt tên là venv hoặc .venv trong thư mục dự án.
- Không được coi là có thể di chuyển hoặc sao chép.

Khi bạn cài đặt phần mềm Python trên máy tính của mình, nó sẽ có sẵn để sử dụng từ bất kỳ đâu trên hệ thống tệp. Đây là một cài đặt toàn cầu trên toàn hệ thống.

### Tạo Môi Trường Ảo trong Python bằng venv

Chức năng này được hỗ trợ bởi module venv trong bản phân phối Python tiêu chuẩn. Sử dụng các lệnh sau để tạo một môi trường ảo mới.

```bash
C:\Users\Acer>md\pythonapp
C:\Users\Acer>cd\pythonapp
C:\pythonapp>python -m venv myvenv
```

Ở đây, myvenv là thư mục mà một môi trường ảo Python mới sẽ được tạo ra hiển thị các cấu trúc thư mục sau:

```
Directory of C:\pythonapp\myvenv
22-02-2023 09:53 <DIR> .
22-02-2023 09:53 <DIR> ..
22-02-2023 09:53 <DIR> Include
22-02-2023 09:53 <DIR> Lib
22-02-2023 09:53 77 pyvenv.cfg
22-02-2023 09:53 <DIR> Scripts
```

Các tiện ích để kích hoạt và vô hiệu hóa môi trường ảo cũng như bản sao cục bộ của trình thông dịch Python sẽ được đặt trong thư mục Scripts.

```bash
Directory of C:\pythonapp\myvenv\scripts
22-02-2023 09:53 <DIR> .
22-02-2023 09:53 <DIR> ..
22-02-2023 09:53 2,063 activate
22-02-2023 09:53 992 activate.bat
22-02-2023 09:53 19,611 Activate.ps1
22-02-2023 09:53 393 deactivate.bat
22-02-2023 09:53 106,349 pip.exe
22-02-2023 09:53 106,349 pip3.10.exe
22-02-2023 09:53 106,349 pip3.exe
22-02-2023 09:53 242,408 python.exe
22-02-2023 09:53 232,688 pythonw.exe
```

### Kích Hoạt Môi Trường Ảo

Để kích hoạt môi trường ảo mới này, thực hiện activate.bat trong thư mục Scripts.

```bash
(myvenv) C:\pythonapp>
```

Lưu ý tên của môi trường ảo trong dấu ngoặc đơn. Thư mục Scripts chứa bản sao cục bộ của trình thông dịch Python. Bạn có thể bắt đầu một phiên Python trong môi trường ảo này.

### Kiểm Tra xem Python có đang Chạy Bên Trong Một Môi Trường Ảo không?

Để xác nhận liệu phiên Python này có ở trong môi trường ảo hay không, hãy kiểm tra sys.path.

```bash
(myvenv) C:\pythonapp>python
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec 6 2021, 19:10:37) [MSC v.1929
64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Python310\\python310.zip', 'C:\\Python310\\DLLs',
'C:\\Python310\\lib', 'C:\\Python310', 'C:\\pythonapp\\myvenv',
'C:\\pythonapp\\myvenv\\lib\\site-packages']
>>>
```

Thư mục Scripts của môi trường ảo này cũng chứa các tiện ích pip. Nếu bạn cài đặt một gói từ PyPI, gói đó sẽ chỉ hoạt động trong môi trường ảo hiện tại.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*