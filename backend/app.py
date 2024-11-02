from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def fetch_stock_data(symbol):
    url = f'https://api.iextrading.com/1.0/stock/{symbol}/quote'
    response = requests.get(url)
    return response.json()


@app.route('/')
def index():
    return "<p>hi</p>"

@app.route('/stocks', methods=['GET'])
def get_stocks():
    symbol = request.args.getList('symbols')
    stock_data = {}

    for symbol in symbols:
        stock_info = fetch_stock_data(symbol)
        stock_data[symbol] = stock_info

    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)