from time import sleep
import keyboard
import pyautogui

# Physical: {X=286,Y=448};
# Physical: {X=344,Y=499};
# Physical: {X=1720,Y=165}
# Physical: {X=1677,Y=270}
# Physical: {X=659,Y=447};
# Physical: {X=802,Y=518};
# Physical: {X=1447,Y=706}
def main() -> None:
    "create a new untitled project"
    "integration to a"
    pyautogui.click(286, 448)
    pyautogui.click(344, 499)
    sleep(3)
    pyautogui.click(170, 230)
    sleep(1)
    pyautogui.click(646, 463)
    sleep(1)
    pyautogui.click(642, 519)
    pyautogui.typewrite("drive")
    pyautogui.click(1441, 710)
    sleep(1)


def main2() -> None:
    """
    This is a multi-line Google style docstring.

    Args:
        None

    Returns:
        None
    """
    pyautogui.click(1440, 197)
    sleep(1)
    pyautogui.click(1345, 252)
    sleep(1)
    pyautogui.click(702, 548)
    sleep(1)
    pyautogui.click(669, 584)
    sleep(1)
    pyautogui.click(657, 613)
    sleep(1)
    pyautogui.click(863, 563)
    sleep(1)
    pyautogui.click(1213, 700)
    sleep(1)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("ctrl + q"):
            main()
        if keyboard.is_pressed("ctrl + b"):
            main2()
        else:
            sleep(0.1)
