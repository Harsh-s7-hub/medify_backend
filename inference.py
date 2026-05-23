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
                "role": "system",
                "content": (
                    "You are a helpful medical AI assistant. "
                    "Provide safe, medically relevant, concise answers. "
                    "Do not give dangerous medical advice."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=512
    )

    return completion.choices[0].message.content