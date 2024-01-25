import pymongo
from dotenv import load_dotenv,find_dotenv
from os import environ as env

def db_connection():
    """Summary
    Connects to the database and returns the database object

    Returns:
    db (object): The database object
    """
    load_dotenv(find_dotenv())
    DB_NAME = env.get("DB_NAME")
    DB_COLLECTION = env.get("DB_COLLECTION")
    URL_BUILD= env.get("DB_LOGIN")+env.get("DB_URL")
    try:
        client = pymongo.MongoClient(URL_BUILD)
        db = client.get_database(DB_NAME).get_collection(DB_COLLECTION)
        print("Connected to database")
        return db
    except Exception as e:
        print("Error in connecting to database open issue on GitHub. Error:",e)
        return None

# db_connection()