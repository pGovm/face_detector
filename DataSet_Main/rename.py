import os
import re

# specify the directory you want to change the files in
directory = '/home/nitin/objsmallpp/DataSet_Main/validation/images'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # find the part in parentheses
        match = re.search(r'\((.*?)\)', filename)
        if match:
            # get the number in parentheses
            number = match.group(1)
            # create the new filename
            new_filename = filename.replace(f' ({number})', f'_{number}')
            print(f'Old: {filename}, New: {new_filename}')
            # rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))