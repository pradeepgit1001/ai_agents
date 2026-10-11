from openai import OpenAI

# Give an API key to the client
client = OpenAI(
  api_key=" "
)

response = client.responses.create(
  model="gpt-6-luna",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);