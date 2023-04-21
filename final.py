import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

confirmed_df.columns = confirmed_df.columns[:4].tolist() + pd.to_datetime(confirmed_df.columns[4:]).tolist()
deaths_df.columns = deaths_df.columns[:4].tolist() + pd.to_datetime(deaths_df.columns[4:]).tolist()

fig, ax1 = plt.subplots(figsize=(15, 9))
ax2 = ax1.twinx()

ax1.plot(confirmed_df.iloc[:, 4:].sum(), label="Total Confirmed Cases", color='blue')
ax1.plot(deaths_df.iloc[:, 4:].sum(), label="Total Death Cases", color='red')
ax1.set_xlabel("Date")
ax1.legend()

ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.setp(ax1.xaxis.get_majorticklabels(), rotation=90, ha='right')
ax1.grid(True)  # add gridlines to ax1

prices_df.plot(ax=ax2, color='black')
ax2.set_ylabel("Stock Prices", color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
prices_df[[col for col in prices_df.columns if 'High' in col]].plot(ax=ax2, linestyle='solid', color='green')
prices_df[[col for col in prices_df.columns if 'Low' in col]].plot(ax=ax2, linestyle='dotted', color='purple')
ax2.grid(True)  # add gridlines to ax2

ax2.set_title("COVID-19 Cases and Stock Prices")
plt.subplots_adjust(right=0.9)

plt.show()
