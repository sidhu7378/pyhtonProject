total_cases = confirmed_df.iloc[:, 4:].sum().max()
total_deaths = deaths_df.iloc[:, 4:].sum().max()
total_df = pd.DataFrame({
    "Total Confirmed Cases": [total_cases],
    "Total Deaths": [total_deaths]
})
total_df