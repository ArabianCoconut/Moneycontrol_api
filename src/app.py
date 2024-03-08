# Author: Arabian Coconut
# Last Modified: 02/01/2024 (DD/MM/YYYY)
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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
