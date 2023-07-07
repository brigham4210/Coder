import json

with open("./../Json/maps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

one = data["one"]
two = data["two"]

# with open("two.json", "r", encoding="utf-8") as f:
#     two = json.load(f)
