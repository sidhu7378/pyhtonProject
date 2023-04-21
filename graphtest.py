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
