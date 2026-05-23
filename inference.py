import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("MODEL_NAME")

client = Groq(api_key=api_key)

def generate_answer(prompt):

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content