import sys
from time import sleep

import keyboard
from bd import bd

from f import bloom, get_prompt, search_google, type_text
from openaiseach import get_code_from_openai


def main(api):
    prompt = get_prompt()

    if api == "google":
        search_google(prompt)
        text = False
    elif api == "openai":

        text = get_code_from_openai(
            prompt,
            model="code-davinci-002",
            temperature=0,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0.1,
        )

    elif api == "bloom":
        text = bloom(prompt)
    elif api == "bd":
        text = bd(prompt)
    elif api == "all":
        try:
            print("openai")
            print(get_code_from_openai(prompt))
        except:
            pass
        try:
            print("bloom")
            print(bloom(prompt))
        except:
            pass
        try:
            print("bloom_hf_demo")
            print(bd(prompt))
        except:
            pass

        return

    type_text(text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        api_ = sys.argv[1]
    else:
        api_ = "google"
    while True:
        if keyboard.is_pressed("ctrl+a"):
            main(api_)
        else:
            sleep(0.1)
