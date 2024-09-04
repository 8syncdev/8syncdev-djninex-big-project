# Bài 05. Python - Sao Chép Mảng

Các loại chuỗi tích hợp sẵn trong Python như list, tuple và string là các tập hợp được chỉ mục của các mục. Tuy nhiên, khác với các mảng trong C/C++, Java v.v., chúng không đồng nhất, trong ý nghĩa rằng các phần tử trong các loại tập hợp này có thể thuộc các loại khác nhau. Module mảng của Python giúp bạn tạo đối tượng tương tự như các mảng trong Java. Trong chương này, chúng ta sẽ thảo luận về cách sao chép một đối tượng mảng sang một đối tượng khác.

Các mảng Python có thể là chuỗi, số nguyên hoặc số thực. Constructor của lớp mảng được sử dụng như sau:

```python
import array
obj = array.array(typecode[, initializer])
```

typecode có thể là một hằng số ký tự đại diện cho kiểu dữ liệu.

## Sao Chép Mảng Bằng Toán Tử Gán

Chúng ta có thể gán một mảng cho một mảng khác bằng toán tử gán.

### Ví dụ
```python
a = arr.array('i', [1, 2, 3, 4, 5])
b = a.copy()
```

Tuy nhiên, việc gán như vậy không tạo ra một mảng mới trong bộ nhớ. Trong Python, một biến chỉ là một nhãn hoặc tham chiếu đến đối tượng trong bộ nhớ. Vì vậy, a là tham chiếu đến một mảng, và b cũng vậy. Kiểm tra id() của cả a và b. Cùng một giá trị id xác nhận rằng phép gán đơn giản không tạo ra một bản sao.

```python
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = a
print (id(a), id(b))
```

Nó sẽ tạo ra kết quả sau:

```python
2771967068656 2771967068656
```

Bởi vì "a" và "b" trỏ đến cùng một đối tượng mảng, bất kỳ thay đổi nào trong "a" cũng sẽ phản ánh trong "b".

```python
a[2]=10
print (a,b)
```

Nó sẽ tạo ra kết quả sau:

```python
array('i', [1, 2, 10, 4, 5]) array('i', [1, 2, 10, 4, 5])
```

## Sao Chép Mảng Bằng Sao Chép Sâu

Để tạo ra một bản sao vật lý khác của một mảng, chúng ta sử dụng một module khác trong thư viện Python, có tên là copy và sử dụng hàm deepcopy() trong module đó. Một bản sao sâu tạo ra một đối tượng hợp thành mới và sau đó, đệ quy chèn các bản sao vào nó của các đối tượng được tìm thấy trong ban đầu.

### Ví dụ
```python
import array, copy
a = arr.array('i', [1, 2, 3, 4, 5])
b = copy.deepcopy(a)
```

Bây giờ hãy kiểm tra id() của cả "a" và "b". Bạn sẽ thấy các id khác nhau.

```python
print (id(a), id(b))
```

Nó sẽ tạo ra kết quả sau:

```python
2771967069936 2771967068976
```
Điều này chứng minh rằng một đối tượng mới "b" được tạo ra là một bản sao thực sự của "a". Nếu chúng ta thay đổi một phần tử trong "a", nó sẽ không phản ánh trong "b".

```python
a[2]=10
print (a,b)
```

Nó sẽ tạo ra kết quả sau:

```python
array('i', [1, 2, 10, 4, 5]) array('i', [1, 2, 3, 4, 5])
```