import config
from time import sleep
import openai
import keyboard
import requests

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


    # url = "https://api.openai.com/v1/edits"
    # response = requests.post(
    #     url,
    #     headers={
    #         "Authorization": f"Bearer {config.OPENAI_API_KEY}",
    #         "Content-Type": "application/json",
    #     },
    #     json={
    #         "input": prompt_,
    #         "instruction": instruction,
    #         "model": model,
    #         "temperature": 0.5,
    #         "max_tokens": max_tokens,
    #         "top_p": 1,
    #         "frequency_penalty": 0,
    #         "presence_penalty": 0,
    #         "stop": ["\n\n\n", "###","\r\n\r\n\r\n"],
    #     },
    # )

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

def main(model="code-davinci-edit-001", instruction="follow instructions in the input"):

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

            main()

            speak("Done")

        else:
            sleep(0.1)

    # max_tokens = None
    # import sys

    # if len(sys.argv) > 1:
    #     max_tokens = int(sys.argv[1])
    # elif len(sys.argv) > 2:
    #     max_tokens = int(sys.argv[1])
    #     temperature = float(sys.argv[2])
    # elif len(sys.argv) > 3:
    #     max_tokens = int(sys.argv[1])
    #     temperature = float(sys.argv[2])
    #     top_p = float(sys.argv[3])
    # elif len(sys.argv) > 4:
    #     max_tokens = int(sys.argv[1])
    #     temperature = float(sys.argv[2])
    #     top_p = float(sys.argv[3])
    #     frequency_penalty = float(sys.argv[4])
    # elif len(sys.argv) > 5:
    #     max_tokens = int(sys.argv[1])
    #     temperature = float(sys.argv[2])
    #     top_p = float(sys.argv[3])
    #     frequency_penalty = float(sys.argv[4])
    #     presence_penalty = float(sys.argv[5])
