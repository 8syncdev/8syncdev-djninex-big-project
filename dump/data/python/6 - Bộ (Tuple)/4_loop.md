# Bài 4. Python - Lặp Qua Các Phần Tử của Tuple trong Python

Trong Python, bạn có thể duyệt qua các phần tử của một tuple bằng cách sử dụng vòng lặp `for`. Việc duyệt này có thể thực hiện bằng cách sử dụng tuple chính nó như một trình lặp hoặc với sự trợ giúp của một chỉ mục.

## Ví dụ

Dưới đây là một ví dụ đơn giản về cách sử dụng vòng lặp `for` trong Python:

```python
tup1 = (25, 12, 10, -21, 10, 100)
for num in tup1:
    print(num, end=' ')
# Output: 25 12 10 -21 10 100
```

Trong ví dụ trên, chúng ta duyệt qua mỗi phần tử trong tuple `tup1` và in ra giá trị của từng phần tử.

## Lặp Qua Các Phần Tử của Tuple sử Dụng Chỉ Mục

Ngoài việc sử dụng vòng lặp trực tiếp, bạn cũng có thể duyệt qua các phần tử của một tuple bằng cách sử dụng chỉ mục của chúng.

### Ví dụ

```python
tup1 = (25, 12, 10, -21, 10, 100)
indices = range(len(tup1))
for i in indices:
    print("tup1[{}]: ".format(i), tup1[i])
# Output:
# tup1[0]: 25
# tup1[1]: 12
# tup1[2]: 10
# tup1[3]: -21
# tup1[4]: 10
# tup1[5]: 100
```

Trong ví dụ này, chúng ta duyệt qua các phần tử của tuple `tup1` bằng cách sử dụng chỉ mục và in ra mỗi phần tử cùng với chỉ mục tương ứng của nó.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*