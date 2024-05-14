import json
import logging
from pymongo import MongoClient, errors
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
    DB_LOGIN= env.get("DB_LOGIN")

    try:
        client = MongoClient(DB_LOGIN)
        db = client.get_database(DB_NAME).get_collection(DB_COLLECTION)
        return db
    except Exception as e:
        print("Error in connecting to database open issue on GitHub. Error:",e)
        return None

# Working Example of Json Data.
def dump_all_data_to_json(filters=None):
    """
    Dumps all the data from the database to a JSON format
    """
    try:
        json_data = json.dumps(list(db_connection().find(filters)), indent=2, default=str)
        if json_data == "[]":
            return json.dumps(
        {
            "status": "No data found in the database.",
            "suggestion": "Please insert some data into the database using the /api/news endpoint."
            }, indent=2, default=str)
        elif filters is None:
            return json.dumps(list(db_connection().find()), indent=2, default=str)
        else:
            return json_data
    except errors as e:
        return ("Error:",e)


def insert_data_to_db(data, filters=None):
    """
    Inserts the given data into the database and also returns the inserted data

    Parameters:
    data (dict): The data to be inserted into the database
    filters (dict): Optional filters to apply when finding the inserted data
    """
    try:
        # db_connection().insert_one(data)
        db_connection().insert_many(documents=data)
        logging.info("Data Inserted Successfully")
        return dump_all_data_to_json(filters)
    except errors.BulkWriteError as e:
        str(e).strip("[]")
        logging.warning(f"Data already exists in the database. Error: {str(e)}")
        return dump_all_data_to_json(filters)
    except errors.DuplicateKeyError as e:
        logging.warning(f"Data already exists in the database. Error: {str(e)}")
        return dump_all_data_to_json(filters)




# Reference Code not to be deleted
# db_connection().delete_many({})
# db_connection().create_index([("Title", pymongo.ASCENDING)], unique=True)
#db_connection().drop_index("")
