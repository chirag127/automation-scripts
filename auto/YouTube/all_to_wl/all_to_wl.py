from functions import *


def main():
    # click on the three dots on the search page
    multiselect = pyautogui.locateOnScreen('multiselect1.png')
    x_three_dots = multiselect[0] + 20
    y_three_dots = multiselect[1] + 10
    pyautogui.click(x_three_dots, y_three_dots)

    sleep(0.1)

    # click on the select all option
    x_select_all = x_three_dots - 100
    y_select_all = y_three_dots + 25
    pyautogui.click(x_select_all, y_select_all)

    sleep(0.1)

    # click on the save to watch later button
    x_save_to_wl = x_three_dots - 100
    y_save_to_wl = y_select_all + 150
    pyautogui.click(x_save_to_wl, y_save_to_wl)


if __name__ == "__main__":

    while True:

        try:

            wait_for_do_key()

            main()

        except Exception as e:

            print(e)

            sleep(1)
