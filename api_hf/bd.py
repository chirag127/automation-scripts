import time
import requests


def bd(promt):

    """
    This function is used to get the bloom prediction from the bloom hugging face api.
    :param promt: The prompt to be used for the prediction.
    :return: The prediction.
    """

    push_url = "https://hf.space/embed/huggingface/bloom_demo/api/queue/push/"

    # payload example: {"fn_index":2,"data":[" india",32,"Sample","Sample 1"],"action":"predict","session_hash":"ar9htvvc59"}
    payload = {
        "fn_index": 2,
        "data": [promt, 64, "Sample", "Sample 1"],
        "action": "predict",
        "session_hash": "ar9htvvc59",
    }

    response = requests.post(push_url, json=payload)
    print(response.text)

    # response = response.text

    # response example: {"hash":"662b265fb17649e691618cf9d452a769","queue_position":0}
    response = response.json()
    hash_from_response = response["hash"]

    # wait for the prediction to be done
    status_url = "https://hf.space/embed/huggingface/bloom_demo/api/queue/status/"

    # payload example: {hash: "662b265fb17649e691618cf9d452a769"}
    payload = {"hash": hash_from_response}

    # prediction pending response example: {"status":"PENDING","data":null}

    # prediction completed response example: {"status":"COMPLETE","data":{"data":["\n  <div id = \"img_placeholder\">\n  </div>\n  <div class=\"relative\" id=\"capture\" align=\"justify\" style=\"display:none;\">\n    <div class=\"absolute font-semibold\" style=\"left:7%; right:7%; bottom:32%; top:7%; font-size: 8rem; line-height: 1; padding: 1rem; font-family:-apple-system, BlinkMacSystemFont, 'Arial', sans-serif;\" id=\"text_box\">\n      <p class=\"text\" style=\"color:white; white-space:pre-wrap;\" dir=\"auto\" id = \"prompt\"> india</p>\n        <p class=\"text\" style=\"color:#FE57A0; white-space:pre-wrap;\" dir=\"auto\" id=\"generation\"> heat transfer coefficient htr [W/m².K]\nFollowing a comprehensive analysis of the data available and in order to evaluate and compare the general properties of</p>\n    </div>\n    <img src=\"https://huggingface.co/spaces/huggingface/bloom_demo/raw/main/bg.jpg\" class=\"w-full\" />\n  </div>\n"," india heat transfer coefficient htr [W/m².K]\nFollowing a comprehensive analysis of the data available and in order to evaluate and compare the general properties of",""],"duration":16.61606740951538,"average_duration":19.821221613234584}}
    while True:

        response = requests.post(status_url, json=payload)

        response = response.json()

        status = response["status"]

        if status == "COMPLETE":

            data = response["data"]

            data = data["data"][1]

            data = data.replace(promt, "")

            return data

        else:
            print(f"status: {status}")
            time.sleep(1)
            continue


if __name__ == "__main__":

    print(bd("how to make a cake"))
