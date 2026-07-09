from openai import OpenAI
from nortllm.env import *

client = OpenAI(
    base_url=BASE_URL
)

messages_to_send = [
    {"role": "system", "content": "AI agent pipeline debug mode."},
    {"role": "user", "content": "Give me your status"}
]

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain quantum computing in one sentence."}
]

response = client.chat.completions.create(
    model="default",
    messages=conversation_history
)

print(response)