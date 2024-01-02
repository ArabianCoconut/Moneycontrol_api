# Author: Arabian Coconut
# Last Modified: 11/08/2023 #DD/MM/YYYY
# Description: This file contains the API for getting the news from the moneycontrol website.
import json
import os
import threading
import time
from functools import lru_cache
import uuid
import requests
from bs4 import BeautifulSoup


# Constants
class Api:
    """
    A class used to store constants
    """

    def __init__(self, title_info=None, link_info=None, date_info=None, news_info=None):
        """
        Initializes the constants
        """
        self.Data = {"NewsType": news_info, "Title": title_info,"Link": link_info, "Date": date_info}
        self.html_parser = "html.parser"
        self.json_file = "static/api_data.json"
        self.url = ["https://www.moneycontrol.com/news", "https://www.moneycontrol.com/news/business","https://www.moneycontrol.com/news/latest-news/"]


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
    soup = BeautifulSoup(requests.get(Api().url[0], timeout=60).text, Api().html_parser)
    soup_process = soup.find_all("h3", {"class": "related_des"})
    json_output = Api()

    for i in soup_process:
        title_info = i.find("a").get("title")
        link_info = i.find("a").get("href")
        json_output.Data.update({"NewsType": "News", "Title": title_info, "Link": link_info})
        dict_storage(json_output.Data)
        return json_output.Data


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
    json_output = Api()
    soup = BeautifulSoup(requests.get(Api().url[1], timeout=60).text, Api().html_parser)

    new_list = "newslist-0"
    news_list = soup.find("li", {"class": "clearfix", "id": new_list})
    title_info = news_list.find("h2").find("a").get("title")
    link_info = news_list.find("h2").find("a").get("href")
    date_info = news_list.find("span", {"class": "list_dt"})
    json_output.Data.update({"NewsType": "Business News", "Title": title_info, "Link": link_info, "Date": date_info})
    dict_storage(json_output.Data)
    return json_output.Data


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

    json_output = Api()
    soup = BeautifulSoup(requests.get(Api().url[2], timeout=60).text, Api().html_parser)
    # Get the title, link and date of the news
    related_des_class = soup.find_all("h3", {"class": "related_des"})
    related_date_class = soup.find_all("p", {"class": "related_date hide-mob"})
    for h3_tag, p_tag in zip(related_des_class, related_date_class):
        title_info = h3_tag.find("a").get("title")
        link_info = h3_tag.find("a").get("href")
        date_info = p_tag.text
        json_output.Data.update({"NewsType": "Latest News", "Title": title_info, "Link": link_info, "Date": date_info})
        dict_storage(json_output.Data)
        return json_output.Data


def file_remove():
    # check file size is greater than 1MB
    # if greater than 1MB then delete the file
    # else wait for 7 days
    while True:
        if os.path.exists(Api().json_file):
            file_size = os.path.getsize(Api().json_file)
            if file_size > 1000000:
                os.remove(Api().json_file)
                print("File removed successfully")
                dict_storage(Api().Data)
                time.sleep(604800)
            else:
                print("File size is less than 1MB, check after 7 days")
                time.sleep(604800)
        else:
            time.sleep(604800)


def dict_storage(json_format: dict):
    """
    Stores the data in a JSON file, and removes the file if the size is greater than 1MB
    """
    threading.Thread(target=file_remove).start()

    new_entry = {
        "NewsType": json_format["NewsType"],
        "Title": json_format["Title"],
        "Link": json_format["Link"],
        "Date": json_format["Date"]
    }
    data = {}

    try:
        with open(Api().json_file, 'r', encoding='utf-8') as f:
            data = dict(json.load(f))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(Api().json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    unique_id = str(uuid.uuid4())
    data[unique_id] = new_entry

    with open(Api().json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
