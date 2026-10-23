
from google import genai
import os

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain machine learning in detail.",
    generation_config= {
        "temperature":1.0,
        "max_output_tokens":300
    }
)

print(interaction.output_text)