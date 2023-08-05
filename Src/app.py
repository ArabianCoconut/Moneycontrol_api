import Modules.moneycontrol_api as mc
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
    if request.method == 'GET' and news == 'news':
        return jsonify(mc.get_news())
    elif request.method == 'GET' and news == 'business':
        return jsonify(mc.get_business_news())
    elif request.method == 'GET' and news == 'latest':
        return jsonify(mc.get_latest_news())
    else:
        return jsonify({"error": "Method not allowed"})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



