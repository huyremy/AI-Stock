# AI-Stock
ARIMA
----------
Trong ví dụ này, chúng ta đầu tiên đọc dữ liệu từ một tệp CSV chứa thông tin về giá cổ phiếu theo thời gian. Sau đó, chúng ta chuyển đổi cột 'date' thành đối tượng datetime và đặt cột 'date' làm chỉ mục của DataFrame.

Tiếp theo, chúng ta chia dữ liệu thành tập huấn luyện (2010-01-01 đến 2022-12-31) và tập kiểm tra (2023-01-01 đến 2023-12-31).

Sau đó, chúng ta tạo một mô hình ARIMA với tham số (p, d, q) được đặt là (2, 1, 2). Đây là một lựa chọn tham số phổ biến trong mô hình ARIMA.

Tiếp theo, chúng ta phù hợp với mô hình với dữ liệu huấn luyện bằng cách gọi phương thức fit().

Sau khi mô hình được huấn luyện, chúng ta sử dụng nó để dự đoán giá cổ phiếu trên tập kiểm tra bằng cách gọi phương thức predict().

Cuối cùng, chúng ta vẽ biểu đồ với giá cổ phiếu thực tế và giá cổ phiếu dự đoán để so sánh chúng.

Lưu ý rằng ví dụ trên chỉ là một mô phỏng đơn giản và không đại diện cho mọi trường hợp sử dụng. ARIMA có thể cần được tinh chỉnh thêm và được áp dụng cho các dữ liệu thực tế khác nhau để đạt được kết quả tốt nhất.
