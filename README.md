# AI-Stock
ARIMA
----------
**Lưu ý rằng ví dụ trên chỉ là một mô phỏng đơn giản và không đại diện cho mọi trường hợp sử dụng. ARIMA có thể cần được tinh chỉnh thêm và được áp dụng cho các dữ liệu thực tế khác nhau để đạt được kết quả tốt nhất.
**
----------
Trong ví dụ trên, tệp CSV '2019.csv' được chuẩn bị với hai cột: 'date' và 'close'. Cột 'date' chứa thông tin về ngày (dưới định dạng 'yyyy-mm-dd') và cột 'Close' chứa thông tin về giá cổ phiếu tương ứng với mỗi ngày.

Dưới đây là một ví dụ về cách dữ liệu có thể được tổ chức trong tệp CSV:

```
date,close
2010-01-01,100.25
2010-01-02,101.50
2010-01-03,99.75
2010-01-04,105.30
...
```

Trong thực tế, dữ liệu giá cổ phiếu thường chứa nhiều cột khác như mở cửa (open), cao nhất (high), thấp nhất (low), khối lượng giao dịch (volume), v.v. Tuy nhiên, trong ví dụ này, chúng ta chỉ tập trung vào giá cổ phiếu duy nhất.

Lưu ý rằng các giá trị trong cột 'close' có thể là số thập phân hoặc số nguyên, tùy thuộc vào đơn vị giá cổ phiếu và mức độ chính xác mong muốn.

Trước khi chạy ví dụ, hãy đảm bảo rằng bạn đã tạo tệp CSV '2019.csv' và điều chỉnh nội dung của nó theo đúng định dạng như ví dụ trên.
