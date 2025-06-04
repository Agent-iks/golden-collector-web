import pandas as pd
import os
from datetime import datetime

def add_main(symbol):
    os.makedirs("data/raw_metrics", exist_ok=True)

    columns = [
        "timestamp", "price", "close", "rsi", "tail", "slope",
        "volume", "volume_surge", "whales", "liquidity", "label"
    ]

    df = pd.DataFrame(columns=columns)
    df["label"] = 0

    filepath = f"data/raw_metrics/{symbol.upper()}.csv"
    df.to_csv(filepath, index=False)

    print(f"[{datetime.now()}] ✅ Создан файл: {filepath}")
