import numbers
import webbrowser
import pyperclip
import pyautogui
from time import sleep


def search_google(text):
    webbrowser.open(f"https://www.google.com/search?q={text}")


def get_prompt():

    sleep(0.5)

    pyautogui.press("right")

    prompt = pyperclip.paste()

    """ find the length of the prompt"""

    number_of_characters = len(prompt)

    if number_of_characters > 20000:
        # prompt is too long, so truncate it to 28000 characters from the right
        prompt = prompt[-20000:]

    return prompt


def type_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


if __name__ == "__main__":
    pass