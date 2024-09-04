# Bài 8. Python - Vòng lặp For Else

Python hỗ trợ việc sử dụng câu lệnh "else" kết hợp với câu lệnh "for". Nếu câu lệnh "else" được sử dụng với một vòng lặp "for", câu lệnh "else" sẽ được thực thi khi chuỗi đã được duyệt qua trước khi điều khiển chuyển sang dòng lệnh chính.


## Cú pháp của Vòng lặp For Else

Cú pháp sau đây của vòng lặp for với mệnh đề else tùy chọn:

```python
for biến in iterable:
    # các câu lệnh trong vòng lặp
    ...
else:
    # các câu lệnh trong mệnh đề else
    ...
```

## Ví dụ về Vòng lặp For Else

Dưới đây là một ví dụ minh họa sự kết hợp của câu lệnh else với câu lệnh for trong Python. Cho đến khi đếm nhỏ hơn 5, số lần lặp lại được in ra. Khi nó trở thành 5, câu lệnh in trong khối else được thực thi, trước khi điều khiển chuyển sang câu lệnh tiếp theo trong chương trình chính.

```python
for count in range(6):
    print("Lần lặp {}".format(count))
else:
    print("Vòng lặp for đã kết thúc. Bây giờ là trong khối else")
print("Kết thúc vòng lặp for")
```

Kết quả khi chạy mã trên sẽ là:

```
Lần lặp 0
Lần lặp 1
Lần lặp 2
Lần lặp 3
Lần lặp 4
Lần lặp 5
Vòng lặp for đã kết thúc. Bây giờ là trong khối else
Kết thúc vòng lặp for
```

## Kết luận

Với câu lệnh "else" kết hợp với vòng lặp "for" trong Python, bạn có thể thực hiện các hành động bổ sung sau khi vòng lặp kết thúc mà không cần kiểm tra điều kiện. Điều này giúp làm cho mã của bạn trở nên sạch sẽ và dễ hiểu.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*
