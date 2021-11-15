from functions import *


# Unsubscribe from every channel in the list


# define a function that will click the unsubscribe button
def click_on_unsubscribe_button():
    pyautogui.click(x=1050, y=600)


# define a function that will click the unsubscribe button in the pop up
def click_on_unsubscribe_button_in_pop_up():
    pyautogui.click(x=1050, y=600)


def main():

    click_on_unsubscribe_button()

    sleep(0.1)

    click_on_unsubscribe_button_in_pop_up()

    sleep(0.1)

    close_tab()
