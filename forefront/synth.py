# In order to use the REST API, you must create an account and get your API key. Each request shall have the following header applied:
# Authorization: Bearer YOUR_API_KEY
# 1.2 Engines
# Most endpoints require an engine_id to operate. The following engines are currently available:
# gptj_6B: GPT-J is a language model with 6 billion parameters trained on the Pile (825 GB of text data) published by EleutherAI. Its main language is English but it is also fluent in several other languages. It is also trained on several computer languages.
# boris_6B: Boris is a fine tuned version of GPT-J for the French language. Use this model is you want the best performance with the French language.
# fairseq_gpt_13B: Fairseq GPT 13B is an English language model with 13 billion parameters. Its training corpus is less diverse than GPT-J but it has better performance at least on pure English language tasks.
# gptneox_20B: GPT-NeoX-20B is the largest publically available English language model with 20 billion parameters. It was trained on the same corpus as GPT-J.
# m2m100_1_2B: M2M100 1.2B is a 1.2 billion parameter language model specialized for translation. It supports multilingual translation between 100 languages.
# 1.3 Text completions
# The API syntax for text completions is:
# POST https://api.textsynth.com/v1/engines/{engine_id}/completions
# where engine_id is the selected engine.
# Request body (JSON)
# prompt: string.
# The input text to complete.

# max_tokens: optional int (default = 100)
# Maximum number of tokens to generate. A token represents about 4 characters for English texts. The total number of tokens (prompt + generated text) cannot exceed the model's maximum context length. It is of 2048 for GPT-J and 1024 for the other models.

# If the prompt length is larger than the model's maximum context length, the beginning of the prompt is discarded.

# stream: optional boolean (default = false)
# If true, the output is streamed so that it is possible to display the result before the complete output is generated. Several JSON answers are output. Each answer is followed by two line feed characters.

# stop: optional string or array of string (default = null)
# Stop the generation when the string(s) are encountered. The generated text does not contain the string. The length of the array is at most 5.

# n: optional integer (range: 1 to 16, default = 1)
# Generate n completions from a single prompt.

# temperature: optional number (default = 1)
# Sampling temperature. A higher temperature means the model will select less common tokens leading to a larger diversity but potentially less relevant output. It is usually better to tune top_p or top_k.

# top_k: optional integer (range: 1 to 1000, default = 40)
# Select the next output token among the top_k most likely ones. A higher top_k gives more diversity but a potentially less relevant output.

# top_p: optional number (range: 0 to 1, default = 0.9)
# Select the next output token among the most probable ones so that their cumulative probability is larger than top_p. A higher top_p gives more diversity but a potentially less relevant output. top_p and top_k are combined, meaning that at most top_k tokens are selected. A value of 1 disables this sampling.

# More advanced sampling parameters are available:
# logit_bias: optional object (default = {})
# Modify the likelihood of the specified tokens in the completion. The specified object is a map between the token indexes and the corresponding logit bias. A negative bias reduces the likelihood of the corresponding token. The bias must be between -100 and 100. Note that the token indexes are specific to the selected model. You can use the tokenize API endpoint to retrieve the token indexes of a given model.
# Example: if you want to ban the " unicorn" token for GPT-J, you can use: logit_bias: { "44986": -100 }

# presence_penalty: optional number (range: -2 to 2, default = 0)
# A positive value penalizes tokens which already appeared in the generated text. Hence it forces the model to have a more diverse output.

# frequency_penalty: optional number (range: -2 to 2, default = 0)
# A positive value penalizes tokens which already appeared in the generated text proportionaly to their frequency. Hence it forces the model to have a more diverse output.

# repetition_penalty: optional number (default = 1)
# Divide by repetition_penalty the logits corresponding to tokens which already appeared in the generated text. A value of 1 effectively disables it. See this article for more details.

# typical_p: optional number (range: 0 to 1, default = 1)
# Alternative to top_p sampling: instead of selecting the tokens starting from the most probable one, start from the ones whose log likelihood is the closest to the symbol entropy. As with top_p, at most top_k tokens are selected. A value of 1 disables this sampling. See this article for more details.

# Answer (JSON)
# text: string or array of string
# It is the completed text. If the n parameter is larger than 1, an array of strings is returned.

# reached_end: boolean
# If true, indicate that it is the last answer. It is only useful in case of streaming output (stream = true in the request).

# truncated_prompt: bool (default = false)
# If true, indicate that the prompt was truncated because it was too large compared to the model's maximum context length. Only the end of the prompt is used to generate the completion.

# input_tokens: integer
# Indicate the number of input tokens. It is useful to estimate the number of compute resources used by the request.

# output_tokens: integer
# Indicate the total number of generated tokens. It is useful to estimate the number of compute resources used by the request.
# convert the above to a python script

import requests

api_key = "fb23ba898dd0b8e6ed1f76051099eac0"


def main(
    engine_id="fairseq_gpt_13B",
    prompt="# print hello world using python",
    max_tokens=100,
    stream=False,
    stop=None,
    number=1,
    temperature=1,
    top_k=40,
    top_p=1.0,
    frequency_penalty=0.1,
    presence_penalty=0.2,
    repetition_penalty=0.2,
    logit_bias=None,
):
    if logit_bias is None:
        logit_bias = {}
    if stop is None:
        stop = []
    url = f"https://api.textsynth.com/v1/engines/{engine_id}/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "stream": stream,
        "stop": stop,
        "n": number,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "logit_bias": logit_bias,
        "repetition_penalty": repetition_penalty
    }
    response = requests.post(url, headers=headers, json=data, timeout=60)
    return response.text


if __name__ == "__main__":
    print(main())
