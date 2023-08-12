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
----------
Trong ví dụ trên, tệp CSV 'stock_prices.csv' được chuẩn bị với hai cột: 'date' và 'stock_price'. Cột 'date' chứa thông tin về ngày (dưới định dạng 'yyyy-mm-dd') và cột 'stock_price' chứa thông tin về giá cổ phiếu tương ứng với mỗi ngày.

Dưới đây là một ví dụ về cách dữ liệu có thể được tổ chức trong tệp CSV:

```
date,stock_price
2010-01-01,100.25
2010-01-02,101.50
2010-01-03,99.75
2010-01-04,105.30
...
```

Trong thực tế, dữ liệu giá cổ phiếu thường chứa nhiều cột khác như mở cửa (open), cao nhất (high), thấp nhất (low), khối lượng giao dịch (volume), v.v. Tuy nhiên, trong ví dụ này, chúng ta chỉ tập trung vào giá cổ phiếu duy nhất.

Lưu ý rằng các giá trị trong cột 'stock_price' có thể là số thập phân hoặc số nguyên, tùy thuộc vào đơn vị giá cổ phiếu và mức độ chính xác mong muốn.

Trước khi chạy ví dụ, hãy đảm bảo rằng bạn đã tạo tệp CSV 'stock_prices.csv' và điều chỉnh nội dung của nó theo đúng định dạng như ví dụ trên.
