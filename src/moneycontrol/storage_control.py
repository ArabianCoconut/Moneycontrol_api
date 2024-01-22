import os
import pickle


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