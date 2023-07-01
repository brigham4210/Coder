import json

with open("Json/one.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i in data:
    print(i)
