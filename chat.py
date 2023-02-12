import os
import openai

CONTEXT_LENGTH = 2048

openai.api_key = os.getenv('OPENAI_API_KEY')
prompt_text = []
while True:
    question = input('Ask your question:\n')
    if question == 'quit()':
        break
    prompt_text.append(question)
    response = openai.Completion.create(model='text-davinci-003',
                                        prompt=prompt_text,
                                        max_tokens=CONTEXT_LENGTH - len(''.join(prompt_text)),
                                        temperature=0,
                                        stream=True)
    for r in response:
        if r['choices'][0]['index'] == len(prompt_text)-1: 
            print(r['choices'][0]['text'], end='')
    print()
