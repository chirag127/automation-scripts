import pyautogui
from time import sleep
while True:

    button = pyautogui.locateOnScreen('sub.png')
    if button:
        pyautogui.click(button)
    else:
        print("Button not found")
        sleep(1)
