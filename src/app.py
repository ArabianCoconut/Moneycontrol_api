# Author: Arabian Coconut
# Last Modified: 02/01/2024 (DD/MM/YYYY)
import requests
import moneycontrol.moneycontrol_api as mc
import moneycontrol.storage_control as sc
from flask import Flask, request,jsonify, render_template

app = Flask(__name__)

@app.route('/api/<news>', methods=['GET'])
def api(news):
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns: json_data (JSON object): A JSON object containing the title, link, and date of the news, business news,
    and latest news.
    """
    match request.method:
        case 'GET':
            match news:
                case 'news':
                    return mc.get_news()
                case 'business':
                    return mc.get_business_news()
                case 'latest':
                    return mc.get_latest_news()
                case 'list': 
                        return sc.dump_all_data_to_json()
                case 'status':
                    return jsonify({"status": "200"})
        case _:
            return jsonify({"error": "Method not allowed or server error"})

@app.route('/price/<stock>', methods=['GET'])
def price_worker(stock):
    """
    Gets the stock price from the given URL and returns a JSON object containing the stock price.

    Parameters:
    url (string): The URL from which to retrieve the stock price

    Returns:
    json_data (JSON object): A JSON object containing the stock price
    """
    match request.method:
        case 'GET':
            try:
                return jsonify(mc.get_basic_price(stock.upper()))
            except requests.exceptions.JSONDecodeError:
                return jsonify({"Error": "Your seeing this because certain symbols are not supported due to complexities raise an issue on the github page.",
                                "Github": "https://github.com/ArabianCoconut/Moneycontrol_api"
                                })
        case _:
            return jsonify({"error": "Method not allowed or server error"})
    
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.run(debug=True, port=5000, host='localhost')