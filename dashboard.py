import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Sedang memproses data...")
df = pd.read_csv('datacustomer.csv')

df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])

df['Year'] = df['Subscription Date'].dt.year
df['Month'] = df['Subscription Date'].dt.strftime('%B')
df['Month_Num'] = df['Subscription Date'].dt.month

sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
data_tahun = df.groupby('Year')['Customer Id'].count()
sns.lineplot(x=data_tahun.index, y=data_tahun.values, marker='o', linewidth=2, color='blue')
plt.title('1. Pertumbuhan Subscriber per Tahun')
plt.xticks(data_tahun.index) 

plt.subplot(2, 2, 2)
top_country = df['Country'].value_counts().head(5)
sns.barplot(x=top_country.values, y=top_country.index, palette='viridis')
plt.title('2. Top singko 5 Negara Terbanyak')

plt.subplot(2, 1, 2)
data_bulan = df.groupby(['Month_Num', 'Month'])['Customer Id'].count().reset_index()
sns.barplot(x='Month', y='Customer Id', data=data_bulan, palette='coolwarm')
plt.title('3. Tren Lonjakan per Bulan')
plt.xlabel('Bulan')

print("Selesai! Grafik akan muncul sekarang.")
plt.tight_layout()
plt.show()