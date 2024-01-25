import pymongo
import pickle
import os
from dotenv import load_dotenv,find_dotenv
from os import environ as env

load_dotenv(find_dotenv())
DB_CONNECTION= env.get("DB_CONNECTION")+env.get("DB_CONNECTION_VARIABLES")
DB_NAME = env.get("DB_NAME")
DB_COLLECTION = env.get("DB_COLLECTION")

# @DeprecationWarning("This class is deprecated, use db_connection instead")
class StorageControl:
    def __init__(self, file_name):
        self.file_name = "moneycontrol/" + file_name
        try:
            open(self.file_name, "xb").close()
        except FileExistsError:
            return None
        except FileNotFoundError:
            open(self.file_name, "wb").close()

    def json_path(self):
        return "moneycontrol/data.json"

    def save(self, data):
        existing_data = self.load()
        if existing_data is None or not isinstance(existing_data, list):
            existing_data = []
        existing_data.append(data)
        with open(self.file_name, "wb") as file:
            pickle.dump(existing_data, file)

    def load(self):
        if os.path.getsize(self.file_name) > 0:
            with open(self.file_name, "rb") as file:
                return pickle.load(file)
        else:
            return None

    def write(self, data):
        with open(self.file_name, "wb") as file:
            pickle.dump(data, file)

def db_connection():
    try:
        client = pymongo.MongoClient(DB_CONNECTION)
        print(client)
        db = client.get_database(DB_NAME).get_collection(DB_COLLECTION)
        db.insert_one({"test":"test"})
        return db
    except Exception as e:
        print("Error in connecting to database open issue on GitHub. Error:",e)
        return None

db_connection()