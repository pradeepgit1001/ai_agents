from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from .env file
load_dotenv()  

# Create AI client
client = OpenAI(
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
    response = client.responses.create(
        model=os.getenv("MODEL"),
        input=user_input,
        store=True,
    )

    message = response.output_text
    print(f"\nAI: {message}\n")