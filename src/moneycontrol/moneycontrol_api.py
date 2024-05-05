# Author: Arabian Coconut
# Last Modified: 21/03/2024 (DD/MM/YYYY)
# Description: This file contains the API for getting the news from the moneycontrol website.
import datetime
from functools import lru_cache
from os import environ as env

import requests
from bs4 import BeautifulSoup
from dotenv import find_dotenv, load_dotenv

import moneycontrol.storage_control as sc


# Constants
class Api:
    """
    A class used to store constants
    """

    def __init__(self):
        """
        Initializes the constants
        """
        self.Data = {
            "NewsType": None,
            "Title": None,
            "Link": None,
            "Date": None,
            "API_CALLED": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
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
        json_output.Data.update(
            {
                "NewsType": "News",
                "Title": title_info,
                "Link": link_info,
            }
        )
        return sc.insert_data_to_db(json_output.Data, filters={"NewsType": "News"})


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
    news_list = list(map(lambda x: "newslist-" + str(x), range(20)))
    processedData= list()

    for i in range(0,len(news_list)):
        process = soup.find("li", {"class": "clearfix", "id": news_list[i]})
        title_info = process.find("h2").find("a").get("title")
        link_info = process.find("h2").find("a").get("href")
        date_info = process.find("span", {"class": "list_dt"})
        json_output.Data.update({
            "NewsType": "Business News",
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
        })
        processedData.append(json_output.Data.copy())

    try:
        sc.insert_data_to_db(data=processedData)
        print("Data inserted successfully.")
    except Exception as e:
        print("Error in inserting data into the database. Error:", e)


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
    processed_data = []
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
        processed_data.append(json_output.Data.copy())
    return sc.insert_data_to_db(processed_data, filters={"NewsType": "Latest News"})


def get_basic_price(symbol):
    load_dotenv(dotenv_path=find_dotenv(), override=True)
    HIDDEN_URL = env.get("HIDDEN_URL")
    r = requests.get(
        f"{HIDDEN_URL}scIdList={symbol}&scId={symbol}",
        timeout=60,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
        },
    )
    return r.json()
