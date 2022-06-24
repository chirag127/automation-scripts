# Physical: {X=594,Y=609}
# Physical: {X=1206,Y=745}

import pyautogui
from time import sleep


def main():
    # press end
    pyautogui.press("end")

    sleep(0.1)

    pyautogui.click(594, 609)

    sleep(0.1)

    pyautogui.hotkey("ctrl", "v")

    sleep(0.1)

    pyautogui.hotkey("ctrl", "enter")

    sleep(0.1)

    pyautogui.hotkey("ctrl", "tab")


if __name__ == "__main__":

    sleep(5)
    for _ in range(10):
        main()
