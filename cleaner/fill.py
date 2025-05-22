import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('data/raw/history.csv', parse_dates=['Date'])
df = df.set_index('Date')

# Bổ sung tất cả các ngày còn thiếu trong khoảng thời gian
full_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
df = df.reindex(full_range)

# Áp dụng rolling mean cho các giá trị thiếu
df_filled = df.copy()
for col in df.columns:
    df_filled[col] = df[col].fillna(df[col].rolling(window=3, min_periods=1, center=True).mean())

# Nếu vẫn còn thiếu (ở đầu/cuối), dùng ffill/bfill
df_filled = df_filled.ffill().bfill()

# Đặt lại index về cột Date
df_filled = df_filled.reset_index().rename(columns={'index': 'Date'})

# Ghi ra file mới
df_filled.to_csv('data/cleaned/history.csv', index=False)

print("✅ Đã bổ sung đủ ngày và điền xong giá trị thiếu!")
