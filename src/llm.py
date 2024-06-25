from openai import OpenAI
client=OpenAI()
def ask_order(message,model="GPT-3.5-Turbo",temprature=0):
    response=client.chat.completions.create(
        model=model,
        temprature=temprature,
        message=messsage
    )