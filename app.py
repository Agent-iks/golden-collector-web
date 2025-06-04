from flask import Flask, request, jsonify, send_file
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
    return jsonify({"message": f"{symbol.upper()} added to raw_metrics"}), 200

@app.route("/download_symbol", methods=["GET"])
def download_symbol():
    symbol = request.args.get("symbol")
    filepath = f"data/raw_metrics/{symbol.upper()}.csv"

    if not os.path.exists(filepath):
        return jsonify({"error": f"{symbol.upper()} not found"}), 404

    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)
