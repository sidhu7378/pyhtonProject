import requests


API_KEY = "TC54JI2GWZOZ8I0J"
symbols = ["VOO", "XIC.TO", "EXPE", "VNQ", "IAU"]
prices_df = pd.DataFrame()

for symbol in symbols:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()["Time Series (Daily) -Adjusted"]
    df = pd.DataFrame.from_dict(data, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    df = df.loc["2020":"2022", ["2. high", "3. low"]]
    df.columns = [f"{symbol}_High", f"{symbol}_Low"]
    prices_df = pd.concat([prices_df, df], axis=1)
