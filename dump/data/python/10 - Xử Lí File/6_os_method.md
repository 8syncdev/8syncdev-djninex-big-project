# Bài 06. Python OS - Các Phương Thức File/Thư Mục

Module os trong Python cung cấp một loạt các phương thức hữu ích để thao tác với tệp tin và thư mục. Dưới đây là danh sách các phương thức hữu ích nhất:

## Các Phương Thức với Mô Tả

1. **`os.access(path, mode)`**
   - Sử dụng uid/gid thực để kiểm tra quyền truy cập vào path.

2. **`os.chdir(path)`**
   - Thay đổi thư mục làm việc hiện tại thành path.

3. **`os.chflags(path, flags)`**
   - Đặt cờ của path thành các cờ số.

4. **`os.chmod(path, mode)`**
   - Thay đổi chế độ của path thành chế độ số.

5. **`os.chown(path, uid, gid)`**
   - Thay đổi chủ sở hữu và nhóm id của path thành uid và gid số.

6. **`os.chroot(path)`**
   - Thay đổi thư mục gốc của quá trình hiện tại thành path.

7. **`os.close(fd)`**
   - Đóng bộ điều khiển tệp fd.

8. **`os.closerange(fd_low, fd_high)`**
   - Đóng tất cả các bộ điều khiển tệp từ fd_low (bao gồm) đến fd_high (không bao gồm), bỏ qua lỗi.

9. **`os.dup(fd)`**
   - Trả về một bản sao của bộ điều khiển tệp fd.

10. **`os.dup2(fd, fd2)`**
    - Sao chép bộ điều khiển tệp fd thành fd2, đóng fd2 trước nếu cần thiết.

11. **`os.fchdir(fd)`**
    - Thay đổi thư mục làm việc hiện tại thành thư mục được đại diện bởi bộ điều khiển tệp fd.

12. **`os.fchmod(fd, mode)`**
    - Thay đổi chế độ của tệp được chỉ định bởi fd thành chế độ số.

13. **`os.fchown(fd, uid, gid)`**
    - Thay đổi chủ sở hữu và nhóm id của tệp được chỉ định bởi fd thành uid và gid số.

14. **`os.fdatasync(fd)`**
    - Buộc ghi của tệp với bộ điều khiển tệp fd xuống đĩa.

15. **`os.fdopen(fd[, mode[, bufsize]])`**
    - Trả về một đối tượng tệp mở kết nối với bộ điều khiển tệp fd.

16. **`os.fpathconf(fd, name)`**
    - Trả về thông tin cấu hình hệ thống liên quan đến một tệp mở. Tên chỉ định giá trị cấu hình cần lấy.

17. **`os.fstat(fd)`**
    - Trả về trạng thái cho bộ điều khiển tệp fd, giống như stat().

18. **`os.fstatvfs(fd)`**
    - Trả về thông tin về hệ thống tệp chứa tệp được liên kết với bộ điều khiển tệp fd, giống như statvfs().

19. **`os.fsync(fd)`**
    - Buộc ghi của tệp với bộ điều khiển tệp fd xuống đĩa.

20. **`os.ftruncate(fd, length)`**
    - Cắt giảm kích thước của tệp tương ứng với bộ điều khiển tệp fd, để nó tối đa là length byte.

21. **`os.getcwd()`**
    - Trả về một chuỗi đại diện cho thư mục làm việc hiện tại.

22. **`os.getcwdu()`**
    - Trả về một đối tượng Unicode đại diện cho thư mục làm việc hiện tại.

23. **`os.isatty(fd)`**
    - Trả về True nếu bộ điều khiển tệp fd mở và được kết nối với thiết bị tty(-giống), ngược lại trả về False.

24. **`os.lchflags(path, flags)`**
    - Đặt cờ của path thành các cờ số, giống như chflags(), nhưng không theo dõi liên kết tượng trưng.

25. **`os.lchmod(path, mode)`**
    - Thay đổi chế độ của path thành chế độ số.

26. **`os.lchown(path, uid, gid)`**
    - Thay đổi chủ sở hữu và nhóm id của path thành uid và gid. Hàm này sẽ không theo dõi các liên kết tượng trưng.

27. **`os.link(src, dst)`**
    - Tạo một liên kết cứng trỏ đến src được đặt tên là dst.

28. **`os.listdir(path)`**
    - Trả về một danh sách chứa tên của các mục trong thư mục được chỉ định bởi path.

29. **`os.lseek(fd, pos, how)`**
    - Đặt vị trí hiện tại của bộ điều khiển tệp fd thành vị trí pos, được sửa đổi bởi cách.

30. **`os.lstat(path)`**
    - Giống như stat(), nhưng không theo dõi các liên kết tượng trưng.

31. **`os.major(device)`**
    - Trích xuất số trình điều khiển chính từ một số thiết bị thô.

32. **`os.makedev(major, minor)`**
    - Tạo một số thiết bị thô từ số trình điều khiển chính và số trình điều khiển phụ.

33. **`os.makedirs(path[, mode])`**
    - Hàm tạo thư mục đệ quy.

34. **`os.minor(device)`**
    - Trích xuất số trình điều khiển phụ từ một số thiết bị thô.

35. **`os.mkdir(path[, mode])`**
    - Tạo một thư mục có tên là path với mode số.

36. **`os.mkfifo(path[, mode])`**
    - Tạo một FIFO (một ống đặt tên) có tên là path với mode số. Chế độ mặc định là 0666 (hệ bát phân).

37. **`os.mknod(filename[, mode=0600, device])`**
    - Tạo một nút hệ thống tệp (tệp, tệp đặc biệt thiết bị hoặc ống đặt tên) có tên là filename.

38. **`os.open(file, flags[, mode])`**
    - Mở tệp file và thiết lập các cờ khác nhau tùy thuộc vào flags và có thể là chế độ của nó tùy thuộc vào mode.

39. **`os.openpty()`**
    - Mở một cặp pseudo-terminal mới. Trả về một cặp bộ điều khiển tệp (master, slave) cho pty và tty, tương ứng.

40. **`os.pathconf(path, name)`**
    - Trả về thông tin cấu hình hệ thống liên quan đến một tệp có tên.

41. **`os.pipe()`**
    - Tạo một ống. Trả về một cặp bộ điều khiển tệp (r, w) có thể sử dụng để đọc và ghi, tương ứng.

42. **`os.popen(command[, mode[, bufsize]])`**
    - Mở một ống vào hoặc ra khỏi lệnh command.

43. **`os.read(fd, n)`**
    - Đọc tối đa n byte từ bộ điều khiển tệp fd. Trả về một chuỗi chứa các byte được đọc.

44. **`os.readlink(path)`**
    - Trả về một chuỗi đại diện cho đường dẫn mà liên kết tượng trưng trỏ đến.

45. **`os.remove(path)`**
    - Xóa tệp path.

46. **`os.removedirs(path)`**
    - Xóa các thư mục đệ quy.

47. **`os.rename(src, dst)`**
    - Đổi tên tệp hoặc thư mục src thành dst.

48. **`os.renames(old, new)`**
    - Hàm đổi tên đệ quy thư mục hoặc tệp.

49. **`os.rmdir(path)`**
    - Xóa thư mục path.

50. **`os.stat(path)`**
    - Thực hiện một cuộc gọi hệ thống stat trên đường dẫn được chỉ định.

51. **`os.stat_float_times([newvalue])`**
    - Xác định xem stat_result có đại diện cho dấu thời gian dưới dạng đối tượng float không.

52. **`os.statvfs(path)`**
    - Thực hiện một cuộc gọi hệ thống statvfs trên đường dẫn được chỉ định.

53. **`os.symlink(src, dst)`**
    - Tạo một liên kết tượng trưng trỏ đến src có tên là dst.

54. **`os.tcgetpgrp(fd)`**
    - Trả về nhóm quá trình được liên kết với thiết bị ký tự được chỉ định bởi fd.

55. **`os.tcsetpgrp(fd, pg)`**
    - Đặt nhóm quá trình được liên kết với thiết bị ký tự được chỉ định bởi fd thành pg.

56. **`os.tempnam([dir[, prefix]])`**
    - Trả về một tên đường dẫn duy nhất hợp lý để tạo một tệp tạm thời.

57. **`os.tmpfile()`**
    - Trả về một đối tượng tệp mới được mở ở chế độ cập nhật (w+b).

58. **

`os.tmpnam()`**
    - Trả về một tên đường dẫn duy nhất hợp lý để tạo một tệp tạm thời.

59. **`os.ttyname(fd)`**
    - Trả về một chuỗi chỉ định thiết bị ký tự được liên kết với bộ điều khiển tệp fd. Nếu fd không được liên kết với thiết bị ký tự, một ngoại lệ sẽ được ném.

60. **`os.unlink(path)`**
    - Xóa tệp path.

61. **`os.utime(path, times)`**
    - Đặt thời gian truy cập và sửa đổi của tệp được chỉ định bởi path.

62. **`os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])`**
    - Tạo ra các tên tệp trong một cây thư mục bằng cách duyệt cây từ trên xuống hoặc từ dưới lên.

63. **`os.write(fd, str)`**
    - Ghi chuỗi str vào bộ điều khiển tệp fd. Trả về số byte thực sự được ghi.