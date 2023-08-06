# Author: Arabian Coconut
# Last Modified: 06/07/2023
import json
import requests
from functools import lru_cache
from bs4 import BeautifulSoup

# Api for getting the latest news from moneycontrol.com

# Constants
title_text = "Title:"
link_text = "Link:"
date_text = "Date:"
html_parser = "html.parser"
news_type = "News Type:"

# Urls for getting the news
url = ["https://www.moneycontrol.com/news",
       "https://www.moneycontrol.com/news/business",
       "https://www.moneycontrol.com/news/latest-news/"]


@lru_cache(maxsize=16)
def get_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    url_data = requests.get(url[0], timeout=60)
    soup = BeautifulSoup(url_data.text, "html.parser")
    soup_process = soup.find_all("h3", {"class": "related_des"})
    for i in soup_process:
        title_info = i.find("a").get("title")
        link_info = i.find("a").get("href")
        json_data = {news_type: "News", title_text: title_info, link_text: link_info, date_text: "None"}
        dict_storage(json_data)
        return json_data


@lru_cache(maxsize=16)
def get_business_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(url[1], timeout=60).text, html_parser)
    # Get the title, link and date of the news
    new_list = "newslist-0"
    news_list = soup.find("li", {"class": "clearfix", "id": new_list})
    title = news_list.find("h2").find("a").get("title")
    link = news_list.find("h2").find("a").get("href")
    date = news_list.find("span", {"class": "list_dt"})
    json_data = {news_type: "Business News", title_text: title, link_text: link, date_text: date}
    dict_storage(json_data)
    return json_data


@lru_cache(maxsize=16)
def get_latest_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(url[2], timeout=60).text, html_parser)
    # Get the title, link and date of the news
    related_des_class = soup.find_all("h3", {"class": "related_des"})
    related_date_class = soup.find_all("p", {"class": "related_date hide-mob"})
    for h3_tag, p_tag in zip(related_des_class, related_date_class):
        title = h3_tag.find("a").get("title")
        link = h3_tag.find("a").get("href")
        date = p_tag.text
        json_data = {news_type: "Latest News", title_text: title, link_text: link, date_text: date}
        dict_storage(json_data)
        return json_data


def dict_storage(json_format: dict):
    new_entry = {
        "news_type": json_format["News Type:"],
        "title": json_format["Title:"],
        "link": json_format["Link:"],
        "date": json_format["Date:"]
    }

    data = {}

    try:
        with open('static/api_data.json', 'r') as f:
            data = dict(json.load(f))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open('static/api_data.json', 'w+') as f:
            json.dump({}, f)

    data.setdefault("Api_response", []).append(new_entry)

    with open('static/api_data.json', 'w') as f:
        json.dump(data, f, indent=4)

    return data
