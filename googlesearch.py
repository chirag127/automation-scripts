from time import sleep
import keyboard
from f import search_google, get_prompt, type_text


def main():

    prompt = get_prompt()

    text = search_google(prompt)

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
