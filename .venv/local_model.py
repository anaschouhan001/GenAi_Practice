from ollama import chat
response= chat(
    model="gemma3:1b",
    messages= [
        {
            "role": "user",
            "content":"Explain machine learinng in one sentence."
        }
    ]
)
print(response.message.content)