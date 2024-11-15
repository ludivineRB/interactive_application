import json

def load_json(option):
    with open(f'./theme/{option}.json', "r") as file:
        data=json.load(file)
    return data