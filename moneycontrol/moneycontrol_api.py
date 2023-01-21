from bs4 import BeautifulSoup
import requests,json

# Api for getting the latest news from moneycontrol.com

# Constants
title_text="Title:"
link_text="Link:"
date_text="Date:"
html_parser="html.parser"
news_type="News Type:"


# Urls for getting the news
url=["https://www.moneycontrol.com/news",
"https://www.moneycontrol.com/news/business",
"https://www.moneycontrol.com/news/latest-news/"]

def get_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(url[0],timeout=60).text, html_parser)
    # Get the title, link and date of the news
    related_des_class = soup.find_all("h3", {"class": "related_des"})
    related_date_class = soup.find_all("p", {"class": "related_date hide-mob"})
    for h3_tag,p_tag in zip(related_des_class, related_date_class):
        title = h3_tag.find("a").get("title")
        link = h3_tag.find("a").get("href")
        date = p_tag.text
        json_data = {news_type:"News", title_text: title, link_text: link, date_text: date }
        return json.dumps(json_data, indent=0)

def get_business_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(url[1],timeout=60).text, html_parser)
    # Get the title, link and date of the news
    for i in range(1, 24):
        new_list = "newslist-"+str(i)
        news_list = soup.find("li", {"class": "clearfix", "id": new_list})
        news_list_heading_2=soup.find("h1",{"class":"fleft"})
        if news_list:
            title_class = news_list.find("h2").find("a")
            title = title_class.get("title")
            link = title_class.get("href")
            date_class = news_list.find("span")
            date = date_class.text
            print(news_type,news_list_heading_2.text)
            json_data = {news_type:news_list_heading_2.text ,
            title_text: title, link_text: link, date_text: date }
            return json.dumps(json_data, indent=0)
        else:
            print(f"li element with class 'clearfix' and id '{id}' not found.")
            return None

def get_latest_news():
    """
    Gets the news from the given URL and returns a JSON object containing the title, link,
    and date of the news.

    Parameters:
    url (string): The URL from which to retrieve the news

    Returns:
    json_data (JSON object): A JSON object containing the title, link, and date of the news
    """
    soup = BeautifulSoup(requests.get(url[2],timeout=60).text, html_parser)
    # Get the title, link and date of the news
    related_des_class = soup.find_all("h3", {"class": "related_des"})
    related_date_class = soup.find_all("p", {"class": "related_date hide-mob"})
    for h3_tag,p_tag in zip(related_des_class, related_date_class):
        title = h3_tag.find("a").get("title")
        link = h3_tag.find("a").get("href")
        date = p_tag.text
        json_data = {news_type:"Latest News", title_text: title, link_text: link, date_text: date}
        return json.dumps(json_data, indent=0)
