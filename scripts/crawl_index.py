import yfinance as yf
import pandas as pd

tickers = {
    'S&P500': '^GSPC',
    'DXY': 'DX-Y.NYB',
    'Nikkei225': '^N225',
    'VIX': '^VIX',
    'BrentOil': 'BZ=F',
    'WTIOil': 'CL=F',
    'US10YYield': '^TNX',
}

start_date = "2020-01-01"
end_date = "2024-12-31"

data = pd.DataFrame()

for name, ticker in tickers.items():
    print(f"Downloading {name}...")
    df = yf.download(ticker, start=start_date, end=end_date)['Close']
    df = df.rename(columns={'Close': name})
    data = pd.concat([data, df], axis=1)

data.to_csv("../data_raw/global_market_indicators.csv")
print("✅ Dữ liệu đã lưu vào global_market_indicators.csv")
