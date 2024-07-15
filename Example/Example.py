# Author: Arabian Coconut
# Date: 06/07/2023
# Description: This is an example implementation for the API
import requests as req
import json

URL = "https://mc-api-j0rn.onrender.com/api/list"

data = req.get(URL, timeout=10).json()

new_data = json.dumps(data, indent=4)

# Convert str to dict
new_data = json.loads(new_data)

# get key Api_response and prints value link

if __name__ == "__main__":
    print(new_data[0])
