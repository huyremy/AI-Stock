import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Đọc file CSV
df = pd.read_csv('/content/dji_2009-2019.csv')

# Chuyển cột 'date' thành kiểu dữ liệu ngày
df['Date'] = pd.to_datetime(df['Date'])

# Sắp xếp dữ liệu theo ngày
df.sort_values('Date', inplace=True)

# Xác định dữ liệu train và test
train_data = df['Open'].values[:-1]  # Sử dụng tất cả dữ liệu trừ dòng cuối cùng làm dữ liệu train
test_data = df['Open'].values[-1:]  # Dòng cuối cùng làm dữ liệu test

# Xây dựng mô hình ARIMA
model = ARIMA(train_data, order=(2, 1, 2))
model_fit = model.fit()

# Dự đoán giá trị 'open' cho 'date' tiếp theo
forecast = model_fit.forecast(steps=1)[0]

# In kết quả dự đoán
print("Dự đoán giá trị 'open' cho 'date' tiếp theo:", forecast)
