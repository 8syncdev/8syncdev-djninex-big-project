# Bài 11. Python pass Statement

Câu lệnh `pass` trong Python được sử dụng khi một câu lệnh được yêu cầu cú pháp nhưng bạn không muốn bất kỳ lệnh hoặc mã nào được thực thi.

Đây là một phép thực thi trống; không có gì xảy ra khi nó được thực thi. Câu lệnh `pass` trong Python cũng hữu ích ở những nơi mà mã của bạn sẽ cuối cùng đi, nhưng chưa được viết, tức là, trong các phần còn thiếu.

### Cú pháp của câu lệnh pass

```python
pass
```

### Ví dụ về câu lệnh pass

Đoạn mã dưới đây cho thấy cách bạn có thể sử dụng câu lệnh pass trong Python:

```python
for letter in 'Python':
   if letter == 'h':
      pass
      print ('Đây là khối pass')
   print ('Chữ hiện tại :', letter)
print ("Tạm biệt!")
```

Khi mã trên được thực thi, nó sẽ tạo ra kết quả sau:

```
Chữ hiện tại : P
Chữ hiện tại : y
Chữ hiện tại : t
Đây là khối pass
Chữ hiện tại : h
Chữ hiện tại : o
Chữ hiện tại : n
Tạm biệt!
```

### Vòng lặp vô hạn đơn giản với câu lệnh pass

Điều này đơn giản đủ để tạo ra một vòng lặp vô hạn bằng câu lệnh pass. Ví dụ, nếu bạn muốn viết một vòng lặp vô hạn mà không làm gì cả, hãy làm điều đó bằng một pass.

#### Ví dụ

```python
while True: pass                  # Nhấn Ctrl-C để dừng
```

Vì thân của vòng lặp chỉ là một câu lệnh trống, Python bị kẹt trong vòng lặp này. Như đã giải thích trước đó, pass là gần như với các câu lệnh như None là với các đối tượng — một điều rõ ràng không làm gì cả.

### Sử dụng dấu ba chấm ... làm lựa chọn thay thế cho câu lệnh pass

Python 3.X cho phép sử dụng dấu ba chấm được mã hóa dưới dạng ba dấu chấm liên tiếp `...` để thay thế cho câu lệnh pass. Dấu ba chấm này có thể phục vụ như một lựa chọn cho câu lệnh pass.

#### Ví dụ

Ví dụ, nếu chúng ta tạo một hàm không làm gì đặc biệt để mã sau này điền vào, thì chúng ta có thể sử dụng `...`:

```python
def func1():
    ...                   # Thay thế cho pass

def func2(): ...          # Hoạt động trên cùng một dòng

func1()                   # Không làm gì nếu được gọi
func2()                   # Không làm gì nếu được gọi
```

Câu lệnh trên khi được gọi không làm gì cả.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*