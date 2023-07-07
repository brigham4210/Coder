import json

with open("Json/mappers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

one = data["one"]
two = data["two"]

