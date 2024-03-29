
# MoneyControl Api

## Status of project: **Partially-Complete**

### Author: Arabian Coconut

#### Docker Version: 1.1.9

#### Local Version: 1.1.3

---

## Description

This is a python API for moneycontrol.com, which provides you with the news, latest news, and
business news from moneycontrol.com in JSON format for your server's integration.

Notes:

* This API is not affiliated with moneycontrol.com in any way.
* Master branch is for Docker deploy and Local branch is for local deploy.

## How to use api

```shell
wget https://mc-api-j0rn.onrender.com/api/news
wget https://mc-api-j0rn.onrender.com/api/latest
wget https://mc-api-j0rn.onrender.com/api/business
wget https://mc-api-j0rn.onrender.com/api/list
wget https://mc-api-j0rn.onrender.com/api/status
wget https://mc-api-j0rn.onrender.com/price/TCS
 ```

### Installation for local implementation

`pip install moneycontrol-api`

### Usage for local implementation

`from moneycontrol import moneycontrol_api as mc`

### Supported API functions

* get_news

* get_latest_news

* get_business_news

* get_basic_price

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
* 1.2.0
  * Stock prices implemented(rudermentry). More elaborate price data will be supported.
  * **Limitation**: Currently due to the structuring of URLs of moneycontrol. Using the API may throw an error on /price/ endpoint if thats the case please raise an issue for me to correct the "symbol". Later on the users themselves can contribute to correct "symbols" moneycontrol uses different "shorthands" hence the limitation.
* 1.1.9
  * Integrated MongoDB for future stock metric implementation.
  * Removed previous Storage handling methods in favour of MongoDB.
* 1.1.8
  * Minor bug fixes and code cleanup.
  * Performance improvements.
* 1.1.7
  * Updated Home page for modern look.
* 1.1.6
  * Modified Storage handling for better performance.
  * Removed static folder from the project as its not required folder.
* 1.1.5
  * Added a unique UUID for each request made to the server.
  * Updated function docs for better understanding of the file_remove and dict_storage.
  * api_data.json is now deleted after 7 days of creation or updating.
  * Added new API for server status check.
* 1.1.4
  * Added LRU cache to reduce the load on the server
  * Added JSON storage for viewing all requests made to the server via /api/list for online demo implementation.
  * **Note**: Only Docker implementation is updated with this version for local implementation please use 1.1.3 from the master branch.

---

## Buy me a Coffee :coffee

<a href="https://www.buymeacoffee.com/arabiancoconut" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
