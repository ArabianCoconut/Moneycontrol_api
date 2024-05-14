import datetime
import json
import logging
from pymongo import MongoClient, errors
from dotenv import load_dotenv,find_dotenv
from os import environ as env


class Api:
    """
    A class used to store constants
    """

    def __init__(self):
        """
        Initializes the constants
        """
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.StorageController = StorageController()
        self.html_parser = "html.parser"
        self.url = [
            "https://www.moneycontrol.com/news",
            "https://www.moneycontrol.com/news/business",
            "https://www.moneycontrol.com/news/latest-news/",
        ]



class StorageController:
    def __init__(self):
        """Summary
        Initializes the StorageController class
        """
        # Reloads the environment variables
        load_dotenv(dotenv_path=find_dotenv(), override=True)

        self.DB_NAME = env.get("DB_NAME")
        self.DB_COLLECTION = env.get("DB_COLLECTION")
        self.DB_LOGIN = env.get("DB_LOGIN")
        self.client = MongoClient(self.DB_LOGIN)
        self.db = self.client.get_database(self.DB_NAME).get_collection(self.DB_COLLECTION)

    def connect_to_db(self):
        """Summary
        Connects to the database and returns the database object

        Returns:
        db (object): The database object
        """
        try:
            self.client = MongoClient(self.DB_LOGIN)
            self.db = self.client.get_database(self.DB_NAME).get_collection(self.DB_COLLECTION)
            return self.db
        except Exception as e:
            print("Error in connecting to database. Error:", e)
            return None

    def dump_all_data_to_json(self, filters=None):
        """
        Dumps all the data from the database to a JSON format

        Parameters:
        filters (dict): Optional filters to apply when finding the data

        Returns:
        json_data (str): The data in JSON format
        """
        try:
            json_data = json.dumps(list(self.connect_to_db().find(filters)), indent=2, default=str)
            if json_data == "[]":
                return json.dumps(
                    {
                        "status": "No data found in the database.",
                        "suggestion": "Please insert some data into the database using the /api/news endpoint."
                    }, indent=2, default=str)
            elif filters is None:
                return json.dumps(list(self.connect_to_db().find()), indent=2, default=str)
            else:
                return json_data
        except errors as e:
            return ("Error:", e)

    def insert_data_to_db(self,data, filters=None):
        """
        Inserts the given data into the database and also returns the inserted data

        Parameters:
        data (dict): The data to be inserted into the database
        filters (dict): Optional filters to apply when finding the inserted data

        Returns:
        json_data (str): The inserted data in JSON format
        """
        try:
            if isinstance(data, list):
                self.connect_to_db().insert_many(documents=data)
            else:
                self.connect_to_db().insert_one(data)
            logging.info("Data Inserted Successfully")
            return self.dump_all_data_to_json(filters)

        except errors.BulkWriteError as e:
            str(e).strip("[]")
            logging.warning(f"Data already exists in the database. Error: {str(e)}")
            return self.dump_all_data_to_json(filters)
        except errors.DuplicateKeyError as e:
            logging.warning(f"Data already exists in the database. Error: {str(e)}")
            return self.dump_all_data_to_json(filters)