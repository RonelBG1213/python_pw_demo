import json

class JsonHandler:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def append_json(file_path, new_data):
        """
        Add new_data to the existing JSON file without removing current data.
        new_data should be a dict.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data.update(new_data)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def overwrite_json(file_path, new_data):
        """
        Clear all data from the JSON file and write new_data.
        new_data should be a dict.
        """
        with open(file_path, 'w') as f:
            json.dump(new_data, f, indent=4)
