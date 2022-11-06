
from time import sleep
import pyautogui
import keyboard



def main() -> None:

    current_x, current_y = pyautogui.position()

    pyautogui.rightClick(current_x,current_y)

    sleep(0.5)

    pyautogui.click(current_x + 103,current_y + 226)

    sleep(0.3)

    pyautogui.click(1096, 565)



if __name__ == "__main__":

    while True:
        if keyboard.is_pressed("ctrl + a"):
            main()
        else:
            sleep(0.1)