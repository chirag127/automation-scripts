import keyboard
from time import sleep
import pyautogui


# define function to wait for z key
def wait_for_do_key():
    while True:
        if keyboard.is_pressed("alt + d"):
            break
        sleep(0.01)

# define function to close tab


def close_tab():
    pyautogui.hotkey("ctrl", "w")
