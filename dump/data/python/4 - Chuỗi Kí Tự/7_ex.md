# Bài 7. Python - Bài Tập Chuỗi

## Bài Tập 1: Đếm số lượng nguyên âm trong chuỗi

```python
mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count = 0
for x in mystr:
   if x.lower() in vowels:
       count += 1
print("Số lượng nguyên âm:", count)
```

Kết quả:

```
Số lượng nguyên âm: 18
```

## Bài Tập 2: Chuyển chuỗi nhị phân thành số nguyên

```python
mystr = '10101'

def strtoint(mystr):
   for x in mystr:
      if x not in '01':
          return "Lỗi. Chuỗi chứa ký tự không phải nhị phân"
   num = int(mystr, 2)
   return num

print("Nhị phân: {}, Số nguyên: {}".format(mystr, strtoint(mystr)))
```

Kết quả:

```
Nhị phân: 10101, Số nguyên: 21
```

Nếu thay `mystr` thành `'10, 101'`:

```
Nhị phân: 10, 101, Số nguyên: Lỗi. Chuỗi chứa ký tự không phải nhị phân
```

## Bài Tập 3: Loại bỏ tất cả các chữ số từ chuỗi

```python
digits = [str(x) for x in range(10)]
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print(newstr)
```

Kết quả:

```
Hello, Python!
```

## Bài Tập 4: Sắp xếp các ký tự trong chuỗi

## Bài Tập 5: Loại bỏ các ký tự trùng lặp từ chuỗi

## Bài Tập 6: Liệt kê các ký tự duy nhất với số lần xuất hiện của chúng trong chuỗi

## Bài Tập 7: Đếm số từ trong chuỗi

## Bài Tập 8: Loại bỏ tất cả các ký tự không phải chữ cái từ chuỗi

Đây là một số bài tập phổ biến về xử lý chuỗi trong Python. Bạn có thể thực hiện các bài tập này để củng cố kiến thức về xử lý chuỗi và các phương thức chuỗi trong Python.


## Bài Tập 1: Đếm số lượng nguyên âm trong chuỗi

### Giải Pháp:
- Sử dụng một vòng lặp để duyệt qua từng ký tự trong chuỗi.
- Kiểm tra xem ký tự đó có phải là nguyên âm không bằng cách so sánh với danh sách các nguyên âm.
- Tăng biến đếm nếu ký tự là nguyên âm.

## Bài Tập 2: Chuyển chuỗi nhị phân thành số nguyên

### Giải Pháp:
- Kiểm tra từng ký tự trong chuỗi xem có phải là '0' hoặc '1' không.
- Nếu có ký tự nào không phải nhị phân, trả về thông báo lỗi.
- Sử dụng hàm `int(mystr, 2)` để chuyển đổi chuỗi nhị phân thành số nguyên.

## Bài Tập 3: Loại bỏ tất cả các chữ số từ chuỗi

### Giải Pháp:
- Duyệt qua từng ký tự trong chuỗi.
- Nếu ký tự không phải là số, thêm vào danh sách các ký tự mới.
- Cuối cùng, kết hợp danh sách các ký tự mới thành một chuỗi mới.

## Bài Tập 4: Sắp xếp các ký tự trong chuỗi

### Giải Pháp:
- Sử dụng hàm `sorted()` để sắp xếp các ký tự trong chuỗi.
- Hàm này sẽ trả về một danh sách các ký tự đã được sắp xếp.
- Sử dụng `''.join()` để kết hợp các ký tự trong danh sách thành một chuỗi mới.

## Bài Tập 5: Loại bỏ các ký tự trùng lặp từ chuỗi

### Giải Pháp:
- Sử dụng một vòng lặp để duyệt qua từng ký tự trong chuỗi.
- Thêm mỗi ký tự vào một danh sách nếu nó chưa xuất hiện trong danh sách.
- Kết hợp các ký tự trong danh sách thành một chuỗi mới.

## Bài Tập 6: Liệt kê các ký tự duy nhất với số lần xuất hiện của chúng trong chuỗi

### Giải Pháp:
- Sử dụng một từ điển để đếm số lần xuất hiện của mỗi ký tự trong chuỗi.
- Duyệt qua từng ký tự trong chuỗi và cập nhật số lần xuất hiện trong từ điển.
- Cuối cùng, in ra các ký tự duy nhất và số lần xuất hiện của chúng.

## Bài Tập 7: Đếm số từ trong chuỗi

### Giải Pháp:
- Sử dụng phương thức `split()` để tách chuỗi thành danh sách các từ.
- Đếm số phần tử trong danh sách, đó chính là số từ trong chuỗi.

## Bài Tập 8: Loại bỏ tất cả các ký tự không phải chữ cái từ chuỗi

### Giải Pháp:
- Duyệt qua từng ký tự trong chuỗi.
- Nếu ký tự là chữ cái, thêm vào danh sách các ký tự mới.
- Cuối cùng, kết hợp danh sách các ký tự mới thành một chuỗi mới.

Đây là các giải pháp cho mỗi bài tập, mỗi giải pháp cung cấp một cách tiếp cận cụ thể để giải quyết vấn đề.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*