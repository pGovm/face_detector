# Kanye West Face Detector

## Introduction

I started this project to gain a deeper understanding of Python programming and custom object detection model. For the code to function, the user will need to train the yolo v3 model with the desired target first. 

To setup the project:
- Create 2 folders, in the same directory, 'train' and 'validation'.
  - 'train' is the first folder the yolo model goes through and learns which target said model should go look to put bounding box around.
  - 'validation' is the second folder the yolo model goes through and verifies weither the target and bounding box are correctly idenitifies and placed respectively.
- Both of those folders should each have 2 subfolders, 'annotations' and 'images'.
  - The 'images' folder should have the original pictures with the intended target.
  - The 'annotations' folder will have the same pictures with the addition of bounding boxes around the target.

If the user is not using a pre-existing dataset and scrapping pitcures from the internet, like I did, the rename, txt_to_json, j-py

## Table of Contents

- [Installation](#installation)
- 

I started by scrapping the internet for pictures of Kanye West using Image Downloader. I then used Microsoft Power Toys to rename all of the images to a sequential name without spaces and change the resolution of all of the images. I then used Label Studio to annotate over 600 pictures and exported the images. I accidentally exported the images incorrectly, so I created a few string manipulation scripts to fix the formatting. I finally trained the images using the imageai python module. In the end, my model has a 75% accuracy with room to improve in more challenging photos. 
