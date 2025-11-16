import ollama

res = ollama.chat(
    model='llava:7b',
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image',
            'images': ['./images/img1.jpg']
        }
    ]
)

print(res['message']['content'])
