# Bài 07. Python - Thiết Lập Môi Trường

## Cài Đặt Môi Trường Cục Bộ

Bước đầu tiên trong hành trình học Python là cài đặt nó trên máy tính của bạn. Hiện nay, hầu hết các máy tính, đặc biệt là có hệ điều hành Linux, đã có Python được cài đặt sẵn. Tuy nhiên, có thể nó không phải là phiên bản mới nhất.

Python có sẵn trên nhiều nền tảng khác nhau bao gồm Linux và Mac OS X. Hãy hiểu cách thiết lập môi trường Python của chúng ta.

### Thiết Lập Môi Trường Cục Bộ

Mở một cửa sổ terminal và gõ "python" để tìm hiểu xem nó đã được cài đặt chưa và phiên bản nào đã được cài đặt. Nếu Python đã được cài đặt sẵn thì bạn sẽ nhận được một thông báo giống như sau:

```bash
$ python
Python 3.11.2 (main, Feb 8 2023, 14:49:24) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>>
```

### Tải Về Python

Mã nguồn, nhị phân, tài liệu, tin tức, v.v., mới nhất và hiện tại, đều có sẵn trên trang web chính thức của Python [https://www.python.org/](https://www.python.org/).

Bạn có thể tải về tài liệu Python từ [https://www.python.org/doc/](https://www.python.org/doc/). Tài liệu có sẵn dưới dạng HTML, PDF và PostScript.

### Cài Đặt Python

Phân phối Python có sẵn cho nhiều nền tảng khác nhau. Bạn chỉ cần tải mã nhị phân phù hợp với nền tảng của mình và cài đặt Python.

Nếu mã nhị phân cho nền tảng của bạn không có sẵn, bạn cần một trình biên dịch C để biên dịch mã nguồn thủ công. Việc biên dịch mã nguồn cung cấp nhiều linh hoạt hơn trong việc lựa chọn các tính năng mà bạn cần trong cài đặt của mình.

Dưới đây là một cái nhìn nhanh chóng về cách cài đặt Python trên các nền tảng khác nhau:

#### Cài Đặt Python trên Ubuntu Linux

Để kiểm tra xem Python đã được cài đặt sẵn chưa, mở terminal Linux và nhập lệnh sau:

```bash
$ python3.11 --version
```

Trong Ubuntu Linux, cách dễ nhất để cài đặt Python là sử dụng apt – Công cụ Đóng Gói Nâng Cao. Luôn luôn được khuyến khích cập nhật danh sách các gói trong tất cả các kho lưu trữ được cấu hình.

```bash
$ sudo apt update
```

Ngay cả sau khi cập nhật, phiên bản Python mới nhất có thể không có sẵn để cài đặt, phụ thuộc vào phiên bản Ubuntu bạn đang sử dụng. Để khắc phục điều này, hãy thêm kho deadsnakes.

```bash
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

Cập nhật lại danh sách các gói.

```bash
$ sudo apt update
```

Để cài đặt phiên bản Python 3.11 mới nhất, nhập lệnh sau vào terminal:

```bash
$ sudo apt-get install python3.11
```

Kiểm tra xem nó đã được cài đặt đúng cách chưa.

```bash
$ python3
Python 3.11.2 (main, Feb 8 2023, 14:49:24) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello World")
Hello World
```

### Cài Đặt Python trên các Hệ Điều Hành Khác

#### Cài Đặt Python trên các Hệ Điều Hành Linux/Unix khác

Dưới đây là các bước đơn giản để cài đặt Python trên máy Unix/Linux:

1. Mở trình duyệt Web và truy cập vào [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Theo đường link để tải mã nguồn nén có sẵn cho Unix/Linux.
3. Tải xuống và giải nén các tệp.
4. Chỉnh sửa tệp Modules/Setup nếu bạn muốn tùy chỉnh một số tùy chọn.
5. Bây giờ thực hiện các lệnh sau:

```bash
$ ./configure # chạy tập lệnh configure
$ make # biên dịch mã nguồn
$ make install # cài đặt
```

Điều này cài đặt Python ở vị trí tiêu chuẩn /usr/local/bin và các thư viện của nó ở /usr/local/lib/pythonXX, trong đó XX là phiên bản của Python.

#### Sử Dụng Lệnh Yum

Red Hat Enterprise Linux (RHEL 8) không cài đặt Python 3 theo mặc định. Chúng ta thường sử dụng lệnh yum trên CentOS và các biến thể liên quan khác. Quy trình cài đặt Python-3 trên RHEL 8 như sau:

```bash
$ sudo yum install python3
```

#### Cài Đặt Python trên Windows

Lưu ý rằng Python từ phiên bản 3.10 trở đi không thể cài đặt trên các hệ điều hành Windows 7 hoặc cũ hơn.

Cách khuyến nghị để cài đặt Python là sử dụng trình cài đặt chính thức. Một liên kết đến phiên bản ổn định mới nhất được đưa ra trên trang chủ. Nó cũng được tìm thấy tại [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).

Bạn có thể tìm thấy các gói nhúng và trình cài đặt cho cả kiến trúc 32 và 64 bit.

![](https://www.python.org/static/img/emacs.png)

Hãy tải xuống trình cài đặt 64 bit Windows.

[Double click](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe) vào tệp đã tải xuống để bắt đầu quá trình cài đặt.

Mặc dù bạn có thể tiếp tục bằng cách nhấn nút Cài đặt Ngay bây giờ, nhưng nên chọn thư mục cài đặt với đường dẫn ngắn hơn, và đánh dấu ô kiểm thứ hai để cập nhật biến PATH.

Chấp nhận các giá trị mặc định cho các bước còn lại trong thuật sĩ cài đặt này để hoàn tất quá trình cài đặt.

Mở terminal Command Prompt trên Windows và chạy Python để kiểm tra việc cài đặt đã thành công hay không.

```bash
C:\Users\Acer>python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb 7 2023, 16:38:35) [MSC v.1934
64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Thư viện chuẩn của Python có một mô-đun thực thi được gọi là IDLE – viết tắt của Môi Trường Phát Triển và Học Tập Tích Hợp. Tìm nó từ menu Start của Windows và khởi chạy.

![](https://www.python.org/static/img/pythonwin_screenshot.jpg)

IDLE chứa Python shell (trình thông dịch tương tác) và một trình soạn thảo văn bản đa cửa sổ có thể tùy chỉnh với các tính năng như làm nổi bật cú pháp, lùi thông minh, hoàn thành tự động, v.v. Nó là đa nền tảng nên hoạt động giống nhau trên Windows, MacOS và Linux. Nó cũng có một bộ gỡ lỗi với khả năng đặt điểm dừng, bước tiếp theo và xem các không gian tên toàn cục và cục bộ.

Dưới đây là các bước để cài đặt Python trên máy Windows.

1. Mở trình duyệt Web và truy cập vào [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Theo liên kết cho tệp cài đặt Windows python-XYZ.msi nơi XYZ là phiên bản bạn cần cài đặt.
3. Để sử dụng trình cài đặt python-XYZ.msi này, hệ thống Windows phải hỗ trợ Trình cài đặt Microsoft 2.0. Lưu tệp cài đặt xuống máy cục bộ của bạn và sau đó chạy nó để biết máy của bạn có hỗ trợ MSI hay không.
4. Chạy tệp đã tải xuống. Điều này đưa ra Trình cài đặt Python, rất dễ sử dụng. Chỉ cần chấp nhận các thiết lập mặc định, chờ đợi cho đến khi cài đặt hoàn tất và bạn đã xong.

#### Cài Đặt trên Macintosh

Các máy Mac gần đây đi kèm với Python được cài đặt sẵn, nhưng nó có thể đã cũ vài năm. Truy cập [http://www.python.org/download/mac/](http://www.python.org/download/mac/) để biết hướng dẫn cách lấy phiên bản hiện tại cùng với các công cụ bổ sung để hỗ trợ phát triển trên Mac. Đối với các phiên bản cũ hơn của macOS trước khi Mac OS X 10.3 (phát hành vào năm 2003), có sẵn MacPython.

Jack Jansen duy trì nó và bạn có thể truy cập vào toàn bộ tài liệu tại trang web của anh ấy − [https://github.com/jackjansen](https://github.com/jackjansen). Bạn có thể tìm thấy các thông tin chi tiết về cách cài đặt hoàn chỉnh cho việc cài đặt Mac OS.

### Thiết Lập Biến Môi Trường PATH

Các chương trình và các tệp thực thi khác có thể nằm ở nhiều thư mục khác nhau, vì vậy hệ điều hành cung cấp một đường dẫn tìm kiếm liệt kê các thư mục mà hệ điều hành tìm kiếm các tệp thực thi.

Đường dẫn được lưu trữ trong một biến môi trường, là một chuỗi có tên được duy trì bởi hệ điều hành. Biến này chứa thông tin có sẵn cho bộ nhớ đệm lệnh và các chương trình khác.

Biến đường dẫn được đặt tên là PATH trong Unix hoặc Path trong Windows (Unix phân biệt chữ hoa; Windows không phân biệt chữ hoa).

Trong macOS, trình cài đặt xử lý các chi tiết về đường dẫn. Để gọi trình thông dịch Python từ bất kỳ thư mục cụ thể nào, bạn phải thêm thư mục Python vào đường dẫn của mình.

#### Thiết Lập Đường Dẫn trong Unix/Linux

Để thêm thư mục Python vào đường dẫn cho một phiên trong Unix:

- Trong shell csh − gõ `setenv PATH "$PATH:/usr/local/bin/python"` và nhấn Enter.
- Trong shell bash (Linux) − gõ `export PATH="$PATH:/usr/local/bin/python"` và nhấn Enter.
- Trong shell sh hoặc ksh − gõ `PATH="$PATH:/usr/local/bin/python"` và nhấn Enter.

#### Thiết Lập Đường Dẫn trong Windows

Để thêm thư mục Python vào đường dẫn cho một phiên trong Windows:

- Ở dấu nhắc lệnh − gõ `path %path%;C:\Python` và nhấn Enter.

Biến `PYTHONPATH` có vai trò tương tự như `PATH`. Biến này cho biết trình thông dịch Python nơi nào để đặt các tệp mô-đun được nhập vào một chương trình. Nó nên bao gồm thư viện nguồn Python và các thư mục chứa mã nguồn Python. `PYTHONPATH` đôi khi được thiết lập trước bởi trình cài đặt Python.

Biến `PYTHONSTARTUP` chứa đường dẫn của một tệp khởi tạo chứa mã nguồn Python. Nó được thực thi mỗi khi bạn bắt đầu trình thông dịch. Nó có tên là .pythonrc.py trong Unix và nó chứa các lệnh để tải các tiện ích hoặc sửa đổi `PYTHONPATH`.

Biến `PYTHONCASEOK` được sử dụng trong Windows để hướng dẫn Python tìm kiếm sự phù hợp không phân biệt chữ hoa đầu tiên trong một câu lệnh nhập. Đặt biến này thành bất kỳ giá trị nào để kích hoạt nó.

Biến `PYTHONHOME` là một đường dẫn thư mục mô-đun thay thế. Thông thường nó được nhúng trong các thư mục `PYTHONSTARTUP` hoặc `PYTHONPATH` để làm cho việc chuyển đổi thư viện mô-đun dễ dàng hơn.

### Chạy Python
Có ba cách khác nhau để bắt đầu Python:

#### Trình Thông Dịch Tương Tác

Bạn có thể bắt đầu Python từ Unix, DOS, hoặc bất kỳ hệ thống nào cung cấp cho bạn một bộ thông dịch dòng lệnh hoặc cửa sổ shell.

Nhập `python` vào dòng lệnh để khởi động trình thông dịch tương tác và bắt đầu lập trình Python ngay trên dòng lệnh hoặc cửa sổ shell. 

#### Sử Dụng Môi Trường Phát Triển Thông Dịch (IDE)

Một số môi trường phát triển tích hợp (IDE) như PyCharm, Visual Studio Code, hoặc IDLE (môi trường phát triển Python mặc định) cung cấp giao diện đồ họa cho việc phát triển Python. Bạn có thể bắt đầu một dự án Python mới và viết mã Python trong môi trường IDE một cách thuận tiện.

#### Sử Dụng Jupyter Notebook

Jupyter Notebook là một công cụ phổ biến cho việc phân tích dữ liệu và phát triển Python tương tác. Nó cung cấp một giao diện web cho phép bạn viết và chạy mã Python theo từng phần, cùng với việc chia sẻ mã, kết quả và thông tin bổ sung trong một tài liệu tương tác.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*