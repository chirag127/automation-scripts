import config
import openai


def get_text_from_openai(
    prompt_: str,
    model: str = "code-davinci-002",
    temperature: float = 0.5,
    max_tokens: int = 100,
    top_p: float = 1,
    frequency_penalty: float = 0,
    presence_penalty: float = 0,
):
    """
    Get text from OpenAI.

    Args:
        prompt_: The prompt to be completed.
        model: The model to be used.
        temperature: The temperature to be used.
        max_tokens: The maximum number of tokens to be used.
        top_p: The top_p to be used.
        frequency_penalty: The frequency_penalty to be used.
        presence_penalty: The presence_penalty to be used.

    Returns:
        The text.
    """
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
        stop=["\n\n\n", "###", "\r\n\r\n\r\n"],
    )
    # pretty_print the response
    import pprint

    pprint.pprint(response)
    text = response.choices[0].text
    print(f"text: {text}")
    with open("openai_response.txt", "a", encoding="utf-8") as file:
        file.write(text)
    return text


prompt = "hello world"
for i in range(5):
    a = get_text_from_openai(prompt)
    print(a)
    prompt = prompt + a
