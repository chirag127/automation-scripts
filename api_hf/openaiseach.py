import config
from time import sleep
import openai
import keyboard

from f import get_prompt, type_text


def get_code_from_openai(
    prompt_,
    model="code-davinci-002",
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,

):
    number_of_characters = len(prompt_)

    max_number_of_characters = 20000

    if number_of_characters > max_number_of_characters:
        print("The prompt is too long. Please shorten it.")
        prompt_ = prompt_[-max_number_of_characters:]

    number_of_characters = len(prompt_)

    max_tokens = 7000 - number_of_characters // 4

    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
        model=model,
        prompt=prompt_,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=["\n\n\n", "###","\r\n\r\n\r\n"],
    )

    # pretty_print the response
    import pprint

    pprint.pprint(response)

    text = response.choices[0].text

    print(f"text: {text}")

    with open("openai_response.txt", "a",encoding="utf-8") as file:
        file.write(text)

    return text


def main(model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):

    prompt = get_prompt()

    text = get_code_from_openai(
        prompt,
        model,
        temperature,
        max_tokens,
        top_p,
        frequency_penalty,
        presence_penalty,
    )

    type_text(text)

def speak(text):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

if __name__ == "__main__":

    max_tokens = None
    temperature = 0.5
    top_p = 1
    frequency_penalty = 0.3
    presence_penalty = 0.1
    import sys

    if len(sys.argv) > 1:
        max_tokens = int(sys.argv[1])
    elif len(sys.argv) > 2:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])
    elif len(sys.argv) > 3:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])
        top_p = float(sys.argv[3])
    elif len(sys.argv) > 4:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])
        top_p = float(sys.argv[3])
        frequency_penalty = float(sys.argv[4])
    elif len(sys.argv) > 5:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])
        top_p = float(sys.argv[3])
        frequency_penalty = float(sys.argv[4])
        presence_penalty = float(sys.argv[5])

    i = 0
    while True:
        key = "ctrl+q"
        if keyboard.is_pressed(key):
            print(f"{key} pressed")

            main(
                model="code-davinci-002",
                temperature=0,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )

            speak("Done")

        else:
            sleep(0.1)
