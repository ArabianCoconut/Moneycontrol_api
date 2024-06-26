# MoneyControl Api

## Status of project: **Partially-Complete**

### Author: Arabian Coconut

#### Docker Version: 1.2.2

#### Local Version: 1.1.3

---

## Description

This is a python API for moneycontrol.com, which provides you with the news, latest news, and
business news from moneycontrol.com in JSON format for your server's integration.

Notes:

- This API is not affiliated with moneycontrol.com in any way.
- Master branch is for Docker deploy and Local branch is for local deploy.

## How to use API

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

- get_news

- get_latest_news

- get_business_news

- get_basic_price

### Output format

```json
{
  "NewsType:": "Latest News",
  "Title:": "Chhattisgarh CM transfers Rs 15 crore online to beneficiaries as part of Godhan Nyay Yojana",
  "Link:": "https://www.moneycontrol.com/news/india/chhattisgarh-cm-transfers-rs-15-crore-online-to-beneficiaries-as-part-of-godhan-nyay-yojana-11103381.html",
  "Date:": "August 05, 2023 05:08 PM"
}
```

---

## Changelog

- 1.2.2
  - Business news now uploads all news to the database. (BS database issues)
  - Now bandwidth will be focused on stock metrics.
- 1.2.1
  - Database for some reason deletes and inserts a few JSON entries. If bandwidth permits will revise the issue. However, the function will dump all 24 business news into a JSON file. Code modification is required from the user's end.
  - Classes are now moved to their file and StorageController is a class now.
  - This project will take a back seat due to limited bandwidth for this project.
- 1.2.0
  - Stock prices implemented(rudermentry). More elaborate price data will be supported.
  - **Limitation**: Currently due to the structuring of URLs of moneycontrol. Using the API may throw an error on /price/ endpoint if that is the case please raise an issue for me to correct the "symbol". Later on, the users themselves can contribute to correct "symbols" Moneycontrol uses different "shorthands" hence the limitation.
- 1.1.9
  - Integrated MongoDB for future stock metric implementation.
  - Removed previous Storage handling methods in favor of MongoDB.
- 1.1.8
  - Minor bug fixes and code cleanup.
  - Performance improvements.
- 1.1.7
  - Updated Home page for a modern look.
- 1.1.6
  - Modified Storage handling for better performance.
  - Removed static folder from the project as it is not a required folder.
- 1.1.5
  - Added a unique UUID for each request made to the server.
  - Updated function docs for a better understanding of the file_remove and dict_storage.
  - api_data.json is now deleted after 7 days of creation or updating.
  - Added new API for server status check.
- 1.1.4
  - Added LRU cache to reduce the load on the server
  - Added JSON storage for viewing all requests made to the server via /api/list for online demo implementation.
  - **Note**: Only Docker implementation is updated with this version for local implementation please use 1.1.3 from the master branch.

---

## Known Issues

- ~Business News doesn't upload all 19 links to the database. The code only uploads a few of them.~ Fixed in 1.2.2

---

## Buy me a Coffee :coffee:

<a href="https://www.buymeacoffee.com/arabiancoconut" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
