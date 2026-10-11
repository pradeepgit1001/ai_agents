from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from .env file
load_dotenv()  

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print("   My AI Assistant")
print("="*40)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\nAI : Exiting the assistant. Goodbye!")
        break

    # Send user input to the AI model
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user", 
                "content": user_input
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
    
    print(f"\nAI: {content}\n")