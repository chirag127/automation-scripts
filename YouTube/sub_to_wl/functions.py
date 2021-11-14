import time
import keyboard
import pyautogui


def wait(x):
    time.sleep(x)


# defining the function to wait for user to press z key
def wait_for_z_key():
    while True:
        if keyboard.is_pressed('z'):
            break
        time.sleep(0.1)

# defining the function to close the tab


def close_tab():
    pyautogui.hotkey('ctrl', 'w')
