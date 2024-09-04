# Bài 04. Python - Thư mục

Tất cả các tệp tin được chứa trong các thư mục khác nhau và Python không gặp vấn đề nào khi xử lý chúng. Module os có một số phương thức giúp bạn tạo, xóa và thay đổi các thư mục.

## Phương thức `mkdir()`

Bạn có thể sử dụng phương thức `mkdir()` của module os để tạo thư mục trong thư mục hiện tại. Bạn cần cung cấp một đối số cho phương thức này, chứa tên của thư mục cần tạo.

**Cú Pháp**
```python
os.mkdir("ten_thu_muc_moi")
```

**Ví dụ**

```python
import os

# Tạo một thư mục "test"
os.mkdir("test")
```

## Phương thức `chdir()`

Bạn có thể sử dụng phương thức `chdir()` để thay đổi thư mục hiện tại. Phương thức `chdir()` nhận một đối số, là tên của thư mục mà bạn muốn làm thư mục hiện tại.

**Cú Pháp**
```python
os.chdir("ten_thu_muc")
```

**Ví dụ**

```python
import os

# Thay đổi thư mục thành "/home/newdir"
os.chdir("/home/newdir")
```

## Phương thức `getcwd()`

Phương thức `getcwd()` hiển thị thư mục làm việc hiện tại.

**Cú Pháp**
```python
os.getcwd()
```

**Ví dụ**

```python
import os

# Hiển thị thư mục làm việc hiện tại
os.getcwd()
```

## Phương thức `rmdir()`

Phương thức `rmdir()` xóa thư mục được chuyển làm đối số trong phương thức.

Trước khi xóa một thư mục, tất cả các nội dung trong đó cần được xóa.

**Cú Pháp**
```python
os.rmdir('ten_thu_muc')
```

**Ví dụ**

```python
import os

# Xóa thư mục "/tmp/test"
os.rmdir("/tmp/test")
```