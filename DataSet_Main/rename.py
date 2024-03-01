import os
import re
import json

# specify the directory you want to change the files in
directory = 'C:/Users/17048/objsmallpp/DataSet_Main/validation/annotations/'

for filename in os.listdir(directory):
    # print(filename)
    if filename.endswith(".txt"):
        with open(filename, 'r') as f:
            text  = f.read()
            text = text[1:-1]
            print(text)

        with open(directory + filename, 'w') as f:
            f.write(text)
        # find the part in parentheses
        # data = json.load(open(filename))
        # data["image"] = data["image"][11:]
        # print(data)
        # with open(directory+filename, 'w') as outfile:
        #     json.dump(data, outfile)
        # # match = re.search(r'\((.*?)\)', filename)
        # # if match:
        # #     # get the number in parentheses
        # #     number = match.group(1)
        # #     # create the new filename
        # #     new_filename = filename.replace(f' ({number})', f'_{number}')
        # #     print(f'Old: {filename}, New: {new_filename}')
        # #     # rename the file
        # #     os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))