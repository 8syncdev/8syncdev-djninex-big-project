# Bài 9. Hàm Built-in Python

Trong phiên bản Python 3.12.2, có tổng cộng 71 hàm Built-in. Dưới đây là danh sách các hàm Built-in cùng với mô tả:

### Hàm Tiêu Biểu:

1. `abs()`: Trả về giá trị tuyệt đối của một số.
2. `all()`: Trả về True khi tất cả các phần tử trong iterable là True.
3. `any()`: Kiểm tra xem có bất kỳ phần tử nào trong iterable nào đó là True không.
4. `bin()`: Chuyển đổi số nguyên thành chuỗi nhị phân.
5. `bool()`: Chuyển đổi một giá trị thành Boolean.
6. `bytes()`: Trả về đối tượng bytes không thay đổi.
7. `callable()`: Kiểm tra xem đối tượng có thể gọi được không.
8. `chr()`: Trả về ký tự từ một số nguyên.
9. `classmethod()`: Trả về phương thức lớp cho hàm đã cho.
10. `compile()`: Trả về một đối tượng mã.
11. `complex()`: Tạo một số phức.
12. `delattr()`: Xóa thuộc tính khỏi đối tượng.
13. `dict()`: Tạo một từ điển.
14. `dir()`: Cố gắng trả về các thuộc tính của đối tượng.
15. `divmod()`: Trả về một bộ chia lấy dư.
16. `enumerate()`: Trả về một đối tượng liệt kê.
17. `eval()`: Chạy mã trong chương trình.
18. `exec()`: Thực thi chương trình được tạo ra động.
19. `filter()`: Xây dựng bộ lặp từ các phần tử đúng.
20. `float()`: Trả về số dấu phẩy động từ số hoặc chuỗi.
21. `format()`: Trả về biểu diễn đã định dạng của một giá trị.
22. `frozenset()`: Trả về đối tượng frozenset không thay đổi.
23. `getattr()`: Trả về giá trị của thuộc tính được đặt tên của một đối tượng.
24. `globals()`: Trả về từ điển của bảng ký hiệu toàn cục hiện tại.
25. `hasattr()`: Trả về xem đối tượng có thuộc tính được đặt tên hay không.
26. `hash()`: Trả về giá trị hash của một đối tượng.
27. `help()`: Kích hoạt Hệ thống Trợ giúp tích hợp.
28. `hex()`: Chuyển đổi số nguyên thành chuỗi thập lục phân.
29. `id()`: Trả về định danh của một đối tượng.
30. `input()`: Đọc và trả về một dòng chuỗi.
31. `int()`: Trả về số nguyên từ một số hoặc chuỗi.
32. `isinstance()`: Kiểm tra xem một đối tượng có phải là một thể hiện của lớp không.
33. `issubclass()`: Kiểm tra xem một lớp có phải là một lớp con của một lớp khác không.
34. `iter()`: Trả về một bộ lặp.
35. `len()`: Trả về độ dài của một đối tượng.
36. `list()`: Tạo một danh sách trong Python.
37. `locals()`: Trả về từ điển của bảng ký hiệu cục bộ hiện tại.
38. `map()`: Áp dụng hàm và trả về một danh sách.
39. `max()`: Trả về phần tử lớn nhất.
40. `memoryview()`: Trả về chế độ xem bộ nhớ của một đối số.
41. `min()`: Trả về giá trị nhỏ nhất.
42. `next()`: Lấy phần tử tiếp theo từ bộ lặp.
43. `object()`: Tạo một đối tượng không đặc điểm.
44. `oct()`: Trả về biểu diễn bát phân của một số nguyên.
45. `open()`: Trả về một đối tượng tệp.
46. `ord()`: Trả về một số nguyên của ký tự Unicode.
47. `pow()`: Trả về lũy thừa của một số.
48. `print()`: In đối tượng đã cho.
49. `property()`: Trả về thuộc tính tài sản.
50. `range()`: Trả về một chuỗi số nguyên.
51. `repr()`: Trả về một biểu diễn in được của đối tượng.
52. `reversed()`: Trả về bộ lặp đảo ngược của một chuỗi.
53. `round()`: Làm tròn một số đến số chữ số thập phân đã chỉ định.
54. `set()`: Xây dựng và trả về một tập hợp.
55. `setattr()`: Đặt giá trị của một thuộc tính của một đối tượng.
56. `slice()`: Trả về một đối tượng lát cắt.
57. `sorted()`: Trả về một danh sách được s

ắp xếp từ iterable đã cho.
58. `staticmethod()`: Biến đổi một phương thức thành một phương thức tĩnh.
59. `str()`: Trả về phiên bản chuỗi của đối tượng.
60. `sum()`: Cộng các mục của một iterable.
61. `super()`: Trả về một đối tượng proxy của lớp cơ sở.
62. `tuple()`: Trả về một tuple.
63. `type()`: Trả về loại của đối tượng.
64. `vars()`: Trả về thuộc tính `__dict__`.
65. `zip()`: Trả về một bộ lặp các tuple.
66. `__import__()`: Hàm được gọi bởi câu lệnh import.

### Các Hàm Toán Học:

Các hàm toán học sau được tích hợp vào trình thông dịch Python, do đó bạn không cần phải nhập chúng từ bất kỳ module nào.

1. `abs()`: Trả về giá trị tuyệt đối của x.
2. `max()`: Trả về phần tử lớn nhất.
3. `min()`: Trả về phần tử nhỏ nhất.
4. `pow()`: Trả về x mũ y, tương đương với x**y, với đối số thứ ba là mod tùy chọn. Nếu được cung cấp, nó trả về giá trị (x**y) % mod.
5. `round()`: Làm tròn x đến n chữ số sau dấu thập phân.
6. `sum()`: Trả về tổng của tất cả các mục số trong bất kỳ iterable nào (list hoặc tuple). Đối số khởi đầu tùy chọn mặc định là 0. Nếu được cung cấp, các số trong danh sách được cộng vào giá trị khởi đầu.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*