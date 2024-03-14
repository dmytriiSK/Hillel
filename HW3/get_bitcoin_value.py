import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/bitcoin_rate')
def get_bitcoin_value():
    currency = request.args.get('currency', default='USD', type=str)
    convert = request.args.get('convert', default=1, type=int)
    response = requests.get('https://bitpay.com/api/rates')
    rates = response.json()

    rate = [r for r in rates if r['code'] == currency]
    if not rate:
        return {"error": "Invalid currency code"}
    rate = rate[0]['rate']
    value = rate * convert

    return {"value": value}
