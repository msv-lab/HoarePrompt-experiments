import json

file_path = "/home/dimitris/HoarePrompt-data/PilotData/data/pilot_apps1_test.json"

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    print("JSON is valid!")
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
