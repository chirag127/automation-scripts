import pyautogui
import webbrowser
import os
import requests
from time import sleep

# import a library that gives random usernames
from random_username.generate import generate_username
def main():

    # Open a URL named deepnote.com and then click the coordinates mentioned above with the time delay of one second

    webbrowser.open(
        "https://deepnote.com/workspace/alex-434a-d58c183a-4cc9-4920-8d07-0df4a72c49b8/create-new-workspace"
    )

    sleep(10)
    # Physical: {X=732,Y=624}


    pyautogui.click(732, 624, duration=1)

    sleep(1)

    pyautogui.click(824, 490)

    sleep(1)

    pyautogui.typewrite(generate_username(1)[0])

    pyautogui.click(621, 595)

    sleep(1)

    pyautogui.click(609, 644)

    sleep(1)

    pyautogui.click(1682, 648)

    sleep(1)

    pyautogui.click(1664, 734)


    def return_image_path(path, url):

        if not bool(os.path.exists(path)):
            print("No image found")

            response = requests.get(url)

            with open(path, "wb") as f:
                f.write(response.content)

        else:
            print("Image found")

        return path

    while True:

        path = return_image_path(
            "brave_new_topic_button.png", "https://i.imgur.com/3IMzEJ8.png"
        )
        brave_new_topic_button = pyautogui.locateOnScreen(path, confidence=0.8)

        if brave_new_topic_button is not None:
            break

        else:

            sleep(1)

    pyautogui.click(286, 448)


    pyautogui.click(344, 499)

    sleep(3)

# Physical: {X=170,Y=230};
# Physical: {X=646,Y=463};
# Physical: {X=642,Y=519};
# Physical: {X=1441,Y=710};

    pyautogui.click(170, 230)

    sleep(1)

    pyautogui.click(646, 463)

    sleep(1)

    pyautogui.click(642, 519)

    pyautogui.typewrite("a")

    pyautogui.click(1441, 710)

    sleep(1)


if __name__ == "__main__":

    sleep(3)
    main()
