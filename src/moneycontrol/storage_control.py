import json
import pymongo
import pymongo.errors
from dotenv import load_dotenv,find_dotenv
from os import environ as env

def db_connection():
    """Summary
    Connects to the database and returns the database object

    Returns:
    db (object): The database object
    """   
    # Reloads the environment variables
    load_dotenv(dotenv_path=find_dotenv(),override=True)

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
def dump_all_data_to_json():
    """
    Dumps all the data from the database to a JSON format
    """
    json_data = json.dumps(list(db_connection().find()), indent=2, default=str)
    return json_data


def insert_data_to_db(data,filters=None):
    """
    Inserts the given data into the database and also returns the inserted data

    Parameters:
    data (dict): The data to be inserted into the database
    """
    try:
        db_connection().insert_one(data)
        return json.dumps(db_connection().find_one(filters), indent=2, default=str)
    except pymongo.errors.DuplicateKeyError as e:
        return ("Duplicate Key Error Occurred. Skipping the insertion.",e)

