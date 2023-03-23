import subprocess
import csv
import time

import pyautogui

# The libraries that have to be downloaded:
# subprocess
# csv
# pyautogui


path_Manifest = "path to the folder that you want to put the mp4's in"
linesCsv = []
with open('Data2.csv', mode='r') as file:
# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
        linesCsv.append(lines)

for i in range(1, len(linesCsv)): # The start not including the top row where the titles are
    row = i
    path_Manifest = "path to the folder that you want to put the mp4's in"

    # Read the URL and video file name from the specified columns
    url = linesCsv[row][5]
    filename = linesCsv[row][6]
    manifest =  linesCsv[row][7]
    path_Manifest += (filename + ".mp4")
    command = "ffmpeg -i " + '"' + manifest + '"' + " -c copy " + path_Manifest


    subprocess.run(command, shell=True, check=True, input=None, text=True)

    #print(filename + " was downloaded")



