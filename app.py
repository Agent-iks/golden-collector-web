from flask import Flask, request, jsonify
from add_symbol import add_main

app = Flask(__name__)

@app.route('/add_symbol', methods=['POST'])
def add_symbol_route():
    try:
        data = request.json
        symbol = data.get('symbol')
        if not symbol:
            return jsonify({"error": "Missing 'symbol'"}), 400
        add_main(symbol.upper())
        return jsonify({"message": f"{symbol} added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
