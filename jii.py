import yfinance as yf
import pandas as pd
import os
from datetime import datetime

kodesaham = "^JKII"
namafolder = "HasilJII"
tglmulai = "2020-01-01"
tglakhir = datetime.now().strftime('%Y-%m-%d')

os.makedirs(namafolder, exist_ok=True)

print(f"Sedang download data {kodesaham}...")

data = yf.download(kodesaham, start=tglmulai, end=tglakhir, progress=False, auto_adjust=False)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

rumus = {
    'Open': 'first', 
    'High': 'max', 
    'Low': 'min', 
    'Close': 'last', 
    'Volume': 'sum'
}

#Mingguan (Jumat)
datamingguan = data.resample('W-FRI').agg(rumus).dropna().round(2)
datamingguan.to_csv(f"{namafolder}/JIIWeekly20202026.csv")
print("✅ Data Mingguan Su Selesai")

#(Akhir Bulan)
databulanan = data.resample('ME').agg(rumus).dropna().round(2)
databulanan.to_csv(f"{namafolder}/JIIMonthly20202026.csv")
print("Data Bulanan Su Selesai")

#(Akhir Tahun)
datatahunan = data.resample('YE').agg(rumus).dropna().round(2)
datatahunan.to_csv(f"{namafolder}/JIIYearly20202026.csv")
print("✅ Data Tahunan Su Selesai")

print(f"\nSelesai! Cek folder '{namafolder}'")