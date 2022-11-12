import requests
import json

# covert the above to a python script
def main(
    model="codegen",
    text="#python 3.10 \n\n# print Hello, world!\ndef",
    length=64,
    temperature=0,
    top_p=1,
    top_k=10,
    repetition_penalty=0,
    stop=None,
    bad_words=None,
    logit_bias=None,
):
    if stop is None:
        stop = []
    if bad_words is None:
        bad_words = []
    if logit_bias is None:
        logit_bias = {}
    url = f"https://playground-api.forefront.link/api/models/{model}"
    payload = json.dumps(
        {
            "text": text,
            "length": length,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "repetition_penalty": repetition_penalty,
            "stop": stop,
            "bad_words": bad_words,
            "logit_bias": logit_bias,
        }
    )
    headers = {
        "authority": "playground-api.forefront.link",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer",
        "content-type": "application/json",
        "origin": "https://playground.helloforefront.com",
        "referer": "https://playground.helloforefront.com/",
        "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=20)

    completion = response.json()["result"][0]["completion"]
    print(completion)
    return completion


if __name__ == "__main__":
    for _ in range(1):

        # avaliable models are codegen, gpt-j, gpt-neox
        main(
            "gpt-j",
            "#python 3.10 \n\n# print Hello, world!\ndef",
            length=64,
            temperature=0.8,
            top_p=1,
            top_k=40,
            repetition_penalty=1,
            stop=[],
            bad_words=[],
            logit_bias={},
        )
