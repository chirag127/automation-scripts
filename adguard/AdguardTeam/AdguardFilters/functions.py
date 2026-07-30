from urllib.parse import urlparse
import clipboard
import pyautogui


def open_last_closed_tab():
    """
    This function opens the last closed tab
    """
    pyautogui.hotkey("ctrl", "shift", "t")


def close_tab():
    """
    This function closes the current tab
    """
    pyautogui.hotkey("ctrl", "w")


def go_to_next_tab():
    """
    This function goes to the next tab
    """
    pyautogui.hotkey("ctrl", "tab")


def copy_selected_text():

    """
    This function copies the selected text
    """
    pyautogui.hotkey("ctrl", "c")


def type_domain() -> None:
    """
    This function types the domain name of the website
    """
    # get the url of the website by using the clipboard
    url = clipboard.paste()
    # parse the url to get the domain name
    domain = urlparse(url).netloc
    pyautogui.typewrite(domain)
