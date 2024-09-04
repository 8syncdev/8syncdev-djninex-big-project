# Bài 10. Python - Phương thức của Danh sách

Trong Python, lớp danh sách bao gồm các phương thức sau mà bạn có thể sử dụng để thêm, cập nhật và xóa các mục trong danh sách:

1. **append(obj)**:
   - Phương thức `append()` thêm một đối tượng `obj` vào cuối danh sách.
   - Cú pháp: `list.append(obj)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   my_list.append(4)
   print(my_list)  # Output: [1, 2, 3, 4]
   ```

2. **clear()**:
   - Phương thức `clear()` xóa tất cả các phần tử trong danh sách, làm cho danh sách trở thành rỗng.
   - Cú pháp: `list.clear()`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   my_list.clear()
   print(my_list)  # Output: []
   ```

3. **copy()**:
   - Phương thức `copy()` tạo và trả về một bản sao của danh sách gốc.
   - Cú pháp: `new_list = list.copy()`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   new_list = my_list.copy()
   print(new_list)  # Output: [1, 2, 3]
   ```

4. **count(obj)**:
   - Phương thức `count()` trả về số lần xuất hiện của đối tượng `obj` trong danh sách.
   - Cú pháp: `count = list.count(obj)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 2, 3, 3, 3]
   count = my_list.count(3)
   print(count)  # Output: 3
   ```

5. **extend(seq)**:
   - Phương thức `extend()` mở rộng danh sách bằng cách thêm các phần tử từ chuỗi hoặc danh sách `seq`.
   - Cú pháp: `list.extend(seq)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   my_list.extend([4, 5])
   print(my_list)  # Output: [1, 2, 3, 4, 5]
   ```

6. **index(obj)**:
   - Phương thức `index()` trả về chỉ mục của lần xuất hiện đầu tiên của đối tượng `obj` trong danh sách.
   - Cú pháp: `index = list.index(obj)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3, 4, 3]
   index = my_list.index(3)
   print(index)  # Output: 2
   ```

7. **insert(index, obj)**:
   - Phương thức `insert()` chèn đối tượng `obj` vào danh sách tại vị trí `index`.
   - Cú pháp: `list.insert(index, obj)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   my_list.insert(1, 4)
   print(my_list)  # Output: [1, 4, 2, 3]
   ```

8. **pop(obj=list[-1])**:
   - Phương thức `pop()` xóa và trả về phần tử cuối cùng trong danh sách hoặc phần tử tại chỉ mục `obj`.
   - Cú pháp: `element = list.pop([obj])`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3]
   last_element = my_list.pop()
   print(last_element)  # Output: 3
   ```

9. **remove(obj)**:
   - Phương thức `remove()` xóa lần xuất hiện đầu tiên của đối tượng `obj` khỏi danh sách.
   - Cú pháp: `list.remove(obj)`
   - Ví dụ:

   ```python
   my_list = [1, 2, 3, 2]
   my_list.remove(2)
   print(my_list)  # Output: [1, 3, 2]
   ```

10. **reverse()**:
    - Phương thức `reverse()` đảo ngược các phần tử trong danh sách.
    - Cú pháp: `list.reverse()`
    - Ví dụ:

    ```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Output: [3, 2, 1]
    ```

11. **sort([func])**:
    - Phương thức `sort()` sắp xếp các phần tử trong danh sách, sử dụng hàm so sánh `func` nếu được chỉ định.
    - Cú pháp: `list.sort([func])`
    - Ví dụ:

    ```python
    my_list = [3, 1, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3]
    ```
 Các phương thức này rất hữu ích để thao tác và xử lý dữ liệu trong danh sách của bạn.

 ## Kết luận

 Việc hiểu và sử dụng các phương thức của lớp danh sách trong Python mang lại nhiều lợi ích quan trọng:

1. **Thêm, xóa và cập nhật dễ dàng**: Các phương thức như `append()`, `insert()`, `pop()`, `remove()` cho phép bạn thêm, xóa và cập nhật các phần tử trong danh sách một cách dễ dàng và linh hoạt.

2. **Sắp xếp và đảo ngược dữ liệu**: Các phương thức `sort()` và `reverse()` cho phép bạn sắp xếp các phần tử trong danh sách theo thứ tự mong muốn hoặc đảo ngược thứ tự của chúng một cách đơn giản.

3. **Tìm kiếm và đếm các phần tử**: Phương thức `index()` cho phép bạn tìm kiếm vị trí của một phần tử trong danh sách, trong khi `count()` cho phép bạn đếm số lần xuất hiện của một phần tử cụ thể.

4. **Tạo bản sao và xóa toàn bộ danh sách**: Các phương thức `copy()` và `clear()` cho phép bạn tạo bản sao của danh sách hoặc xóa toàn bộ nội dung của danh sách một cách dễ dàng.

5. **Kết hợp danh sách**: Phương thức `extend()` cho phép bạn kết hợp hai danh sách lại với nhau một cách thuận tiện và hiệu quả.

6. **Kiểm tra sự tồn tại của phần tử**: Phương thức `in` và `not in` cho phép bạn kiểm tra xem một phần tử có tồn tại trong danh sách hay không.

Tóm lại, việc sử dụng các phương thức của lớp danh sách trong Python giúp bạn thực hiện nhiều thao tác với dữ liệu trong danh sách một cách hiệu quả và linh hoạt, từ thêm, xóa và cập nhật đến sắp xếp, đảo ngược và tìm kiếm.

*Nếu bạn có bất kỳ câu hỏi hoặc cần thêm thông tin, hãy liên hệ với chúng tôi, chúng tôi luôn sẵn sàng giải đáp mọi thắc mắc của bạn! Chúc bạn thành công trong quá trình chinh phục Python!*