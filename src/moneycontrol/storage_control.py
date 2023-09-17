import pickle
import json
import os

class StorageControl:
    def __init__(self, file_name):
        self.file_name = "moneycontrol/"+file_name
        try:
            open(self.file_name, 'xb').close()
        except FileExistsError:
            pass
        
    def json_path(self):
        return "moneycontrol/data.json"
    
    def save(self, data):
        with open(self.file_name, 'ab') as file:
            pickle.dump(data, file)

    def load(self):
        if os.path.getsize(self.file_name) > 0:
            return pickle.load(open(self.file_name, 'rb'))
        else:
            pass
    def write(self, data):
        with open(self.file_name, 'wb') as file:
            pickle.dump(data, file)


    def convert_to_json(self):
        data = []
        json_file_path = self.json_path()
        with open(self.file_name, 'rb') as file:
            while True:
                try:
                    data.append(pickle.load(file))
                except EOFError:
                    break
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)