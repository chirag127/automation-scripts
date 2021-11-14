import pyautogui
from functions import *

# Load all result on the youtube search page


def main():

    for i in range(1, 30):

        pyautogui.press('end')

        wait(1.5)


if __name__ == "__main__":

    wait_for_do_key()

    main()
