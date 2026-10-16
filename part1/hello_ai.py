from pathlib import Path
import os

from openai import OpenAI
from dotenv import load_dotenv

# Load configuration from the local .env file next to this script
load_dotenv(Path(__file__).resolve().with_name(".env"))

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

if not all([base_url, api_key, model]):
    raise RuntimeError(
        "Missing environment variables. Check BASE_URL, API_KEY, and MODEL in d_env/.env"
    )

# Create a client that communicates with the Ollama API
client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

# Send a question to the Ollama API and get a response
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is newton's first law?",
        }
    ],
    max_tokens=120,
    timeout=120,
    extra_body={"think": False},
)

message = response.choices[0].message
content = message.content or getattr(message, "reasoning", "") or ""

if not content.strip():
    raise RuntimeError(
        "The model returned an empty response. Try a lighter model."
    )

# Display the response from the Ollama API
print(content)