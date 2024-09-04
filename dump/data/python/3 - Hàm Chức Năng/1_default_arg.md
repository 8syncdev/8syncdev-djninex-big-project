# Bài 1. Python - Tham số Mặc định

Trong Python, bạn có thể định nghĩa một hàm với giá trị mặc định được gán cho một hoặc nhiều đối số hình thức. Python sử dụng giá trị mặc định cho đối số đó nếu không có giá trị nào được truyền vào. Nếu có bất kỳ giá trị nào được truyền, giá trị mặc định sẽ bị ghi đè bằng giá trị thực tế được truyền vào.

Tham số mặc định trong Python là các đối số hàm sẽ được sử dụng nếu không có đối số nào được truyền vào cuộc gọi hàm.
Ví dụ về Tham số Mặc định
```python
# Định nghĩa hàm ở đây
def printinfo(name, age=35):
   "In ra thông tin đã được truyền vào hàm này"
   print("Name: ", name)
   print("Age ", age)
   return

# Bây giờ bạn có thể gọi hàm printinfo
printinfo(age=50, name="miki")
printinfo(name="miki")
```
Kết quả sẽ là:

```
Name: miki
Age 50
Name: miki
Age 35
```
Trong ví dụ trên, cuộc gọi thứ hai đến hàm không truyền giá trị cho đối số tuổi (age), do đó giá trị mặc định của nó là 35.

Hãy xem một ví dụ khác trong đó gán giá trị mặc định cho một đối số hàm. Hàm percent() được định nghĩa như sau:

```python
def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val
```
Giả sử điểm cho mỗi môn là trên 100, đối số maxmarks được thiết lập là 200. Do đó, chúng ta có thể bỏ qua giá trị của đối số thứ ba khi gọi hàm percent().

```python
phy = 60
maths = 70
result = percent(phy, maths)
```

Tuy nhiên, nếu số điểm tối đa cho mỗi môn không phải là 100, chúng ta cần đưa ra đối số thứ ba khi gọi hàm percent().

```python
phy = 40
maths = 46
result = percent(phy, maths, 100)
```

### Ví dụ: Gọi Hàm Không Sử Dụng Tham số Từ Khóa

Dưới đây là ví dụ hoàn chỉnh:

```python
def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val

phy = 60
maths = 70
result = percent(phy, maths)
print("Phần trăm:", result)

phy = 40
maths = 46
result = percent(phy, maths, 100)
print("Phần trăm:", result)
```

Kết quả sẽ là:

```
Phần trăm: 65.0
Phần trăm: 86.0
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
