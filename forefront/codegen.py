# curl 'https://playground-api.forefront.link/api/models/gpt-j' \
#   -H 'authority: playground-api.forefront.link' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: en-US,en;q=0.9' \
#   -H 'authorization: Bearer' \
#   -H 'content-type: application/json' \
#   -H 'origin: https://playground.helloforefront.com' \
#   -H 'referer: https://playground.helloforefront.com/' \
#   -H 'sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: cross-site' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35' \
#   --data-raw $'{"text":"# print hello\\n\\n\\n\\ndef main():\\n    print(\\"Hello, world\u0021\\")\\n    import time\\n    time.sleep(10)\\n    print(\\"End\u0021\\")\\n    \\n\\ndef main():\\n    print(\\"Hello, world\u0021\\")\\n    import time\\n    time.sleep(10)\\n    print(\\"End\u0021\\")\\n\\n\\t\\ndef main():\\n    print(\\"Hello, world\u0021\\")\\n    import time\\n    time.sleep(10)\\n    print(\\"End\u0021\\"","length":64,"temperature":0.8,"top_p":1,"top_k":40,"repetition_penalty":1,"stop":[],"bad_words":[],"logit_bias":{}}' \
#   --compressed

# covert the above to a python script
def main():
    import requests
    import json
    url = "https://playground-api.forefront.link/api/models/gpt-j"
    payload = {"text":"# print hello\n\n\ndef main():\n    print(\"Hello, world!\")\n    import time\n    time.sleep(10)\n    print(\"End!\")\n    \ndef main():\n    print(\"Hello, world!\")\n    import time\n    time.sleep(10)\n    print(\"End!\")\n\t\ndef main():\n    print(\"Hello, world!\")\n    import time\n    time.sleep(10)\n    print(\"End!\")","length":64,"temperature":0.8,"top_p":1,"top_k":40,"repetition_penalty":1,"stop":[],"bad_words":[],"logit_bias":{}}
    headers = {
        'authority': 'playground-api.forefront.link',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://playground.helloforefront.com',
        'referer': 'https://playground.helloforefront.com/',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
    }
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.text.encode('utf8'))

if __name__ == "__main__":
    for i in range(10):
        main()