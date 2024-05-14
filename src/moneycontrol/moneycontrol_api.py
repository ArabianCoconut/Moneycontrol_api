# Author: Arabian Coconut
# Last Modified: 14/05/2024 (DD/MM/YYYY)
# Description: This file contains the API for getting the news and price from the moneycontrol website.
from functools import lru_cache
from os import environ as env

import requests
from bs4 import BeautifulSoup
from dotenv import find_dotenv, load_dotenv
from moneycontrol.Classes import Api

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

    for i in soup_process:
        title_info = i.find("a").get("title")
        link_info = i.find("a").get("href")
        Api().StorageController.insert_data_to_db(data={
                "NewsType": "News",
                "Title": title_info,
                "Link": link_info,
                "Api_Called": Api().date,
            }
        )
        return Api().StorageController.dump_all_data_to_json(filters={"NewsType": "News"})


@lru_cache(maxsize=30)
def get_business_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(Api().url[1], timeout=60).text, Api().html_parser)
    news_list = list(map(lambda x: "newslist-" + str(x), range(24)))

    for i in range(len(news_list)):
        process = soup.find("li", {"class": "clearfix", "id": news_list[i]})
        title_info = process.find("h2").find("a").get("title")
        link_info = process.find("h2").find("a").get("href")
        date_info = process.find("span").get_text()
        Api().StorageController.insert_data_to_db(data={
            "NewsType": "Business News",
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
            "Api_Called": Api().date
        })
        return Api().StorageController.dump_all_data_to_json(filters={"NewsType": "Business News"})


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

    soup = BeautifulSoup(requests.get(Api().url[2], timeout=60).text, Api().html_parser)
    # Get the title, link and date of the news
    related_des_class = soup.find_all("h3", {"class": "related_des"})
    related_date_class = soup.find_all("p", {"class": "related_date hide-mob"})
    for h3_tag, p_tag in zip(related_des_class, related_date_class):
        title_info = h3_tag.find("a").get("title")
        link_info = h3_tag.find("a").get("href")
        date_info = p_tag.text
        Api().StorageController.insert_data_to_db(data={
            "NewsType": "Latest News",
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
            "Api_Called": Api().date
        })
    return Api().StorageController.dump_all_data_to_json(filters={"NewsType": "Latest News"})


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
