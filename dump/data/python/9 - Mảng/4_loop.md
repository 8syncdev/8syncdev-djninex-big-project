# Bài 04. Python - Lặp qua Mảng

Vì đối tượng mảng hoạt động như một chuỗi, bạn có thể lặp qua các phần tử của nó với sự giúp đỡ của vòng lặp for hoặc while.

## Vòng Lặp "for" với Mảng

Xem ví dụ sau:

```python
import array as arr
a = arr.array('d', [1, 2, 3])
for x in a:
   print (x)
```

Nó sẽ tạo ra kết quả sau:

```
1.0
2.0
3.0
```

## Vòng Lặp "while" với Mảng

Ví dụ sau cho thấy cách bạn có thể lặp qua một mảng bằng cách sử dụng một vòng lặp while:

```python
import array as arr
a = arr.array('d', [1, 2, 3])
l = len(a)
idx =0
while idx<l:
   print (a[idx])
   idx+=1
```

## Vòng Lặp "for" với Chỉ Số của Mảng

Chúng ta có thể tìm độ dài của mảng bằng hàm tích hợp len(). Sử dụng nó để tạo một đối tượng range để có được dãy chỉ số và sau đó truy cập các phần tử của mảng trong một vòng lặp for.

```python
import array as arr
a = arr.array('d', [1, 2, 3])
l = len(a)
for x in range(l):
   print (a[x])
```

Bạn sẽ nhận được cùng một kết quả như trong ví dụ đầu tiên.