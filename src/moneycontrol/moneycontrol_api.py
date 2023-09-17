# Author: Arabian Coconut
# Last Modified: 17/09/2023 #DD/MM/YYYY
# Description: This file contains the API for getting the news from the moneycontrol website.
import os
import threading
import time
import moneycontrol.storage_control as sc
import uuid
import requests
from bs4 import BeautifulSoup
from functools import lru_cache



# Constants
class Api:
    """
    A class used to store constants
    """

    def __init__(self, title_info=None, link_info=None, date_info=None, news_info=None):
        """
        Initializes the constants
        """
        self.Data = {"NewsType": news_info, "Title": title_info,
                     "Link": link_info, "Date": date_info}
        self.json_file = sc.StorageControl("data.pkl").json_path()
        self.html_parser = "html.parser"
        self.url = ["https://www.moneycontrol.com/news", "https://www.moneycontrol.com/news/business",
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
        "ID":str(uuid.uuid4()),
        "NewsType": json_format["NewsType"],
        "Title": json_format["Title"],
        "Link": json_format["Link"],
        "Date": json_format["Date"]
    }
    
# Load the data into Pickle file
    sc_instance = sc.StorageControl("data.pkl")
    file_load = sc_instance.load()

    try:
        if file_load is None:
            sc_instance.save(new_entry)
        elif file_load.get("Title") != json_format["Title"]:
            sc_instance.save(new_entry)
        else:
            print("Data already exists")
    except FileNotFoundError:
        sc_instance.write(new_entry)