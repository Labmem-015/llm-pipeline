from openai import OpenAI
from nortllm.env import *

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

messages_to_send = [
    {"role": "system", "content": "AI agent pipeline debug mode."},
    {"role": "user", "content": "Give me your status"}
]

response = client.chat.completions.create(
    model="default",
    messages=messages_to_send # type:ignore 
)

print(response.choices[0].message.content)
print(client.chat.completions.list())