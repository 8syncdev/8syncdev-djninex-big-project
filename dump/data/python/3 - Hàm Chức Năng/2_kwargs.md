# Bài 2. Python - Tham số từ khóa

Trong Python, bạn có thể truyền các đối số hàm dưới dạng từ khóa còn được gọi là đối số được đặt tên. Các biến trong định nghĩa hàm được sử dụng như từ khóa. Khi gọi hàm, bạn có thể rõ ràng đề cập đến tên và giá trị của nó.

### Ví dụ về Tham số từ khóa

```python
# Định nghĩa hàm ở đây
def printinfo(name, age):
   "In ra thông tin đã được truyền vào hàm này"
   print("Name: ", name)
   print("Age ", age)
   return

# Bây giờ bạn có thể gọi hàm printinfo
# bằng các đối số vị trí
printinfo("Naveen", 29)

# bằng các đối số từ khóa
printinfo(name="miki", age=30)
```

Kết quả sẽ là:

```
Name: Naveen
Age 29
Name: miki
Age 30
```

Theo mặc định, hàm gán các giá trị cho các đối số theo thứ tự xuất hiện. Trong cuộc gọi hàm thứ hai, chúng ta đã gán giá trị cho một đối số cụ thể.

### Gọi Hàm với Tham số từ khóa

Thay vì truyền các giá trị với các đối số vị trí, hãy gọi hàm với các đối số từ khóa.

### Ví dụ

```python
division(num=10, den=5)
division(den=5, num=10)
```

Kết quả sẽ là:

```
num:10 den:5 quotient:2.0
num:10 den:5 quotient:2.0
```

### Thứ tự của Tham số từ khóa

Khi sử dụng các tham số từ khóa, không cần thiết phải tuân theo thứ tự của các đối số hình thức trong định nghĩa hàm.

Việc sử dụng các tham số từ khóa là tùy chọn. Bạn có thể sử dụng cách gọi kết hợp. Bạn có thể truyền giá trị cho một số đối số mà không cần từ khóa và cho những đối số khác với từ khóa.

Tuy nhiên, các đối số vị trí phải đứng trước các đối số từ khóa khi sử dụng cách gọi kết hợp.

### Thử gọi hàm division() với câu lệnh sau:

```python
def division(num, den):
   quotient = num/den
   print("num:{} den:{} quotient:{}".format(num, den, quotient))

division(num=5, 10)
```

Vì đối số vị trí không thể xuất hiện sau các đối số từ khóa, Python sẽ tạo ra thông báo lỗi như sau:

```
    division(num=5, 10)
                      ^
SyntaxError: non-keyword arg after keyword arg
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*