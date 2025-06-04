import pandas as pd
import os
from datetime import datetime

def add_main(symbol):
    # Убедимся, что папка существует
    os.makedirs("data/raw_metrics", exist_ok=True)

    # Шапка таблицы
    columns = [
        "timestamp", "price", "close", "rsi", "tail", "slope",
        "volume", "volume_surge", "whales", "liquidity", "label"
    ]

    # Создаём пустую таблицу с label = 0
    df = pd.DataFrame(columns=columns)
    df["label"] = 0

    # Сохраняем
    filepath = f"data/raw_metrics/{symbol.upper()}.csv"
    df.to_csv(filepath, index=False)

    print(f"[{datetime.now()}] ✅ Создан файл: {filepath}")
