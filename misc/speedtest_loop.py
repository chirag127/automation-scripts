# https://www.speedtest.net/run open every 20 seconds

import pyautogui
from time import sleep
import webbrowser

while True:

    webbrowser.open("https://www.speedtest.net/run")

    sleep(1)

    pyautogui.hotkey("ctrl", "shift", "tab")




    pyautogui.hotkey("ctrl", "w")

    sleep(60)
