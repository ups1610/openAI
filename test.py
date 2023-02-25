import os
import openai

OPENAI_API_KEY="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"
openai.api_key = OPENAI_API_KEY
while(True):
    try:
        prompt = input("Hi, How can I help you\n")
        if(prompt == 'exit'):
            break
        response = openai.Completion.create(model = "text-davinci-003" , prompt = prompt,max_tokens = 4000)
        response = response.choices
        print(response[0]["text"]+"\n")
    except Exception as e:
        print(e)    