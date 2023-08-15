
# MoneyControl Api
### Status of project: **Complete**
#### Author: Arabian Coconut
#### Docker Version: 1.1.5
#### Local Version: 1.1.3

---
## Description

This is a python API for moneycontrol.com, which provides you with the news, latest news, and 
business news from moneycontrol.com in JSON format for your server's integration.

## How to use api
```shell
wget https://mc-api-j0rn.onrender.com/api/news 
wget https://mc-api-j0rn.onrender.com/api/latest_news
wget https://mc-api-j0rn.onrender.com/api/business_news
wget https://mc-api-j0rn.onrender.com/api/list
wget https://mc-api-j0rn.onrender.com/api/status
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
  "NewsType:": "Latest News",
  "Title:": "Chhattisgarh CM transfers Rs 15 crore online to beneficiaries as part of Godhan Nyay Yojana",
  "Link:": "https://www.moneycontrol.com/news/india/chhattisgarh-cm-transfers-rs-15-crore-online-to-beneficiaries-as-part-of-godhan-nyay-yojana-11103381.html",
  "Date:": "August 05, 2023 05:08 PM"
}
```
---
## Changelog
* 1.1.4
    * Added LRU cache to reduce load on server
    * Added json storage for viewing all requests made to server via /api/list for online demo implementation.
    * **Note**: Only Docker implementation is updated with this version for local implementation please use 1.1.3 from master branch.
* 1.1.5
  * Added unique UUID for each request made to server.
  * Updated function docs for better understanding of the file_remove and dict_storage.
  * api_data.json is now deleted after 7 days of creation or updating.
  * Added new api for server status check.

---
## Buy me a Coffee :coffee:
<a href="https://www.buymeacoffee.com/arabiancoconut" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
