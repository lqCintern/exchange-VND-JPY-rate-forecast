# exchange-VND-JPY-rate-forecast

# Dự báo tỷ giá JPY/VND

Thu thập dữ liệu gốc phục vụ bài toán dự báo tỷ giá bằng mô hình chuỗi thời gian.

## 1. Dữ liệu

- tỉ giá JPY/VND trên Vietcombank
- `sp500.csv`: chỉ số thị trường S&P 500 từ Yahoo Finance (qua thư viện `yfinance`).

## 2. Cách chạy script

### Crawl tỷ giá JPY/VND theo Vietcombank

```bash
cd scripts
python crawl_forex.py

```

## 3. Cấu trúc

exchange-rate-forecast/
├── data_raw/
│ ├── forex_usdjpy_daily.csv # Dữ liệu tỷ giá JPY/VND (đại diện volume)
│ └── sp500.csv # Dữ liệu chỉ số thị trường S&P 500
├── scripts/
│ ├── crawl_forex.py # Script crawl tỷ giá JPY/VND từ Vietcombank
│ └── crawl_index.py # Script crawl chỉ số S&P 500 từ yfinance
├── .gitignore
└── README.md

| Tên chỉ số                 | Diễn giải                            | Tác động                                       |
| -------------------------- | ------------------------------------ | ---------------------------------------------- |
| **S&P 500** (Mỹ)           | Chỉ số chứng khoán lớn nhất thế giới | Tâm lý rủi ro toàn cầu                         |
| **DXY – US Dollar Index**  | Sức mạnh đồng USD                    | Ảnh hưởng trực tiếp đến USD/JPY, USD/VND       |
| **Nikkei 225** (Nhật)      | Chỉ số thị trường chứng khoán Nhật   | Tác động đến JPY                               |
| **VIX (Fear Index)**       | Mức độ sợ hãi của thị trường         | Căng thẳng tăng → dòng tiền vào JPY            |
| **Oil prices (Brent/WTI)** | Giá dầu thế giới                     | Ảnh hưởng gián tiếp đến VN (vì xuất nhập khẩu) |
| **US 10Y Bond Yield**      | Lãi suất trái phiếu Mỹ               | Dòng tiền toàn cầu, ảnh hưởng USD & tỷ giá     |

- File `global_market_indicators.csv` có định dạng:

| Date       | S&P500 | DXY  | Nikkei225 | VIX   | BrentOil | WTIOil | US10YYield |
| ---------- | ------ | ---- | --------- | ----- | -------- | ------ | ---------- |
| 2020-01-02 | 3257.8 | 96.3 | 23656     | 13.78 | 66.25    | 61.0   | 1.88       |
| …          | …      | …    | …         | …     | …        | …      | …          |

```

```
