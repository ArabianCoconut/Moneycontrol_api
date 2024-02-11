import json
import pymongo
from dotenv import load_dotenv,find_dotenv
from os import environ as env

def db_connection():
    """Summary
    Connects to the database and returns the database object

    Returns:
    db (object): The database object
    """   
    # Reloads the environment variables
    load_dotenv(dotenv_path=find_dotenv(),override=True,verbose=True)

    DB_NAME = env.get("DB_NAME")
    DB_COLLECTION = env.get("DB_COLLECTION")
    URL_BUILD= env.get("DB_LOGIN")

    try:
        client = pymongo.MongoClient(URL_BUILD)
        db = client.get_database(DB_NAME).get_collection(DB_COLLECTION)
        print("Connected to database")
        return db
    except Exception as e:
        print("Error in connecting to database open issue on GitHub. Error:",e)
        return None

# Working Example of Json Data.
data = list(db_connection().find())
json_data = json.dumps(data, indent=4, default=str)
print(json_data)