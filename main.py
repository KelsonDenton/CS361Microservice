import json
from time import sleep

# write to JSON file
dict = {"url": "https://en.wikipedia.org/wiki/Peter_J._Denning", "title": "Education early life"}
json_obj = json.dumps(dict)
try:
    with open("wiki.json", "w") as openfile:
        openfile.write(json_obj)
finally:
    openfile.close()
sleep(1.0)


# read from JSON file
try:
    with open("wiki.json", "r") as openfile:
        wiki_info = json.load(openfile)
        data = wiki_info["text"]
finally:
    openfile.close()

print(data)
