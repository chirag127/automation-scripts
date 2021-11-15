from functions import *


# Unsubscribe from every channel in the list


# define a function that will click the unsubscribe button
def click_on_unsubscribe_button():
    pyautogui.click(x=1679, y=220)


# define a function that will click the unsubscribe button in the pop up
def click_on_unsubscribe_button_in_pop_up():
    pyautogui.click(1038, 590)


def main():

    click_on_unsubscribe_button()

    sleep(0.1)

    click_on_unsubscribe_button_in_pop_up()

    sleep(0.1)

    # close_tab()


if __name__ == '__main__':
    wait_for_do_key()

    for i in range(1, 5):
        main()
