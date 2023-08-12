import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Đọc file CSV
df = pd.read_csv('/content/dji_2009-2019.csv')

# Chuyển cột 'date' thành kiểu dữ liệu ngày
df['Date'] = pd.to_datetime(df['Date'])

# Sắp xếp dữ liệu theo ngày
df.sort_values('Date', inplace=True)

# Xác định dữ liệu train và test
train_data = df[:-1]  # Sử dụng tất cả dữ liệu trừ dòng cuối cùng làm dữ liệu train
test_data = df[-1:]  # Dòng cuối cùng làm dữ liệu test

# Dự đoán giá trị 'open', 'close', 'high', 'low' cho 'date' tiếp theo
forecast_data = []
columns = ['Open', 'Close', 'High', 'Low']

for column in columns:
    # Xây dựng mô hình ARIMA cho cột dữ liệu hiện tại
    model = ARIMA(train_data[column].values, order=(2, 1, 2))
    model_fit = model.fit()

    # Dự đoán giá trị cho 'date' tiếp theo
    forecast = model_fit.forecast(steps=1)[0]

    # Lưu trữ kết quả dự đoán
    forecast_data.append(forecast)

# In kết quả dự đoán
for i, column in enumerate(columns):
    print(f"Dự đoán giá trị '{column}' cho 'date' tiếp theo:", forecast_data[i])
