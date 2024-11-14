import openai

# Set your API key directly
openai.api_key = "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"

# Generate a response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
)

print(response['choices'][0]['message']['content'])
