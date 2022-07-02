import numbers
import webbrowser
import pyperclip
import pyautogui
from time import sleep


def search_google(text):
    webbrowser.open(f"https://www.google.com/search?q={text}")


def get_prompt():

    sleep(0.5)
    pyautogui.hotkey("ctrl", "c")

    pyautogui.press("right")

    prompt = pyperclip.paste()

    """ find the length of the prompt"""

    number_of_characters = len(prompt)

    print(f"number of characters: {number_of_characters}")
    print(f"number of tokens: {number_of_characters//4}")

    return prompt, number_of_characters


def type_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


if __name__ == "__main__":
    pass
