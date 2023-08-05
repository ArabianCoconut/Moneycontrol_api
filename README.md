
# MoneyControl Api
### Status of project: **Complete**
#### Author: Arabian Coconut
#### Version: 1.0.0

---
## Description

This is a python API for moneycontrol.com, which provides you with the news, latest news, and 
business news from moneycontrol.com in JSON format for your server's integration.

## How to use api
```shell
wget https://mc-api-j0rn.onrender.com/api/news 
wget https://mc-api-j0rn.onrender.com/api/latest_news
wget https://mc-api-j0rn.onrender.com/api/business_news
 ```
### Installation for local implementation

`pip install moneycontrol-api`

### Usage for local implementation

`from moneycontrol import moneycontrol_api as mc`

### Supported API functions

* get_news

* get_latest_news

* get_business_news

### Output format

``` json
{
  "News Type:": "Latest News",
  "Title:": "Chhattisgarh CM transfers Rs 15 crore online to beneficiaries as part of Godhan Nyay Yojana",
  "Link:": "https://www.moneycontrol.com/news/india/chhattisgarh-cm-transfers-rs-15-crore-online-to-beneficiaries-as-part-of-godhan-nyay-yojana-11103381.html",
  "Date:": "August 05, 2023 05:08 PM"
}
```