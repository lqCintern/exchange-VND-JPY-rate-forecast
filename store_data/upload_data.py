import os
import boto3
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# Load biến môi trường từ .env
load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Khởi tạo client S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

# Đọc file raw lớn
df = pd.read_csv('data/cleaned/history.csv', parse_dates=['Date'])
df = df.set_index('Date')

# Tách dữ liệu lịch sử (history) và upload
history = df[df.index <= '2025-05-14']
history_file = 'history.csv'
history.to_csv(history_file)
s3.upload_file(history_file, S3_BUCKET_NAME, 'uploads/global_market_indicators/history.csv')
print("✅ Đã upload history.csv lên S3")

# Tách và upload từng ngày mới
daily = df[df.index > '2025-05-14']
for date, group in daily.groupby(daily.index.date):
    date_str = date.strftime('%d-%m-%Y')
    file_name = f'{date_str}.csv'
    group.to_csv(file_name)
    s3.upload_file(file_name, S3_BUCKET_NAME, f'uploads/global_market_indicators/{file_name}')
    print(f"✅ Đã upload {file_name} lên S3")
    os.remove(file_name)  # Xóa file tạm sau khi upload

# Xóa file tạm history nếu muốn
os.remove(history_file)
