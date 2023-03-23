# This program gives the coordinates of the mouse cursor, this can be used to tweak the values in the manifest.py's click coordinates
import pyautogui

# Get the current position of the mouse cursor
x, y = pyautogui.position()

# Print the coordinates
print("x-coordinate:", x)
print("y-coordinate:", y)
