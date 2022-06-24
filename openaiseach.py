import config
from time import sleep
import openai
import keyboard

from f import get_prompt, type_text


def get_code_from_openai(prompt_, model="code-davinci-002"):
    prompt_ = f"write python code to {prompt_}"
    prompt_ = f"{prompt_}"
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
        model=model,
        prompt=prompt_,
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    text = response.choices[0].text

    print(f"text: {text}")

    return text


def main():

    prompt = get_prompt()

    text = get_code_from_openai(prompt)

    type_text(text)


if __name__ == "__main__":
    i = 0
    while True:
        if keyboard.is_pressed("ctrl+c"):
            main()
        else:
            sleep(0.1)
            print(i)
            i = i % 10
            i += 1

# Compare this snippet from googlesearch.py:

# make a function to search google for a given string and return the first result
