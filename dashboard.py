import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Sedang memproses data...")

dfCustomer = pd.read_csv('datacustomer.csv')


dfCustomer['SubscriptionDate'] = pd.to_datetime(dfCustomer['Subscription Date'])
dfCustomer['Year'] = dfCustomer['SubscriptionDate'].dt.year
dfCustomer['Month'] = dfCustomer['SubscriptionDate'].dt.strftime('%B')
dfCustomer['MonthNum'] = dfCustomer['SubscriptionDate'].dt.month


sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
plt.subplots_adjust(hspace=0.4)

dataTahun = dfCustomer.groupby('Year')['Customer Id'].count()
ax1 = plt.subplot(2, 2, 1)
sns.lineplot(x=dataTahun.index, y=dataTahun.values, marker='o', linewidth=2, color='royalblue', ax=ax1)
plt.title('1. Pertumbuhan Subscriber per Tahun', fontweight='bold')
plt.xticks(dataTahun.index)

for x, y in zip(dataTahun.index, dataTahun.values):
    plt.text(x, y + 0.5, str(int(y)), ha='center', fontweight='bold', color='darkblue')


topNegara = dfCustomer['Country'].value_counts().head(5)
ax2 = plt.subplot(2, 2, 2)
plotNegara = sns.barplot(x=topNegara.values, y=topNegara.index, hue=topNegara.index, palette='viridis', legend=False, ax=ax2)
plt.title('2. Top 5 Negara Terbanyak', fontweight='bold')
ax2.bar_label(ax2.containers[0], padding=3, fontweight='bold')

dataBulan = dfCustomer.groupby(['MonthNum', 'Month'])['Customer Id'].count().reset_index()
ax3 = plt.subplot(2, 1, 2)
plotBulan = sns.barplot(x='Month', y='Customer Id', data=dataBulan, hue='Month', palette='coolwarm', legend=False, ax=ax3)
plt.title('3. Tren Lonjakan per Bulan', fontweight='bold')
plt.xlabel('Bulan')
ax3.bar_label(ax3.containers[0], padding=3, fontweight='bold')

print("Selesai! Grafik dengan angka rinci akan muncul sekarang.")
plt.tight_layout()
plt.show()