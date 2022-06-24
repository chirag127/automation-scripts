from time import sleep
from urllib.parse import urlparse
import clipboard
import keyboard
import pyautogui
import pyautogui
import webbrowser


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():
    pyautogui.hotkey("ctrl", "shift", "t")


# define a function that will close tab
def close_tab():
    pyautogui.hotkey("ctrl", "w")


# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')


def go_to_next_tab():
    pyautogui.hotkey("ctrl", "tab")


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copy_selected_text():
    pyautogui.hotkey("ctrl", "c")


def type_domain():

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    pyautogui.typewrite(domain)
