import pyautogui
import webbrowser
from functions import *


# Open the web browser and navigate to the URL https://www.youtube.com/feed/subscriptions


def open_subscriptions_page_in_edge():
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(
        "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))

    webbrowser.get('edge').open("https://www.youtube.com/feed/subscriptions")


# defining the function to click on the 3 dots button at (x,y) coordinates = (680,480)
def click_on_three_dots_on_subcription():
    pyautogui.moveTo(680, 471)
    pyautogui.click()


# defining the function to click on the checkbox button to select all videos on the page at (x,y) coordinates = (730,490)
def click_on_checkbox_on_subcription():
    pyautogui.moveTo(730, 490)
    pyautogui.click()


# defining the function to click on the "Add to queue" button at (x,y) coordinates = (800,570)
def click_on_add_to_queue_on_subcription():
    pyautogui.moveTo(730, 580)
    pyautogui.click()

# click on expand at 1400,680


def click_on_expand_on_subcription():
    pyautogui.moveTo(1400, 680)
    pyautogui.click()

# defining the function to click on the save button at (x,y) coordinates = (1350,270)
# click on the save above the queue playlist created by the addtop100toE function


def click_on_the_save_above_the_queue_playlist_created_by_the_add100totrans_function():
    pyautogui.moveTo(1350, 270)
    pyautogui.click()

# defining the function to click on the trans playlist at (x,y) coordinates = (880,500)
# click on the trans playlist after click on the save button above the queue playlist created by the addtop100toE function


def click_on_trans_playlist_after_click_on_the_save_button_above_the_queue_playlist_created_by_the_add100totrans_function():
    pyautogui.moveTo(880, 500)
    pyautogui.click()


def main():

    open_subscriptions_page_in_edge()

    sleep(10)

    click_on_three_dots_on_subcription()

    sleep(0.5)

    click_on_checkbox_on_subcription()

    sleep(0.5)

    click_on_add_to_queue_on_subcription()

    sleep(2)

    click_on_expand_on_subcription()

    sleep(1)

    click_on_the_save_above_the_queue_playlist_created_by_the_add100totrans_function()

    sleep(2)

    click_on_trans_playlist_after_click_on_the_save_button_above_the_queue_playlist_created_by_the_add100totrans_function()

    sleep(2)


if __name__ == '__main__':
    while True:

        wait_for_do_key()

        main()
