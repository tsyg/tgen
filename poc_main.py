import json
import openai
import os
import time

from openai import APIError

openai.api_key = os.environ["OPENAI_API_KEY"]
yml_file_pathname = "C:\\Users\\tsyg\\work\\try\\openAPI\\tiny_api01.yml"  # "C:\\Users\\tsyg\\work\\try\\openAPI\\sample01.yml"
open_api_definition = ""  # To be loaded from the file


def request_decorator(
        sent_request: callable, time_sleep: int = 10, retries: int = 1, **kwargs
):
    def decorator(sent_request: callable):
        def wrapper(**kwargs):
            count_retries = 0
            while count_retries < retries:
                try:
                    response = sent_request(**kwargs)
                    return response
                except (openai.error.APIError, openai.error.RateLimitError, openai.error.Timeout) as e:
                    print(f"{type(e)}")
                    time.sleep(time_sleep)
                    print(f"Bad context response {e}")  # logging.warning(f"Bad context response {e}")
                    count_retries += 1
            raise RuntimeError(f"Maximum number {retries} has been reached")

        return wrapper

    return decorator


def sent_chat_request():
    model = "gpt-3.5-turbo"  # "gpt-4"  # https://platform.openai.com/docs/models/gpt-4
    max_tokens = 3300
    global open_api_definition
    messages = [{"role": "user",
                 # "can I get automated API tests in python that cover my openAPI definition"
                 "content":
                     f"Please generate various  positive and negative automated tests in python " +
                     f"based on the following OpenApi definition: \n{open_api_definition}" +
                     f" The python tests should be data-driven"
                 }
                ]
    completion = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=max_tokens)
    print(f"model = {model}, max_tokens={max_tokens} messages = {json.dumps(messages)}" +
          "\n=== Below is response from ChatGPT: =====")
    print(completion.choices[0].message.content)
    return completion


@request_decorator(sent_request=sent_chat_request)
def sent_chat_request_with_decorator():
    return sent_chat_request()


if __name__ == "__main__":
    with open(yml_file_pathname, 'r') as f:
        open_api_definition = f.readlines()
        sent_chat_request_with_decorator()
