# import moneycontrol.moneycontrol_api as mc
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """


# TODO: Add the ability to get news and return JSON.

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
