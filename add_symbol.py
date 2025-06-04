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

    # Путь к файлу
    filepath = f"data/raw_metrics/{symbol.upper()}.csv"

    # Убедимся, что директория существует
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Шапка таблицы
    columns = [
        "timestamp", "price", "close", "rsi", "tail", "slope",
        "volume", "volume_surge", "whales", "liquidity", "label"
    ]

    # Создаём пустую таблицу
    df = pd.DataFrame(columns=columns)
    df["label"] = 0

    # Сохраняем
    df.to_csv(filepath, index=False)

    print(f"[{datetime.now()}] ✅ Файл создан: {filepath}")
    return jsonify({"message": f"{symbol.upper()} added to raw_metrics"}), 200

if __name__ == "__main__":
    app.run(debug=True)
