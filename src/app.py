# Author: Arabian Coconut
# Last Modified: 17/09/2023
import moneycontrol.moneycontrol_api as mc
import moneycontrol.storage_control as sc
from flask import Flask, jsonify, render_template

app = Flask(__name__)
sc_instance= sc.StorageControl("data.pkl")

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
    match news:
        case 'news':
            return jsonify(mc.get_news())
        case 'business':
            return jsonify(mc.get_business_news())
        case 'latest':
            return jsonify(mc.get_latest_news())
        case 'list':
            sc_instance.convert_to_json()
            return jsonify(open(sc_instance.json_path(), 'r', encoding='utf-8').read())
        case 'status':
            return jsonify({"status": "200"})
        case _:
            return jsonify({"error": "Method not allowed or server error"})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080, debug=True)