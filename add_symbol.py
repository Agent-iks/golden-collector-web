from flask import Flask, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/add_symbol", methods=["POST"])
def add_symbol():
    data = request.get_json()
    symbol = data.get("symbol")

    if not symbol:
        return jsonify({"error": "Symbol not provided"}), 400

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
    return jsonify({"message": f"{symbol.upper()} added to raw_metrics"}), 200

if __name__ == "__main__":
    app.run(debug=True)
