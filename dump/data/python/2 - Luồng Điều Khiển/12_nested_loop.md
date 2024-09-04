# Bài 12. Python Nested Loops

Trong Python, khi bạn viết một hoặc nhiều vòng lặp trong một câu lệnh vòng lặp đó được gọi là vòng lặp lồng nhau. Vòng lặp chính được coi là vòng lặp bên ngoài và các vòng lặp bên trong vòng lặp bên ngoài được gọi là các vòng lặp bên trong.

Ngôn ngữ lập trình Python cho phép sử dụng một vòng lặp bên trong một vòng lặp khác. Phần sau sẽ mô tả một số ví dụ để minh họa khái niệm vòng lặp lồng nhau với vòng lặp for và vòng lặp while.

## Python Nested for Loop

Vòng lặp for có một hoặc nhiều vòng lặp for bên trong được gọi là vòng lặp for lồng nhau.

### Cú pháp vòng lặp for lồng nhau trong Python

Cú pháp cho câu lệnh vòng lặp for lồng nhau trong ngôn ngữ lập trình Python như sau:

```python
for biến_lặp_ngoài in chuỗi:
   for biến_lặp_trong in chuỗi:
      câu_lệnh(s)
   câu_lệnh(s)
```

### Ví dụ về vòng lặp for lồng nhau trong Python

Chương trình sau sử dụng một vòng lặp for lồng nhau để tìm các số nguyên tố từ 2 đến 100:

```python
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]

for x in months:
  for y in days:
    print(x, y)

print("Good bye!")
```

Khi mã trên được thực thi, nó tạo ra kết quả như sau:

```
('jan', 'sun')
('jan', 'mon')
('jan', 'tue')
('feb', 'sun')
('feb', 'mon')
('feb', 'tue')
('mar', 'sun')
('mar', 'mon')
('mar', 'tue')
Good bye!
```

## Python Nested while Loop

Vòng lặp while có một hoặc nhiều vòng lặp while bên trong được gọi là vòng lặp while lồng nhau.

### Cú pháp vòng lặp while lồng nhau trong Python

Cú pháp cho câu lệnh vòng lặp while lồng nhau trong ngôn ngữ lập trình Python như sau:

```python
while biểu_thức:
   while biểu_thức:
      câu_lệnh(s)
   câu_lệnh(s)
```

Một lưu ý cuối cùng về việc lồng nhau các vòng lặp là bạn có thể đặt bất kỳ loại vòng lặp nào bên trong bất kỳ loại vòng lặp nào khác. Ví dụ, một vòng lặp for có thể nằm trong một vòng lặp while hoặc ngược lại.

### Ví dụ về vòng lặp while lồng nhau trong Python

Chương trình sau sử dụng một vòng lặp while lồng nhau để tìm các số nguyên tố từ 2 đến 100:

```python
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j):
      print(i, " is prime")
   i = i + 1

print("Good bye!")
```

Khi mã trên được thực thi, nó tạo ra kết quả như sau:

```
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime
43 is prime
47 is prime
53 is prime
59 is prime
61 is prime
67 is prime
71 is prime
73 is prime
79 is prime
83 is prime
89 is prime
97 is prime
Good bye!
```

Đó là một bài toán phổ biến khi học về vòng lặp lồng nhau trong Python. 

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*