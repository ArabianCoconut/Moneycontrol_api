import requests
import datetime
from bs4 import BeautifulSoup
import storage_control as sc

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
            "API_CALLED": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # self.upload = sc.db_connection()
        self.html_parser = "html.parser"
        self.url = [
            "https://www.moneycontrol.com/news",
            "https://www.moneycontrol.com/news/business",
            "https://www.moneycontrol.com/news/latest-news/",
        ]

def get_business_news():  #! Problem with Webscraper
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

    i = 0
    while i < len(news_list)-1:
        process = soup.find("li", {"class": "clearfix", "id": news_list[i]})
        title_info = process.find("h2").find("a").get("title")
        link_info = process.find("h2").find("a").get("href")
        date_info = process.find("span", {"class": "list_dt"})
        json_output.Data.update(
            {
            "NewsType": "Business News",
            "Title": title_info,
            "Link": link_info,
            "Date": date_info,
            }
        )
        i += 1
        return sc.insert_data_to_db(json_output.Data, filters={"NewsType": "Business News"})    
