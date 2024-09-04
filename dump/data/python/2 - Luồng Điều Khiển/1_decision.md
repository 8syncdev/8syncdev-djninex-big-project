# Bài 1. Python - Ra Quyết Định

Trong Python, khả năng ra quyết định được thực hiện thông qua các từ khóa if..elif...else. Từ khóa if yêu cầu một biểu thức boolean, theo sau bởi dấu hai chấm (:) để bắt đầu một khối được thụt vào. Các câu lệnh có cùng mức thụt vào sẽ được thực thi nếu biểu thức boolean trong câu lệnh if là Đúng. Nếu biểu thức không Đúng (False), trình thông dịch sẽ bỏ qua khối được thụt vào và tiếp tục thực thi các câu lệnh ở mức thụt vào trước đó.

Cấu trúc quyết định đánh giá nhiều biểu thức, tạo ra Kết quả TRUE hoặc FALSE. Bạn cần xác định hành động nào cần thực hiện và các câu lệnh nào sẽ được thực thi nếu Kết quả là TRUE hoặc FALSE.


Ngôn ngữ lập trình Python giả định bất kỳ giá trị không bằng không và không rỗng như TRUE, và nếu nó là không hoặc null, thì nó được giả định là giá trị FALSE.

Ngôn ngữ lập trình Python cung cấp các loại câu lệnh ra quyết định sau đây. Nhấp vào các liên kết sau đây để kiểm tra chi tiết của chúng.

**1.** Câu lệnh if

   Một câu lệnh if bao gồm một biểu thức boolean theo sau là một hoặc nhiều câu lệnh.

**2.** Câu lệnh if...else

   Một câu lệnh if có thể được theo sau bởi một câu lệnh else tùy chọn, thực thi khi biểu thức boolean là FALSE.

**3.** Câu lệnh if lồng nhau

   Bạn có thể sử dụng một câu lệnh if hoặc else if bên trong một câu lệnh if hoặc else if(s).

Hãy đi qua từng câu lệnh ra quyết định một cách ngắn gọn.

### Các Khối Mã Đơn

Nếu khối mã của một mệnh đề if chỉ bao gồm một dòng duy nhất, nó có thể được viết trên cùng một dòng với câu lệnh tiêu đề.

Dưới đây là một ví dụ về mệnh đề if trên một dòng:

```python
#!/usr/bin/python

var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")
```

Khi mã trên được thực thi, nó sẽ tạo ra kết quả sau:

```
Value of expression is 100
Good bye!
```

Đây là cách Python thực hiện ra quyết định trong các chương trình của mình. Các câu lệnh ra quyết định giúp chương trình lựa chọn hành động dựa trên các điều kiện cụ thể và là một phần quan trọng của việc kiểm soát luồng của chương trình.

Dưới đây là một ví dụ minh họa về cách sử dụng câu lệnh if để quyết định hành động dựa trên một biểu thức boolean:

```python
# Kiểm tra điểm số và in ra kết quả dựa trên điều kiện
marks = 80

if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print("Result:", result)
```

Kết quả sẽ là:

```
Result: Passed with distinction
```

Dưới đây là một ví dụ sử dụng câu lệnh if...else để xác định xem một ký tự là nguyên âm hay không:

```python
# Kiểm tra xem ký tự có phải là nguyên âm không
def checkVowel(character):
    if character in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel alphabet"
    else:
        return "Not a vowel alphabet"

print(checkVowel('a'))  # Kết quả: Vowel alphabet
print(checkVowel('b'))  # Kết quả: Not a vowel alphabet
```

Dưới đây là một ví dụ sử dụng câu lệnh if lồng nhau để kiểm tra số lớn nhất trong ba số:

```python
# Tìm số lớn nhất trong ba số
num1 = 10
num2 = 20
num3 = 15

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print("Largest number is:", largest)
```

Kết quả sẽ là:

```
Largest number is: 20
```

Như vậy, đây là một số ví dụ về cách sử dụng câu lệnh ra quyết định trong Python để thực hiện các hành động dựa trên điều kiện cụ thể.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
