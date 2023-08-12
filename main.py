import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('stock_prices.csv')

# Chuyển đổi cột 'date' thành đối tượng datetime
df['date'] = pd.to_datetime(df['date'])

# Đặt cột 'date' làm chỉ mục
df.set_index('date', inplace=True)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_data = df['2010-01-01':'2022-12-31']
test_data = df['2023-01-01':'2023-12-31']

# Tạo mô hình ARIMA với (p, d, q) = (2, 1, 2)
model = ARIMA(train_data, order=(2, 1, 2))

# Phù hợp với mô hình với dữ liệu huấn luyện
model_fit = model.fit()

# Dự đoán giá cổ phiếu trên tập kiểm tra
predictions = model_fit.predict(start='2023-01-01', end='2023-12-31', typ='levels')

# Vẽ biểu đồ dự đoán và giá thực tế
plt.plot(test_data.index, test_data['stock_price'], label='Thực tế')
plt.plot(predictions.index, predictions, label='Dự đoán')
plt.xlabel('Ngày')
plt.ylabel('Giá cổ phiếu')
plt.title('Dự đoán giá cổ phiếu bằng mô hình ARIMA')
plt.legend()
plt.show()
