import webbrowser
import pyperclip
import pyautogui
from time import sleep
import requests


def search_google(text):
    webbrowser.open(f"https://www.google.com/search?q={text}")


def bloom(text):

    try:

        # if the prompt is too long, truncate it to 240 haracters from the right
        if len(text) > 240:
            text = text[-240:]

        api = "https://api-inference.huggingface.co/models/bigscience/bloom"

        payload = {
            "inputs": text,
            "parameters": {
                "seed": 54,
                "early_stopping": False,
                "length_penalty": 0,
                "max_new_tokens": 64,
                "do_sample": True,
                "top_p": 0,
            },
        }
        response = requests.post(api, json=payload)

        # response.text is [{"generated_text":"Correct this to standard English:\r\n\r\nShe no went to the market.\r\nShe did not go to the market.\r\n\r\nShe no eat cake.\r\nShe did not eat cake."}]
        generated_text = response.json()[0]["generated_text"]
        final_text = generated_text.replace(text, "")

        return final_text

    except Exception as e: # pylint: disable=broad-except
        print(e)
        return bloom(text)



def get_prompt():

    """
    Get the prompt from the user.
    """

    sleep(0.5)
    pyautogui.hotkey("ctrl", "c")

    pyautogui.press("right")

    prompt = pyperclip.paste()
    return prompt


def type_text(text):
    if text:
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")


if __name__ == "__main__":
    print(bloom("hello"))
