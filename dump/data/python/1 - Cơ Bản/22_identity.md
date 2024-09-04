# Bài 22. Python - Toán Tử Nhận Dạng

Toán tử nhận dạng trong Python so sánh các đối tượng để xác định liệu chúng có chia sẻ cùng một bộ nhớ và tham chiếu đến cùng một loại đối tượng (kiểu dữ liệu) hay không.

### Toán Tử 'is'

Toán tử 'is' trả về True nếu cả hai đối tượng của toán hạng chia sẻ cùng một vị trí bộ nhớ. Vị trí bộ nhớ của đối tượng có thể được lấy thông qua hàm "id()". Nếu "id()" của cả hai biến giống nhau, toán tử "is" trả về True.

#### Ví dụ về Toán Tử 'is'

```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# So sánh và in giá trị trả về
print(a is c)
print(a is b)

# In các ID của a, b, và c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))
```

Kết quả sẽ là:

```
True
False
id(a) :  140114091859456
id(b) :  140114091906944
id(c) :  140114091859456
```

### Toán Tử 'is not'

Toán tử 'is not' trả về True nếu cả hai đối tượng của toán hạng không chia sẻ cùng một vị trí bộ nhớ hoặc cả hai toán hạng không phải là cùng một đối tượng.

#### Ví dụ về Toán Tử 'is not'

```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# So sánh và in giá trị trả về
print(a is not c)
print(a is not b)

# In các ID của a, b, và c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))
```

Kết quả sẽ là:

```
False
True
id(a) :  140559927442176
id(b) :  140559925598080
id(c) :  140559927442176
```

### Ví dụ với Giải Thích

#### Ví dụ 1

```python
a="8 Sync Dev"
b=a
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)
```

Kết quả sẽ là:

```
id(a), id(b): 2739311598832 2739311598832
a is b: True
b is not a: False
```

Trong trường hợp các đối tượng là các danh sách và bộ dữ liệu, chúng có cách hoạt động khác nhau, điều này có thể nhìn lạ trong trường hợp đầu tiên. Trong ví dụ dưới đây, hai danh sách "a" và "b" chứa các mục giống nhau. Nhưng id() của chúng khác nhau.

#### Ví dụ 2

```python
a=[1,2,3]
b=[1,2,3]
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)
```

Kết quả sẽ là:

```
id(a), id(b): 1552612704640 1552567805568
a is b: False
b is not a: True
```

Các đối tượng danh sách hoặc bộ dữ liệu chỉ chứa các vị trí bộ nhớ của các mục riêng lẻ và không phải là các mục đó. Do đó, "a" chứa các địa chỉ của các đối tượng số nguyên 10, 20 và 30 ở một vị trí nhất định có thể khác nhau so với "b".

#### Ví dụ 3

```python
print (id(a[0]), id(a[1]), id(a[2]))
print (id(b[0]), id(b[1]), id(b[2]))
```

Kết quả sẽ là:

```
140734682034984 140734682035016 140734682035048
140734682034984 140734682035016 140734682035048
```

Vì vị trí khác biệt của "a" và "b", toán tử "is" trả về False ngay cả khi hai danh sách chứa cùng các số giống nhau.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
