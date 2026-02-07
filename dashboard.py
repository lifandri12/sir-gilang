import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Sedang memproses data pelanggan... sabar ya sir")
dfCustomer = pd.read_csv('datacustomer.csv')

dfCustomer['SubscriptionDate'] = pd.to_datetime(dfCustomer['Subscription Date'])
dfCustomer['Year'] = dfCustomer['SubscriptionDate'].dt.year
dfCustomer['MonthName'] = dfCustomer['SubscriptionDate'].dt.strftime('%B')
dfCustomer['MonthNum'] = dfCustomer['SubscriptionDate'].dt.month

dataTahunan = dfCustomer.groupby('Year')['Customer Id'].count()
topNegara = dfCustomer['Country'].value_counts().head(5)
dataBulanan = dfCustomer.groupby(['MonthNum', 'MonthName'])['Customer Id'].count().reset_index()

sns.set_style("whitegrid")
fig = plt.figure(figsize=(18, 12), constrained_layout=True)
gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[0, 0])
sns.lineplot(x=dataTahunan.index, y=dataTahunan.values, marker='o', markersize=10, 
             linewidth=3, color='royalblue', ax=ax1)
ax1.set_title('1.Tren Pertumbuhan Tahunan', fontsize=12, fontweight='bold', pad=15)
ax1.set_xticks(dataTahunan.index)

for x, y in zip(dataTahunan.index, dataTahunan.values):
    ax1.text(x, y + (max(dataTahunan.values)*0.02), f'{int(y)}', 
             ha='center', fontweight='bold', color='darkblue', fontsize=12)

ax2 = fig.add_subplot(gs[0, 1])
sns.barplot(x=topNegara.values, y=topNegara.index, hue=topNegara.index, 
            palette='viridis', legend=False, ax=ax2)
ax2.set_title('2.Top singko 5 Negara Terbanyak', fontsize=12, fontweight='bold', pad=15)
ax2.bar_label(ax2.containers[0], padding=8, fontweight='bold', fontsize=12)

ax3 = fig.add_subplot(gs[1, :])
plotBulan = sns.barplot(x='MonthName', y='Customer Id', data=dataBulanan, hue='MonthName', 
                        palette='coolwarm', legend=False, ax=ax3)
ax3.set_title('3. Analisis Musiman: Lonjakan per Bulan ', fontsize=12, fontweight='bold', pad=15)
ax3.set_xlabel('Bulan', fontsize=12)
ax3.set_ylabel('Jumlah Subscriber', fontsize=12)

for container in ax3.containers:
    ax3.bar_label(container, padding=3, fontweight='bold', fontsize=12)

ax3.set_ylim(0, dataBulanan['Customer Id'].max() * 1.15)

print("Selesai! sir saya dedek ijin tidur.")
plt.show()