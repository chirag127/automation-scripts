# Physical: {X=1222,Y=625};
# Physical: {X=1279,Y=538};
# Physical: {X=995,Y=592};
# Physical: {X=817,Y=305};
# Physical: {X=794,Y=822};
# Physical: {X=1133,Y=923};
# Physical: {X=1235,Y=711};
# Physical: {X=612,Y=801};
# Physical: {X=1202,Y=771};
from time import sleep
import pyautogui
import os
import webbrowser


def main():

    webbrowser.open("https://takeout.google.com/u/1/")

    sleep(5)

    pyautogui.press("end")

    sleep(1)

    for _ in range(10):
        pyautogui.press("pageup")

    sleep(1)

    pyautogui.press("end")

    pyautogui.click(1222, 351)

    sleep(1)

    pyautogui.click(1279, 538)

    sleep(1)

    pyautogui.click(995, 592)

    sleep(1)

    pyautogui.click(817, 305)

    sleep(1)
    pyautogui.scroll(-30)

    pyautogui.click(794, 822)

    sleep(1)

    pyautogui.click(1133, 923)

    sleep(1)

    pyautogui.click(1235, 711)

    sleep(1)

    pyautogui.click(612, 801)

    sleep(1)

    pyautogui.press("end")

    sleep(1)

    pyautogui.click(1202, 771)


if __name__ == "__main__":

    main()
