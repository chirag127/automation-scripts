

import os
from time import sleep
import pyautogui
import requests


def return_image_path(path, url):

    if not bool(os.path.exists(path)):
        print("No image found")

        response = requests.get(url)

        with open(path, "wb") as f:
            f.write(response.content)

    else:

        print("Image found")
    return path

def main():


    button7location = pyautogui.position()

    pyautogui.click(button7location)

    buttonx, buttony = button7location

    sleep(0.5)

    pyautogui.click(buttonx, buttony + 90)

    sleep(.4)

    pyautogui.click(1174, 618)

    pyautogui.moveTo(button7location)






import keyboard


if __name__ == "__main__":
    sleep(3)

    while True:
        if keyboard.is_pressed("q"):
            print("q pressed")
            main()
        else:
            sleep(0.1)