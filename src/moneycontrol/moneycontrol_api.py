# Author: Arabian Coconut
# Last Modified: 02/01/2024 (DD/MM/YYYY)
# Description: This file contains the API for getting the news from the moneycontrol website.
import datetime
from functools import lru_cache

import requests
from bs4 import BeautifulSoup

import moneycontrol.storage_control as sc


# Constants
class Api:
    """
    A class used to store constants
    """

    def __init__(self, title_info=None, link_info=None, date_info=None, news_info=None):
        """
        Initializes the constants
        """
        self.Data = {
            "NewsType": news_info,
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
        }
        self.upload = sc.db_connection()
        self.html_parser = "html.parser"
        self.url = [
            "https://www.moneycontrol.com/news",
            "https://www.moneycontrol.com/news/business",
            "https://www.moneycontrol.com/news/latest-news/",
        ]


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
        date_info = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        json_output.Data.update(
            {
                "NewsType": "News",
                "Title": title_info,
                "Link": link_info,
                "Server_Time": date_info,
            }
        )
        json_output.upload.insert_one(json_output.Data)
        # if not json_output.upload.find_one({"Tile": json_output.Data["Title"]}):
        #     json_output.upload.insert_one(json_output.Data)
        #     return json_output.Data
        # else:
        #     return json_output.Data
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
    json_output.Data.update(
        {
            "NewsType": "Business News",
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
        }
    )
    if not json_output.upload.find_one({"Tile": json_output.Data["Title"]}):
        json_output.upload.insert_one(json_output.Data)
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
        json_output.Data.update(
            {
                "NewsType": "Latest News",
                "Title": title_info,
                "Link": link_info,
                "Date": date_info,
            }
        )
    if not json_output.upload.find_one({"Tile": json_output.Data["Title"]}):
        json_output.upload.insert_one(json_output.Data)
    return json_output.Data

# get_news()