import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Đọc dữ liệu history hiện tại
history_path = 'data/raw/history.csv'
history = pd.read_csv(history_path, parse_dates=['Date'], index_col='Date')

# Xác định ngày bắt đầu crawl mới (ngày cuối cùng trong history + 1)
last_date = history.index.max()
start_date = (last_date + timedelta(days=1)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

# Nếu đã cập nhật đến hôm nay thì không cần crawl
if pd.to_datetime(start_date) > pd.to_datetime(end_date):
    print("Dữ liệu đã cập nhật đến hiện tại.")
    exit(0)

# Danh sách chỉ số cần tải (giống file crawl_index.py)
tickers = {
    'S&P500': '^GSPC',
    'DXY': 'DX-Y.NYB', 
    'Nikkei225': '^N225',
    'VIX': '^VIX',
    'BrentOil': 'BZ=F',
    'WTIOil': 'CL=F',
    'US10YYield': '^TNX',
}

print(f"Crawl bổ sung từ {start_date} đến {end_date}...")

# Crawl dữ liệu mới
new_data = pd.DataFrame()
for name, ticker in tickers.items():
    print(f"Downloading {name}...")
    df = yf.download(ticker, start=start_date, end=(datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)).strftime('%Y-%m-%d'))['Close']
    df = pd.DataFrame(df)
    df = df.rename(columns={'Close': name})
    if new_data.empty:
        new_data = df
    else:
        new_data = new_data.join(df)

# Nếu không có dữ liệu mới thì dừng
if new_data.empty:
    print("Không có dữ liệu mới để cập nhật.")
    exit(0)

# Nối vào history và loại bỏ trùng lặp
all_history = pd.concat([history, new_data])
all_history = all_history[~all_history.index.duplicated(keep='first')]
all_history = all_history.sort_index()

# Lưu lại file history
all_history.to_csv(history_path)
print(f"✅ Đã cập nhật dữ liệu mới vào {history_path}")
