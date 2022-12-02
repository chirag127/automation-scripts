"""
This module contains the code for the Pocket API.
"""

import requests
from concurrent import futures


def post_urls(urls):

    with futures.ThreadPoolExecutor(max_workers=1000) as executor:

        the_futures = []
        for url in urls:
            the_futures.append(executor.submit(add_url, url))

        for _ in futures.as_completed(the_futures):
            pass



def get_request_token():

    json = {
        "consumer_key": "REDACTED_POCKET_CONSUMER_KEY",
        "redirect_uri": "pocketapp1234:authorizationFinished",
    }
    headers = {
        "Host": "getpocket.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Accept": "application/json",
    }

    r = requests.post(
        "https://getpocket.com/v3/oauth/request", headers=headers, data=json
    )
    print(r.text)
    print(r.status_code)


def convert_request_token():
    json = {
        "consumer_key": "REDACTED_POCKET_CONSUMER_KEY",
        "code": "REDACTED_POCKET_REQUEST_TOKEN",
    }
    r = requests.post("https://getpocket.com/v3/oauth/authorize", json=json,timeout=10)

    
    print(r.text)
    print(r.json)
    print(r.status_code)
    print(r.headers)


access_token = "REDACTED_POCKET_ACCESS_TOKEN"
username = "REDACTED_EMAIL"


def add_url(url):

    request_url = "https://getpocket.com/v3/add"

    request_data = {
        "url": url,
        "consumer_key": "REDACTED_POCKET_CONSUMER_KEY",
        "access_token": access_token,
    }

    response = requests.post(request_url, data=request_data,timeout=10)

    response_json = response.json()

    if response_json["status"] == 1:
        print("Successfully added item to Pocket")
        return True
    else:
        print("Error adding item to Pocket")
        print(response_json["error"])
        return False


if __name__ == "__main__":

    with open("links.txt", "r", encoding="utf-8") as f:

        urls = f.readlines()
    post_urls(urls)
