from openai import OpenAI
from src.prompt import system_instruction
client=OpenAI()
messages=[{"role":"system","content":"system_instruction"}]
def ask_order(messages,model="GPT-3.5-Turbo",temprature=0):
    response=client.chat.completions.create(
        model=model,
        temprature=temprature,
        message=messsages
    )
    return response.chioce[0].message.content
