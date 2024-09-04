# Bài 01. Python-  Ghi vào Tệp Trong Python

Để ghi dữ liệu vào một tệp trong Python, bạn cần mở một tệp. Bất kỳ đối tượng nào tương tác với dòng nhập và dòng xuất được gọi là Đối tượng Tệp. Hàm tích hợp open() của Python trả về một đối tượng tệp.

```python
đối_tượng_tệp = open(tên_tệp [, chế_độ_truy_cập][, đệm])
```

## Ghi vào Một Tệp Mới

Sau khi bạn có được đối tượng tệp với hàm open(), bạn có thể sử dụng phương thức write() để ghi bất kỳ chuỗi nào vào tệp được biểu diễn bởi đối tượng tệp. Quan trọng phải lưu ý rằng chuỗi Python có thể chứa dữ liệu nhị phân và không chỉ là văn bản.

Phương thức write() không thêm ký tự xuống dòng ('\n') vào cuối chuỗi.

**Cú pháp**
```python
đối_tượng_tệp.write(chuỗi)
```

Trong đó, tham số truyền vào là nội dung cần được ghi vào tệp đã mở.

**Ví dụ**

```python
# Mở một tệp
fo = open("foo.txt", "w")
fo.write("Python là một ngôn ngữ tuyệt vời.\nYeah, nó thật tuyệt!!\n")

# Đóng tệp đã mở
fo.close()
```

Phương pháp trên sẽ tạo tệp foo.txt và sẽ ghi nội dung đã cho vào tệp đó và cuối cùng nó sẽ đóng tệp đó. Chương trình không hiển thị bất kỳ đầu ra cụ thể nào, tuy nhiên nếu bạn mở tệp này với bất kỳ ứng dụng soạn thảo văn bản nào như Notepad, nó sẽ có nội dung sau đây.

```
Python là một ngôn ngữ tuyệt vời.
Yeah, nó thật tuyệt!!
```

## Ghi vào Một Tệp Mới ở Chế Độ Nhị Phân

Mặc định, các hoạt động đọc/viết trên một đối tượng tệp được thực hiện trên dữ liệu chuỗi văn bản. Nếu chúng ta muốn xử lý các tệp của các loại khác nhau như phương tiện (mp3), các tập tin thực thi (exe), hình ảnh (jpg) vv, chúng ta cần thêm tiền tố 'b' vào chế độ đọc/viết.

Câu lệnh sau sẽ chuyển đổi một chuỗi thành byte và ghi vào một tệp.

```python
f = open('test.bin', 'wb')
dữ_liệu = b"Hello World"
f.write(dữ_liệu)
f.close()
```

Chuyển đổi từ chuỗi văn bản sang byte cũng có thể được thực hiện bằng cách sử dụng hàm encode().

```python
dữ_liệu = "Hello World".encode('utf-8')
```

## Ghi vào Một Tệp Đã Tồn Tại

Khi bất kỳ tệp nào đã tồn tại được mở trong chế độ 'w' để lưu trữ thêm văn bản, nội dung trước đó của nó sẽ bị xóa. Khi một tệp được mở với quyền ghi, nó được xử lý như là một tệp mới. Để thêm dữ liệu vào một tệp đã tồn tại, sử dụng 'a' cho chế độ nối.

**Cú Pháp**
```python
đối_tượng_tệp = open(tên_tệp,"a")
```

**Ví dụ**
```python
# Mở một tệp trong chế độ nối
fo = open("foo.txt", "a")
văn_bản = "TutorialsPoint có một hướng dẫn Python tuyệt vời"
fo.write(văn_bản)

# Đóng tệp đã mở
fo.close()
```

Khi chương trình trên được thực thi, không có đầu ra nào được hiển thị, nhưng một dòng mới được thêm vào foo.txt. Để xác

 minh, hãy mở với một trình soạn thảo văn bản.

```
Python là một ngôn ngữ tuyệt vời.
Yeah, nó thật tuyệt!!
TutorialsPoint có một hướng dẫn Python tuyệt vời
```

## Ghi vào Một Tệp Trong Chế Độ Đọc và Viết

Khi một tệp được mở để ghi (với 'w' hoặc 'a'), không thể thực hiện hoạt động ghi tại bất kỳ vị trí byte nào trước đó trong tệp. Chế độ 'w+' cho phép sử dụng các phương thức write() cũng như read() mà không cần đóng một tệp. Đối tượng Tệp hỗ trợ hàm seek() để tua lại luồng đến bất kỳ vị trí byte nào mong muốn.

Dưới đây là cú pháp cho phương thức seek().

```python
đối_tượng_tệp.seek(vị_trí[, cách])
```

**Tham số**
- **vị_trí**. Đây là vị trí của con trỏ đọc/viết trong tệp.
- **cách**. Đây là tùy chọn và mặc định là 0 nghĩa là vị trí tệp tuyệt đối, các giá trị khác là 1 nghĩa là tua liên quan đến vị trí hiện tại và 2 nghĩa là tua liên quan đến cuối tệp.

Hãy sử dụng phương thức seek() để hiển thị cách thực hiện các hoạt động đọc/viết đồng thời trên một tệp.

**Ví dụ**

Chương trình dưới đây mở tệp trong chế độ w+ (là chế độ đọc-viết), thêm một số dữ liệu. Sau đó nó tìm kiếm một vị trí cụ thể trong tệp và ghi đè nội dung trước đó bằng văn bản mới.

```python
# Mở một tệp trong chế độ đọc-viết
fo = open("foo.txt", "w+")
fo.write("Đây là một cuộc đua chuột")
fo.seek(10, 0)
dữ_liệu = fo.read(3)
fo.seek(10, 0)
fo.write('mèo')
fo.close()
```

**Kết quả**

Nếu chúng ta mở tệp trong chế độ Đọc (hoặc tua về vị trí bắt đầu trong chế độ w+), và đọc nội dung, nó sẽ hiển thị.

```
Đây là một cuộc mèo chuột
```