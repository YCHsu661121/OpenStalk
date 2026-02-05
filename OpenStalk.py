from flask import Flask, request, jsonify
import yfinance as yf
import subprocess

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_stock_data():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Ticker symbol is required"}), 400
    
    try:
        stock = yf.Ticker(ticker)
        data = {
            "company": stock.info.get("longName", "N/A"),
            "current_price": stock.info.get("currentPrice", "N/A"),
            "market_cap": stock.info.get("marketCap", "N/A"),
            "sector": stock.info.get("sector", "N/A")
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ollama', methods=['POST'])
def call_ollama():
    data = request.json
    if not data or 'command' not in data:
        return jsonify({"error": "Command is required."}), 400

    command = data['command']
    try:
        # Call the Ollama docker container via subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"output": result.stdout, "error": result.stderr}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)