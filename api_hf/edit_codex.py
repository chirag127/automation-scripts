"""
This module contains the main function.
"""
from time import sleep
import config
import keyboard
import openai
import pyautogui
import pyperclip
from f import type_text


def get_edited_code_from_openai(
    prompt_: str,
    model: str,
    instruction: str,
):
    """
    Get edited code from OpenAI.

    Args:
        prompt_: The prompt to edit.
        model: The model to use.
        instruction: The instruction to use.

    Returns:
        The edited code.
    """
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
    with open("openai_response.txt", "a", encoding="utf-8") as file:
        file.write(text)
    return text


def main(model: str = "code-davinci-edit-001", instruction: str = "solve the problem"):
    """
    Get the prompt from the user and edit it.

    Args:
        model: The model to use.
        instruction: The instruction to use.

    Returns:
        None
    """
    sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    prompt = pyperclip.paste()
    text = get_edited_code_from_openai(
        prompt_=prompt, model=model, instruction=instruction
    )
    type_text(text)


def speak(text: str) -> None:
    """
    This function takes a string as an argument and speaks it.

    Args:
        text: The text to be spoken.

    Returns:
        None
    """
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
