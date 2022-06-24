# submit the issue by clicking on the submit button on the create new issue page of github and go to the next tab in the browser
# by pressing the hotkeys control+ tab

from functions import *
from time import sleep
import keyboard

# define the function to click on the submit button


def click_submit():

    pyautogui.click(x=1250, y=950)


def main():

    sleep(1)

    click_submit()

    go_to_next_tab()


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("z"):
            main()
