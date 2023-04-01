import json

def load_database(fName):
    with open(fName) as db_file:
        return json.load(db_file)

def save_database(fName):
    with open(fName, 'w') as db_file:
        return json.dump(database, db_file)

database = load_database("flash.json")