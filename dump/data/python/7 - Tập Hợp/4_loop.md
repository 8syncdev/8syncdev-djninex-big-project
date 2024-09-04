# Bài 4. Python - Lặp Qua Tập Hợp

## Lặp Qua Các Phần Tử của Tập Hợp

Tập hợp trong Python không phải là một chuỗi, cũng không phải là một lớp kiểu ánh xạ. Do đó, các đối tượng trong một tập hợp không thể được duyệt bằng chỉ số hoặc khóa. Tuy nhiên, bạn có thể duyệt qua từng phần tử trong một tập hợp bằng cách sử dụng một vòng lặp for.

**Ví dụ:**
```python
langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print (lang)
```

Kết quả sẽ là:

```
C
Python
C++
Java
```

## Lặp Qua Các Phần Tử của Tập Hợp với Phương Thức `add()`

Dưới đây là ví dụ về cách chạy một vòng lặp for qua các phần tử của một tập hợp và sử dụng phương thức `add()` của lớp set để thêm vào một tập hợp khác.

**Ví dụ:**
```python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
for x in s2:
   s1.add(x)
print (s1)
```

Kết quả sẽ là:

```
{1, 2, 3, 4, 5, 6, 7, 8}
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*