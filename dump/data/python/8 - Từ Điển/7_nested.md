# Bài 7. Python - Từ Điển Lồng Nhau trong Python

Trong Python, một từ điển được gọi là có cấu trúc lồng nhau nếu giá trị của một hoặc nhiều key là một từ điển khác. Một từ điển lồng nhau thường được sử dụng để lưu trữ một cấu trúc dữ liệu phức tạp.

Đoạn mã sau đại diện cho một từ điển lồng nhau:

```python
marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}
```

**Ví dụ 1:**
Bạn cũng có thể sử dụng một vòng lặp for để duyệt qua từ điển lồng nhau, như trong phần trước.

```python
marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}
for k,v in marklist.items():
   print (k, ":", v)
```

Kết quả:
```
Mahesh : {'Phy': 60, 'maths': 70}
Madhavi : {'phy': 75, 'maths': 68}
Mitchell : {'phy': 67, 'maths': 71}
```

**Ví dụ 2:**
Có thể truy cập giá trị từ một từ điển lồng nhau bằng cách sử dụng [] hoặc phương thức get().

```python
print(marklist.get("Madhavi")['maths'])
obj = marklist['Mahesh']
print(obj.get('Phy'))
print(marklist['Mitchell'].get('maths'))
```

Kết quả:
```
68
60
71
```

Trong ví dụ này, chúng ta truy cập các giá trị từ từ điển lồng nhau bằng cách sử dụng các key và phương thức get().

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*