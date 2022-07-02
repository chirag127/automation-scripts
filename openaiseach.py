import config
from time import sleep
import openai
import keyboard

from f import get_prompt, type_text


def get_code_from_openai(
    prompt_,
    model="code-davinci-002",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.3,
    presence_penalty=0.1,
):
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
        model=model,
        prompt=prompt_,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    # pretty_print the response
    import pprint

    pprint.pprint(response)

    text = response.choices[0].text

    print(f"text: {text}")

    with open("openai_response.txt", "a") as f:
        f.write(text)

    return text


def main(model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):

    prompt, number_of_characters = get_prompt()

    if number_of_characters > 20000:
        # prompt is too long, so truncate it to 28000 characters from the right
        prompt = prompt[-20000:]

    number_of_characters = len(prompt)

    if max_tokens is None:
        max_tokens = 7000 - number_of_characters // 4

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


if __name__ == "__main__":

    max_tokens = None
    temperature = 0
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
        if keyboard.is_pressed("ctrl+s"):
            main(
                model="code-davinci-002",
                temperature=0,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )
        else:
            sleep(0.1)
            print(i)
            i = i % 10
            i += 1


# python main.py
