import datetime
import requests
import storage_control as sc
from bs4 import BeautifulSoup

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
        # self.upload = sc.db_connection()
        self.html_parser = "html.parser"
        self.url = [
            "https://www.moneycontrol.com/news",
            "https://www.moneycontrol.com/news/business",
            "https://www.moneycontrol.com/news/latest-news/",
        ]

def get_business_news():  #* CODE FIXED?
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