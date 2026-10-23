
from google import genai
from google.genai import errors

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain Python in simple words."
    )
    print(response.text)

except errors.APIError as e:
    print("Gemini API error:", e.code)
    print(e.message)

