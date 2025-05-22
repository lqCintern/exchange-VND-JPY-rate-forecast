import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('data_raw/global_market_indicators/history.csv', parse_dates=['Date'])

# Đặt Date làm index để nội suy theo thời gian
df = df.set_index('Date')

# Nội suy tuyến tính cho toàn bộ các cột (theo trục thời gian)
df_interp = df.interpolate(method='time')

# Nếu còn giá trị thiếu ở đầu/cuối, dùng forward/backward fill
df_interp = df_interp.ffill().bfill()

# Đặt lại index về cột Date
df_interp = df_interp.reset_index()

# Ghi ra file mới
df_interp.to_csv('data_raw/global_market_indicators/history_filled.csv', index=False)

print("✅ Đã điền xong giá trị thiếu bằng nội suy tuyến tính!")
