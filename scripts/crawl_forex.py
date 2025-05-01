#!/usr/bin/env python3
"""
Script to crawl JPY/VND exchange rate data from Vietcombank's website.
"""

import requests
from bs4 import BeautifulSoup

# URL của trang Vietcombank
URL = "https://portal.vietcombank.com.vn/Personal/TG/Pages/ty-gia.aspx"

# User agent để giả lập trình duyệt
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_and_parse():
    """
    Fetch and parse JPY/VND exchange rate from Vietcombank.
    """
    try:
        # Gửi request đến trang web
        response = requests.get(URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Phân tích HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm bảng tỷ giá (cập nhật logic tìm kiếm)
        table = soup.find('table')
        if not table:
            print("Không tìm thấy bảng tỷ giá.")
            return

        # Tìm tất cả các dòng trong bảng
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if cells and 'JPY' in cells[0].get_text(strip=True):
                # Lấy các giá trị mua, chuyển khoản, bán
                buy_rate = cells[1].get_text(strip=True)
                transfer_rate = cells[2].get_text(strip=True)
                sell_rate = cells[3].get_text(strip=True)

                # Hiển thị kết quả
                print(f"Tỷ giá JPY/VND:")
                print(f"  Mua: {buy_rate}")
                print(f"  Chuyển khoản: {transfer_rate}")
                print(f"  Bán: {sell_rate}")
                return

        print("Không tìm thấy tỷ giá JPY/VND.")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gửi request: {e}")
    except Exception as e:
        print(f"Lỗi khi phân tích dữ liệu: {e}")

if __name__ == "__main__":
    fetch_and_parse()
