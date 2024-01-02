# Author: Arabian Coconut
# Last Modified: 06/07/2023
import moneycontrol.moneycontrol_api as mc
import json
from flask import Flask, request, jsonify, render_template

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
                    return jsonify(mc.get_news())
                case 'business':
                    return jsonify(mc.get_business_news())
                case 'latest':
                    return jsonify(mc.get_latest_news())
                case 'list':
                    with open('static/api_data.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    return jsonify(data)
                case 'status':
                    return jsonify({"status": "200"})
        case _:
            return jsonify({"error": "Method not allowed or server error"})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
