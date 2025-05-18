import yfinance as yf
import pandas as pd
import os
from datetime import datetime

# Tạo thư mục để lưu dữ liệu
os.makedirs('../data_raw/global_market_indicators', exist_ok=True)

# Danh sách chỉ số cần tải
tickers = {
    'S&P500': '^GSPC',
    'DXY': 'DX-Y.NYB', 
    'Nikkei225': '^N225',
    'VIX': '^VIX',
    'BrentOil': 'BZ=F',
    'WTIOil': 'CL=F',
    'US10YYield': '^TNX',
    'USDJPY': 'JPY=X',  # Thêm tỷ giá USD/JPY
}

# Ngày bắt đầu và kết thúc cho dữ liệu lịch sử
start_date = "2020-01-01"
end_date = "2025-05-16"  # Đến ngày hiện tại

# Ngày giới hạn cho dữ liệu lịch sử
cutoff_date = "2025-05-14"

# Tải dữ liệu
print("Đang tải dữ liệu...")
all_data = pd.DataFrame()

for name, ticker in tickers.items():
    print(f"Downloading {name}...")
    df = yf.download(ticker, start=start_date, end=end_date)['Close']
    df = pd.DataFrame(df)  # Chuyển Series thành DataFrame
    df = df.rename(columns={'Close': name})
    
    if all_data.empty:
        all_data = df
    else:
        all_data = all_data.join(df)

# Chia dữ liệu thành lịch sử và theo ngày
history_data = all_data[all_data.index <= cutoff_date]
daily_data = all_data[all_data.index > cutoff_date]

# Lưu dữ liệu lịch sử
history_file = '../data_raw/global_market_indicators/history.csv'
history_data.to_csv(history_file)
print(f"✅ Lưu dữ liệu lịch sử vào: {history_file}")

# Lưu dữ liệu theo từng ngày
for date, data in daily_data.groupby(daily_data.index.date):
    date_str = date.strftime('%d-%m-%Y')
    daily_file = f'../data_raw/global_market_indicators/{date_str}.csv'
    data.to_csv(daily_file)
    print(f"✅ Lưu dữ liệu ngày {date_str} vào: {daily_file}")

print("Hoàn tất tải và lưu dữ liệu!")
