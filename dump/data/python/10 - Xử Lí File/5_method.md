# Bài 05. Python - Các Phương Thức File

Một đối tượng tệp tin được tạo bằng cách sử dụng hàm `open()`. Lớp tệp tin định nghĩa các phương thức sau đây để thực hiện các hoạt động IO tệp tin khác nhau. Các phương thức có thể được sử dụng với bất kỳ đối tượng tệp tin nào như luồng byte hoặc luồng mạng.

## Các Phương Thức

1. **`file.close()`**
   - Đóng tệp tin. Một tệp tin đã đóng không thể được đọc hoặc ghi thêm.

2. **`file.flush()`**
   - Xả bộ đệm nội bộ, tương tự như fflush của stdio. Điều này có thể không có tác dụng trên một số đối tượng giống như tệp tin.

3. **`file.fileno()`**
   - Trả về số hiệu tệp nguyên mà được sử dụng bởi triển khai cơ sở để yêu cầu các hoạt động IO từ hệ điều hành.

4. **`file.isatty()`**
   - Trả về True nếu tệp tin được kết nối với một thiết bị tty (giống như), ngược lại trả về False.

5. **`file.next()`**
   - Trả về dòng tiếp theo từ tệp mỗi khi được gọi.

6. **`file.read([size])`**
   - Đọc tối đa size byte từ tệp (ít hơn nếu đọc đến cuối tệp trước khi nhận size byte).

7. **`file.readline([size])`**
   - Đọc một dòng toàn bộ từ tệp. Một ký tự dòng mới dư thừa được giữ trong chuỗi.

8. **`file.readlines([sizehint])`**
   - Đọc đến EOF bằng cách sử dụng readline() và trả về một danh sách chứa các dòng. Nếu đối số sizehint tùy chọn được cung cấp, thay vì đọc đến EOF, các dòng toàn bộ có tổng cộng khoảng sizehint byte (có thể sau khi làm tròn lên đến kích thước bộ đệm nội bộ) được đọc.

9. **`file.seek(offset[, whence])`**
   - Đặt vị trí hiện tại của tệp

10. **`file.tell()`**
    - Trả về vị trí hiện tại của tệp

11. **`file.truncate([size])`**
    - Cắt giảm kích thước của tệp. Nếu đối số size tùy chọn được cung cấp, tệp sẽ được cắt giảm thành (tối đa) kích thước đó.

12. **`file.write(str)`**
    - Ghi một chuỗi vào tệp. Không có giá trị trả về.

13. **`file.writelines(sequence)`**
    - Ghi một chuỗi các dòng vào tệp. Chuỗi có thể là bất kỳ đối tượng lặp lại nào sản xuất chuỗi, thường là một danh sách các chuỗi.