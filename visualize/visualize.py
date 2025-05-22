import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu đã điền đầy đủ
df = pd.read_csv('data/cleaned/history.csv', parse_dates=['Date'])
df = df.set_index('Date')

# Vẽ tất cả các chỉ số trên cùng một biểu đồ và lưu ra file
df.plot(figsize=(15, 6))
plt.title('Các chỉ số tài chính sau khi điền giá trị thiếu')
plt.xlabel('Ngày')
plt.ylabel('Giá trị')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('all_indices.png')  # Lưu ra file ảnh
plt.close()

# Vẽ từng chỉ số riêng và lưu ra file
for col in df.columns:
    df[col].plot(figsize=(15, 4), title=col)
    plt.xlabel('Ngày')
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(f'{col}.png')
    plt.close()