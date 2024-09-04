# Bài 7. Python - Toán Tử Tập Hợp

## Toán Tử Hợp (Union) Tập Hợp Python (|)

Hợp của hai tập hợp là một tập hợp chứa tất cả các phần tử nằm trong A hoặc trong B hoặc cả hai. Ví dụ:

{1,2}∪{2,3}={1,2,3}

Python sử dụng ký hiệu "|" như là toán tử hợp. Ví dụ sau sử dụng toán tử "|" và trả về hợp của hai tập hợp.

**Ví dụ**
```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 | s2
print ("Hợp của s1 và s2: ", s3)
```

**Kết Quả**
```
Hợp của s1 và s2: {1, 2, 3, 4, 5, 6, 7, 8}
```

## Toán Tử Giao (Intersection) Tập Hợp Python (&)

Giao của hai tập hợp AA và BB, được ký hiệu bởi A∩B, bao gồm tất cả các phần tử đồng thời thuộc A và B. Ví dụ:

{1,2}∩{2,3}={2}

Python sử dụng ký hiệu "&" như là toán tử giao. Ví dụ sau sử dụng toán tử "&" và trả về giao của hai tập hợp.

**Ví dụ**
```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 & s2
print ("Giao của s1 và s2: ", s3)
```

**Kết Quả**
```
Giao của s1 và s2: {4, 5}
```

## Toán Tử Hiệu (Difference) Tập Hợp Python (-)

Hiệu (hoặc sự trừ) được định nghĩa như sau. Tập A−B bao gồm các phần tử thuộc A nhưng không thuộc B. Ví dụ:

Nếu A={1,2,3} và B={3,5}, thì A−B={1,2}

Python sử dụng ký hiệu "-" như là toán tử hiệu.

**Ví dụ**
```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 - s2
print ("Hiệu của s1 - s2: ", s3)
s3 = s2 - s1
print ("Hiệu của s2 - s1: ", s3)
```

**Kết Quả**
```
Hiệu của s1 - s2: {1, 2, 3}
Hiệu của s2 - s1: {8, 6, 7}
```

## Toán Tử Hiệu Đối Xứng (Symmetric Difference) Tập Hợp Python (^)

Hiệu đối xứng của A và B được ký hiệu là "A Δ B" và được định nghĩa bởi

A Δ B = (A − B) ⋃ (B − A)

Python sử dụng ký hiệu "^" như là toán tử hiệu đối xứng.

**Ví dụ**
```python
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 - s2
print ("Hiệu của s1 - s2: ", s3)
s3 = s2 - s1
print ("Hiệu của s2 - s1: ", s3)
s3 = s1 ^ s2
print ("Hiệu Đối Xứng trong s1 và s2: ", s3)
```

**Kết Quả**
```
Hiệu của s1 - s2: {1, 2, 3}
Hiệu của s2 - s1: {8, 6, 7}
Hiệu Đối Xứng trong s1 và s2: {1, 2, 3, 6, 7, 8}
```
*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*