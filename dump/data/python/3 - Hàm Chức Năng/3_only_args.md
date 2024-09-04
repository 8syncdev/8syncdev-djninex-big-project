# Bài 3. Python - Tham số chỉ từ khóa

Bạn có thể sử dụng các biến trong danh sách đối số hình thức như các từ khóa để truyền giá trị. Việc sử dụng các đối số từ khóa là tùy chọn. Nhưng, bạn có thể buộc hàm chỉ nhận các đối số dưới dạng từ khóa. Bạn nên đặt một dấu * trước danh sách các đối số chỉ từ khóa.

Giả sử chúng ta có một hàm với ba đối số, trong đó chúng ta muốn đối số thứ hai và thứ ba chỉ được chấp nhận dưới dạng từ khóa. Để làm điều đó, đặt * sau đối số đầu tiên.

### Ví dụ về Tham số chỉ từ khóa

Hàm print() được tích hợp sẵn là một ví dụ về các đối số chỉ từ khóa. Bạn có thể đưa ra danh sách các biểu thức cần in trong dấu ngoặc đơn. Các giá trị được in sẽ được phân tách bằng một khoảng trắng theo mặc định. Bạn cũng có thể chỉ định bất kỳ ký tự phân tách nào khác thay thế bằng đối số sep.

```python
print("Hello", "World", sep="-")
```

Nó sẽ in ra:

```
Hello-World
```

### Ví dụ: Sử dụng Đối số sep trong phương thức print()

Đối số sep là đối số chỉ từ khóa. Hãy thử sử dụng nó như một đối số không phải từ khóa.

```python
print("Hello", "World", "-")
```

Bạn sẽ nhận được đầu ra khác - không như mong muốn.

```
Hello World -
```

### Ví dụ: Sử dụng Tham số chỉ từ khóa với Phương thức Tự định nghĩa

Trong hàm người dùng đã xác định intr() với hai đối số, amt và rate. Để làm cho đối số rate chỉ dưới dạng từ khóa, đặt "*" trước nó.

```python
def intr(amt, *, rate):
   val = amt * rate / 100
   return val
```

Để gọi hàm này, giá trị cho rate phải được truyền theo từ khóa.

```python
interest = intr(1000, rate=10)
```

Tuy nhiên, nếu bạn cố gắng sử dụng cách gọi hàm mặc định theo vị trí, bạn sẽ nhận được một lỗi.

```python
interest = intr(1000, 10)
# TypeError: intr() takes 1 positional argument but 2 were given
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
