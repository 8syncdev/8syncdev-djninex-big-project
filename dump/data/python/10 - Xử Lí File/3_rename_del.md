# Bài 03. Python - Đổi Tên và Xóa Tệp Tin

Module `os` trong Python cung cấp các phương thức giúp bạn thực hiện các hoạt động xử lý tệp tin như đổi tên và xóa tệp tin.

Để sử dụng module này, bạn cần import nó trước và sau đó bạn có thể gọi bất kỳ hàm liên quan nào.

## Phương thức `rename()`

Phương thức `rename()` nhận hai đối số, tên tệp tin hiện tại và tên tệp tin mới.

**Cú Pháp**
```python
os.rename(ten_tep_hien_tai, ten_tep_moi)
```

**Ví dụ**

```python
import os
# Đổi tên tệp từ "test1.txt" thành "test2.txt"
os.rename("test1.txt", "test2.txt")
```

## Phương thức `remove()`

Bạn có thể sử dụng phương thức `remove()` để xóa tệp tin bằng cách cung cấp tên của tệp tin cần xóa làm đối số.

**Cú Pháp**
```python
os.remove(ten_tep)
```

**Ví dụ**

```python
import os
# Xóa tệp tin "test2.txt"
os.remove("test2.txt")
```