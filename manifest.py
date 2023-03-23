import subprocess
import time
import pyautogui
import csv
import pyperclip


linesCsv = []
with open('Data - Sheet1.csv', mode='r') as file:
# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
        linesCsv.append(lines)



for i in range(1, len(linesCsv)):
    # opening the CSV file


    row = i

    # Read the URL and video file name from the specified columns
    url = linesCsv[row][5]
    filename = linesCsv[row][6]
    # Manifest link is [row][7]

    # define the URL to open in Safari




    time.sleep(2)
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Click the Safari icon to open Safari, Note: The browser must be Safari
    pyautogui.click(193, 1077)
    time.sleep(3)

    # Enter the url of the video
    pyautogui.write(url)
    pyautogui.press('enter')

    # Click play on the video
    time.sleep(8)
    pyautogui.click(767, 435)

    time.sleep(2)

    # Right click on the video to get it's manifest link
    pyautogui.rightClick(767,435)
    
    # Click on the copy video adress button to copy it's manifest link
    time.sleep(5)
    pyautogui.click(838, 638)
    
    # Pause the video
    time.sleep(2)
    pyautogui.click(798, 457)

    time.sleep(2)

    pyautogui.rightClick(767,445)
    
    
    time.sleep(2)
    pyautogui.click(838, 646)

    time.sleep(5)



    # Get the contents of the clipboard(which is the manifest link)
    manifest_link = pyperclip.paste()
    linesCsv[row][7] = manifest_link

    print(manifest_link)

    pyautogui.rightClick(193, 1077)

    pyautogui.click(203, 1005)

# Open a CSV file for writing
with open('Data2.csv', mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write each row of data to the CSV file
    for row in linesCsv:
        writer.writerow(row)
