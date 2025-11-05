from openai import OpenAI

# Initialize the new client
client = OpenAI(api_key="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")

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or any available model like "gpt-4-turbo" or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": "Hello, world!"}
        ]
    )

    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")
