from f import get_prompt, type_text


def get_code_from_metaai(prompt, max_tokens=None, temperature=0):

    if max_tokens is None:
        max_tokens = 320

    send_data = {
        "length": max_tokens,
        "temperature": temperature,
        "extra_sentinel": False,
        "prompt": prompt,
    }

    # convert above js code to python code:
    import base64
    import json

    stringified = json.dumps(send_data)
    encoded_data = base64.b64encode(stringified.encode("utf-8"))

    print(f"encoded_data: {encoded_data}")

    # remove the b' from the beginning of the string:
    encoded_data = encoded_data.decode("utf-8")

    print(f"encoded_data: {encoded_data}")

    # remove all = from the string:
    encoded_data = encoded_data.replace("=", "")

    print(f"encoded_data: {encoded_data}")
    import requests

    url = f"https://hf.space/embed/facebook/incoder-demo/generate?info={encoded_data}"

    print(f"url: {url}")

    response = requests.get(url)

    print(f"response: {response}")

    lenght_of_prompt = len(prompt)
    response = json.loads(response.text)
    text = response["text"]

    text_without_prompt = text[lenght_of_prompt:]

    return text_without_prompt


def main(max_tokens=None, temperature=0):

    
    prompt, number_of_characters = get_prompt()

    if number_of_characters > 400:
    # prompt is too long, so truncate it to 400 characters from the right
        print("prompt is too long, so truncate it to 400 characters from the right")
        prompt = prompt[-400:]

        number_of_characters = 400

        print(f"number_of_characters: {number_of_characters}")

    if max_tokens is None:
        max_tokens = 320 - number_of_characters // 4

        print(f"max_tokens: {max_tokens}")

    text = get_code_from_metaai(
        prompt,
        max_tokens,
        temperature,
    )

    type_text(text)





if __name__ == "__main__":

    max_tokens = None
    temperature = 0.6
    import sys

    if len(sys.argv) > 1:
        max_tokens = int(sys.argv[1])
    elif len(sys.argv) > 2:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])

    elif len(sys.argv) > 3:
        max_tokens = int(sys.argv[1])
        temperature = float(sys.argv[2])
        print("too many arguments")
        exit()

    import keyboard
    from time import sleep

    i = 0
    while True:
        if keyboard.is_pressed("ctrl+s"):
            main(max_tokens,temperature)
        else:
            sleep(0.1)
            print(i)
            i = i % 10
            i += 1
            
