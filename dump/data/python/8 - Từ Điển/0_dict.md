# Bài 0. Python - Từ Điển (Dictionaries)

Từ điển (dictionary) là một trong những kiểu dữ liệu tích hợp sẵn trong Python. Từ điển trong Python là một ví dụ về kiểu ánh xạ (mapping type). Một đối tượng ánh xạ "ánh xạ" giá trị của một đối tượng khác.

Trong một từ điển ngôn ngữ, chúng ta có các cặp từ và nghĩa tương ứng. Hai phần của cặp là key (từ) và value (nghĩa). Tương tự, từ điển Python cũng là một tập hợp các cặp key:value. Các cặp được phân tách bằng dấu phẩy và đặt trong dấu ngoặc nhọn {}.

Dưới đây là một số ví dụ về các đối tượng từ điển Python:

```python
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
```

**Ví dụ 1**:
Chỉ số, chuỗi hoặc tuple có thể được sử dụng làm key. Tất cả chúng đều là bất biến. Bạn có thể sử dụng một đối tượng của bất kỳ kiểu nào làm value. Vì vậy, các định nghĩa từ điển sau cũng hợp lệ:

```python
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)
```

Kết quả sẽ là:

```
{'Fruit': ['Mango', 'Banana'], 'Flower': ['Rose', 'Lotus']}
{'India, USA': 'Countries', ('New Delhi', 'New York'): 'Capitals'}
```

**Ví dụ 2**:
Python không chấp nhận các đối tượng có thể thay đổi như danh sách (list) làm key, và sẽ gây ra TypeError.

```python
d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
print (d1)
```

Nó sẽ gây ra một TypeError.

**Ví dụ 3**:
Bạn có thể gán một giá trị cho nhiều key trong một từ điển, nhưng một key không thể xuất hiện nhiều hơn một lần trong một từ điển.

```python
d1 = {"Banana":"Fruit", "Rose":"Flower", "Lotus":"Flower", "Mango":"Fruit"}
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d1)
print (d2)
```

Kết quả sẽ là:

```
{'Banana': 'Fruit', 'Rose': 'Flower', 'Lotus': 'Flower', 'Mango': 'Fruit'}
{'Fruit': 'Mango', 'Flower': 'Lotus'}
**Toán tử của Từ Điển trong Python**

Trong Python, các toán tử sau được định nghĩa để sử dụng với các toán hạng từ điển. Trong ví dụ, các đối tượng từ điển sau được sử dụng:

```python
d1 = {'a': 2, 'b': 4, 'c': 30}
d2 = {'a1': 20, 'b1': 40, 'c1': 60}
```

| Toán tử   | Mô tả                              | Ví dụ                                                                               |
| --------- | ---------------------------------- | ----------------------------------------------------------------------------------- |
| dict[key] | Trích xuất/gán giá trị được ánh xạ | `print (d1['b'])` trích xuất giá trị 4, `d1['b'] = 'Z'` gán giá trị mới cho key 'b' |
| dict1     | dict2                              | Hợp của hai đối tượng từ điển, trả về đối tượng mới                                 | `d3=d1 | d2 ; print (d3)` trả về `{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}` |
| dict1     | =dict2                             | Toán tử hợp của từ điển được bổ sung                                                | `d1    | =d2; print (d1)` trả về `{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}` |

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*