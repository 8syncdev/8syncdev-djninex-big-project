# Bài 02. Python - Đọc Tệp Trong Python

Để đọc dữ liệu từ một tệp bằng cách sử dụng mã nguồn trong Python, trước tiên tệp đó phải được mở. Sử dụng hàm tích hợp open() như sau:

```python
đối_tượng_tệp = open(tên_tệp [, chế_độ_truy_cập][, đệm])
```

Dưới đây là chi tiết về các tham số:

- **file_name**: Đối số file_name là một giá trị chuỗi chứa tên của tệp mà bạn muốn truy cập.
- **access_mode**: Tham số access_mode xác định chế độ mà tệp phải được mở, tức là, đọc, viết, thêm, vv. Đây là một tham số tùy chọn và chế độ truy cập tệp mặc định là đọc (r).

Hai câu lệnh sau là tương đương nhau:

```python
fo = open("foo.txt", "r")
fo = open("foo.txt")
```

Để đọc dữ liệu từ tệp đã mở, sử dụng phương thức read() của Đối tượng Tệp. Quan trọng phải lưu ý rằng chuỗi Python có thể chứa dữ liệu nhị phân ngoài dữ liệu văn bản.

**Cú pháp**
```python
đối_tượng_tệp.read([số_lượng])
```

**Tham số**
- **số_lượng**: Số byte cần đọc.

Ở đây, tham số truyền vào là số byte cần đọc từ tệp đã mở. Phương thức này bắt đầu đọc từ đầu của tệp và nếu số_lượng bị thiếu, thì nó cố gắng đọc càng nhiều càng tốt, có thể đến cuối tệp.

**Ví dụ: Đọc Một Tệp Trong Python**
```python
# Mở một tệp
fo = open("foo.txt", "r")
text = fo.read()
print (text)

# Đóng tệp đã mở
fo.close()
```

Kết quả sẽ là:

```
Python is a great language.
Yeah its great!!
```

## Đọc Một Tệp Trong Chế Độ Nhị Phân

Mặc định, các hoạt động đọc/viết trên một đối tượng tệp được thực hiện trên dữ liệu chuỗi văn bản. Nếu chúng ta muốn xử lý các tệp của các loại khác nhau như phương tiện (mp3), các tập tin thực thi (exe), hình ảnh (jpg) vv, chúng ta cần thêm tiền tố 'b' vào chế độ đọc/viết.

Giả sử rằng tệp test.bin đã được viết trước đó với chế độ nhị phân.

```python
f = open('test.bin', 'wb')
data = b"Hello World"
f.write(data)
f.close()
```

**Ví dụ: Đọc Một Tệp Trong Chế Độ Nhị Phân**

Chúng ta cần sử dụng chế độ 'rb' để đọc tệp nhị phân. Giá trị trả về của phương thức read() được giải mã trước khi in ra.

```python
f = open('test.bin', 'rb')
data = f.read()
print(data.decode(encoding='utf-8'))
```

Kết quả sẽ là:

```
Hello World
```

## Đọc Số (Dữ Liệu Kiểu Số Nguyên) Từ Một Tệp

Để viết dữ liệu số nguyên vào một tệp nhị phân, đối tượng số nguyên phải được chuyển đổi thành bytes bằng phương thức to_bytes().

```python
n = 25
n.to_bytes(8, 'big')
f = open('test.bin', 'wb')
data = n.to_bytes(8, 'big')
f.write(data)
```

Để đọc lại từ một tệp nhị phân, chuyển đổi kết quả của hàm read() thành số nguyên bằng cách sử dụng hàm from_bytes().

```python
f = open('test.bin', 'rb')
data = f.read()
n = int.from_bytes(data, 'big')
print(n)
```

## Đọc Số (Dữ Liệu Kiểu Số Thực) Từ Một Tệp

Đối với dữ liệu số thực, chúng ta cần sử dụng module struct từ thư viện chuẩn của Python.

```python
import struct
x = 23.50
data = struct.pack('f', x)
f = open('test.bin', 'wb')
f.write(data)
```

**Ví dụ: Đọc Số Th

ực Từ Một Tệp**

Giải nén chuỗi từ hàm read() để lấy dữ liệu số thực từ tệp nhị phân.

```python
f = open('test.bin', 'rb')
data = f.read()
x = struct.unpack('f', data)
print(x)
```

## Đọc Một Tệp Sử Dụng Chế Độ Đọc-Viết (r+)

Khi một tệp được mở để đọc (với 'r' hoặc 'rb'), không thể ghi dữ liệu vào tệp đó. Chúng ta cần đóng tệp trước khi thực hiện hoạt động khác. Để thực hiện cả hai hoạt động đồng thời, chúng ta phải thêm ký tự '+' vào tham số chế độ. Do đó, chế độ 'w+' hoặc 'r+' cho phép sử dụng cả hai phương thức write() và read() mà không cần đóng tệp.

Đối tượng Tệp cũng hỗ trợ hàm seek() để tua lại dòng để đọc từ bất kỳ vị trí byte mong muốn nào.

Dưới đây là cú pháp cho phương thức seek():

```python
đối_tượng_tệp.seek(vị_trí[, cách])
```

**Tham số**
- **vị_trí**: Đây là vị trí của con trỏ đọc/viết trong tệp.
- **cách**: Đây là tùy chọn và mặc định là 0 nghĩa là vị trí tuyệt đối của tệp, các giá trị khác là 1 nghĩa là tua liên quan đến vị trí hiện tại và 2 nghĩa là tua liên quan đến cuối tệp.

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

Nếu chúng ta mở tệp trong chế độ Đọc (hoặc tua về vị trí bắt đầu trong chế độ w+), và đọc nội dung, nó sẽ hiển thị:

```
Đây là một cuộc mèo chuột
```

Đọc Một Tệp Từ Vị Trí Xác Định
Phương thức seek() đặt vị trí hiện tại của tệp tại offset. Tham số whence là tùy chọn và mặc định là 0, nghĩa là định vị tệp tuyệt đối, các giá trị khác là 1 nghĩa là định vị liên quan đến vị trí hiện tại và 2 nghĩa là định vị liên quan đến cuối tệp.

Không có giá trị trả về. Lưu ý rằng nếu tệp được mở để ghi vào sử dụng 'a' hoặc 'a+', bất kỳ hoạt động seek() nào cũng sẽ bị hủy tại lần ghi tiếp theo.

Nếu tệp chỉ được mở để ghi trong chế độ thêm sử dụng 'a', phương thức này về cơ bản là một hoạt động không có tác dụng, nhưng nó vẫn hữu ích cho các tệp được mở trong chế độ thêm với việc đọc được kích hoạt (chế độ 'a+').

Nếu tệp được mở trong chế độ văn bản sử dụng 't', chỉ các định vị được tr

ả về bởi tell() là hợp lệ. Việc sử dụng các định vị khác gây ra hành vi không xác định.

Lưu ý rằng không phải tất cả các đối tượng tệp đều có thể được tua.

**Cú pháp**

Dưới đây là cú pháp cho phương thức seek():

```python
đối_tượng_tệp.seek(vị_trí[, cách])
```

**Tham số**

- **vị_trí**: Đây là vị trí của con trỏ đọc/viết trong tệp.
- **cách**: Đây là tùy chọn và mặc định là 0 nghĩa là vị trí tuyệt đối của tệp, các giá trị khác là 1 nghĩa là tua liên quan đến vị trí hiện tại và 2 nghĩa là tua liên quan đến cuối tệp.

**Ví dụ**

Dưới đây là chương trình mở tệp trong chế độ w+ (là chế độ đọc-viết), thêm một số dữ liệu. Sau đó nó tìm kiếm một vị trí cụ thể trong tệp và ghi đè nội dung trước đó bằng văn bản mới.

```python
# Mở một tệp trong chế độ đọc-viết
fo = open("foo.txt", "w+")
fo.write("Đây là một cuộc đua chuột")
fo.seek(10, 0)
dữ_liệu = fo.read(3)
fo.seek(10, 0)
fo.write('mèo')
fo.seek(0, 0)
dữ_liệu = fo.read()
print(dữ_liệu)
fo.close()
```

**Kết quả**

```
Đây là một cuộc mèo chuột
```

# Kết Luận

Thông qua các ví dụ và giải thích chi tiết, bạn đã học cách đọc dữ liệu từ một tệp trong Python, bao gồm cả chế độ văn bản và chế độ nhị phân, cũng như cách xử lý số nguyên và số thực. Bạn cũng đã hiểu về cách thực hiện các hoạt động đọc và viết đồng thời trên một tệp bằng cách sử dụng chế độ 'r+' hoặc 'w+'.