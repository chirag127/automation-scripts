import config
from time import sleep
import openai
import keyboard

from f import type_text


def get_edited_code_from_openai(
        prompt_,
        model,
        instruction,
):

    number_of_characters = len(prompt_)

    max_number_of_characters = 20000

    if number_of_characters > max_number_of_characters:
        print("The prompt is too long. Please shorten it.")
        prompt_ = prompt_[-max_number_of_characters:]

    number_of_characters = len(prompt_)

    max_tokens = 7000 - number_of_characters // 4

    openai.api_key = config.OPENAI_API_KEY

    response = openai.Edit.create(
        input=prompt_,
        instruction=instruction,
        model=model,
    )


    print(response)

    # pretty_print the response
    import pprint

    pprint.pprint(response)

    text = response.choices[0].text

    print(f"text: {text}")

    with open("openai_response.txt", "a",encoding="utf-8") as file:
        file.write(text)

    return text

import pyautogui
import pyperclip

def main(model="code-davinci-edit-001", instruction="solve the problem"):

    """
    Get the prompt from the user.
    """

    sleep(0.5)
    pyautogui.hotkey("ctrl", "c")

    prompt = pyperclip.paste()

    text = get_edited_code_from_openai(
        prompt_=prompt,
        model=model,
        instruction=instruction)

    type_text(text)

def speak(text):
    import win32com.client as wincl
    spea = wincl.Dispatch("SAPI.SpVoice")
    spea.Speak(text)

if __name__ == "__main__":

    i = 0
    while True:
        key = "ctrl+a"
        if keyboard.is_pressed(key):
            print(f"{key} pressed")

            speak("starting")

            # instruction = "remove all pylint errors"

            # main(instruction=instruction)

            main()

            speak("Done")

        else:
            sleep(0.1)
