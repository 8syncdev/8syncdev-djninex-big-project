# Bài 3. Python - Ghép Chuỗi trong Python

Toán tử "+" được biết đến như một toán tử cộng, trả về tổng của hai số. Tuy nhiên, ký hiệu "+" hoạt động như một toán tử ghép chuỗi trong Python. Nó hoạt động với hai toán hạng chuỗi và kết quả là sự ghép nối của hai chuỗi.

Các ký tự của chuỗi bên phải của ký hiệu cộng được nối vào chuỗi bên trái của nó. Kết quả của việc ghép nối là một chuỗi mới.

**Ví dụ**

```python
str1 = "Hello"
str2 = "World"
print("Chuỗi 1:", str1)
print("Chuỗi 2:", str2)
str3 = str1 + str2
print("Chuỗi 3:", str3)
```

Kết quả sẽ là:

```
Chuỗi 1: Hello
Chuỗi 2: World
Chuỗi 3: HelloWorld
```

## Chèn Khoảng Trắng Giữa Hai Chuỗi Đã Ghép

Để chèn một khoảng trắng giữa hai chuỗi, sử dụng một chuỗi trống thứ ba.

**Ví dụ**

```python
str1 = "Hello"
str2 = "World"
khoang_trang = " "
print("Chuỗi 1:", str1)
print("Chuỗi 2:", str2)
str3 = str1 + khoang_trang + str2
print("Chuỗi 3:", str3)
```

Kết quả sẽ là:

```
Chuỗi 1: Hello
Chuỗi 2: World
Chuỗi 3: Hello World
```

## Ghép Chuỗi Bằng Cách Nhân

Ký hiệu "*", mà chúng ta thường sử dụng để nhân hai số, cũng có thể được sử dụng với các toán hạng chuỗi. Ở đây, "*" hoạt động như một toán tử lặp lại trong Python. Một trong các toán hạng phải là một số nguyên và thứ hai là một chuỗi. Toán tử nối nhiều bản sao của chuỗi lại với nhau. Ví dụ −

**Ví dụ**

```python
>>> "Hello" * 3
'HelloHelloHello'
```

Toán hạng số nguyên là số bản sao của toán hạng chuỗi để được nối.

## Ghép Chuỗi Với Các Toán Tử '+' và '*'

Cả hai toán tử chuỗi, (*) toán tử lặp lại và (+) toán tử ghép chuỗi, có thể được sử dụng trong một biểu thức duy nhất. Toán tử "*" có độ ưu tiên cao hơn toán tử "+".

**Ví dụ**

```python
str1 = "Hello"
str2 = "World"
print("Chuỗi 1:", str1)
print("Chuỗi 2:", str2)
str3 = str1 + str2 * 3
print("Chuỗi 3:", str3)
str4 = (str1 + str2) * 3
print("Chuỗi 4:", str4)
```

Để tạo chuỗi str3, Python ghép 3 bản sao của World trước, và sau đó nối kết quả vào Hello

```
Chuỗi 3: HelloWorldWorldWorld
```

Trong trường hợp thứ hai, các chuỗi str1 và str2 được đặt trong dấu ngoặc đơn, do đó việc ghép của chúng diễn ra trước. Kết quả của nó sau đó được lặp lại ba lần.

```
Chuỗi 4: HelloWorldHelloWorldHelloWorld
```

Ngoài "+" và "*", không có ký hiệu toán hạng số học nào khác có thể được sử dụng với các toán hạng chuỗi.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*