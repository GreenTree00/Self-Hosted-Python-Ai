from ollama import chat
from ollama import ChatResponse

def question(data):
    # place your selected locally running model below
    response: ChatResponse = chat(model='AI_MODEL_NAME', messages=[
        {
            'role': 'user',
            'content': f'{data}',
        },
    ])
    print(response.message.content)

active = True

print("Type 'end' to exit chat")
while active:
    data = input("Message to AI: ")
    if data == "end":
        active = False
    else:
        question(data)
