from flask import Flask, request, jsonify
import asyncio
from add_symbol import main as add_main

app = Flask(__name__)

@app.route("/add_symbol", methods=["POST"])
def add_symbol():
    data = request.get_json()
    symbol = data.get("symbol")
    if not symbol:
        return jsonify({"error": "Symbol not provided"}), 400

    try:
        asyncio.run(add_main(symbol))
        return jsonify({"status": "OK", "symbol": symbol}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
