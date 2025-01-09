import json
import os

#opening the JSON file
with open("C:/Users/17048/OneDrive/Documents/CL/Python Programs/Object_Recognition/train/annotations/project-2-at-2024-02-27-21-27-0bef95bb.json") as f:
    #instantiating JSON file as an obj
    data = json.load(f)
#loops through each object, collects image directory, and converts to text file
print("[")
for img in data:
    file_name = img["image"]
    file_name = file_name[11:-3] + "txt"
    print("\""+file_name+"\",")

    with open(file_name, "w") as g:
        json.dump(img, g, indent = 4)
print("]")