# Bài 5. Python - Kết Hợp Các Tập Hợp

## Sử Dụng Toán Tử "|" Để Kết Hợp Các Tập Hợp

Ký hiệu "|" (dấu đường ống) được định nghĩa như là toán tử hợp nhất. Nó thực hiện phép toán A∪B và trả về một tập hợp các phần tử trong A, B hoặc cả hai. Tập hợp không cho phép các phần tử trùng lặp.

**Ví dụ:**
```python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)
```

Kết quả sẽ là:

```
{1, 2, 3, 4, 5, 6, 7, 8}
```

## Sử Dụng Phương Thức `union()` Để Kết Hợp Các Tập Hợp

Lớp set có phương thức union() thực hiện cùng một phép toán như toán tử |. Nó trả về một đối tượng tập hợp chứa tất cả các phần tử trong cả hai tập hợp, loại bỏ các phần tử trùng lặp.

**Ví dụ:**
```python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)
```

## Sử Dụng Phương Thức `update()` Để Kết Hợp Các Tập Hợp

Phương thức update() cũng kết hợp hai tập hợp, nhưng khác với phương thức union(), nó không trả về một đối tượng tập hợp mới. Thay vào đó, các phần tử của tập hợp thứ hai được thêm vào tập hợp đầu tiên, và các phần tử trùng lặp không được phép.

**Ví dụ:**
```python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)
```

## Sử Dụng Toán Tử Unpacking Để Kết Hợp Các Tập Hợp

Trong Python, ký hiệu "*" được sử dụng như là toán tử unpacking. Toán tử unpacking gán mỗi phần tử trong một bộ sưu tập cho một biến riêng biệt.

**Ví dụ:**
```python
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)
```

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*