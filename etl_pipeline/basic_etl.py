import pandas as pd

def extract():
    data = {
        "symbol": ["AAPL", "TSLA", "NVDA"],
        "price": [190, 250, 800],
        "volume": [1000, 2000, 1500]
    }
    return pd.DataFrame(data)

def transform(df):
    df["price_usd"] = df["price"] * 1.0
    df["volume_flag"] = df["volume"].apply(lambda x: "HIGH" if x > 1500 else "LOW")
    return df

def load(df):
    df.to_csv("output.csv", index=False)
    print("Data saved to output.csv")

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
