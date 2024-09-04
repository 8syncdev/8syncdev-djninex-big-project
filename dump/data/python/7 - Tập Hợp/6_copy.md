# Bài 6. Python - Sao Chép Tập Hợp

## Sử Dụng Phương Thức `copy()` để Sao Chép Tập Hợp

Phương thức `copy()` trong lớp set tạo một bản sao sâu của một đối tượng tập hợp.

**Cú Pháp**
```python
set.copy()
```

**Giá Trị Trả Về**
Phương thức `copy()` trả về một tập hợp mới là một bản sao sâu của tập hợp hiện tại.

**Ví dụ**
```python
lang1 = {"C", "C++", "Java", "Python"}
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
lang2 = lang1.copy()
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
lang1.add("PHP")
print ("After updating lang1")
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
```

**Kết Quả**
```
lang1: {'Python', 'Java', 'C', 'C++'} id(lang1): 2451578196864
lang2: {'Python', 'Java', 'C', 'C++'} id(lang2): 2451578197312
After updating lang1
lang1: {'Python', 'C', 'C++', 'PHP', 'Java'} id(lang1): 2451578196864
lang2: {'Python', 'Java', 'C', 'C++'} id(lang2): 2451578197312
```

Trong ví dụ này, chúng ta sao chép `lang1` thành `lang2` bằng cách sử dụng phương thức `copy()`. Sau đó, khi thêm phần tử "PHP" vào `lang1`, `lang2` không bị ảnh hưởng vì chúng là hai tập hợp khác biệt.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*