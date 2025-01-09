import json
import os

directory = 'C:/Users/17048/face_detector/train/annotations/'

for filename in os.listdir(directory):
    text = ""
    #gets file data
    with open(directory+filename,'r') as f:
        text = f.read()
    #changes filename
    filename = filename[0:-3]+"json"
    print(filename)
    with open(directory+filename,'w') as f:
        f.write("{\n"+text+"\n}")
