from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from .env file
load_dotenv()  

# Check that the API key is configured before creating the client
api_key = os.getenv("API_KEY")
if not api_key:
    raise SystemExit(
        "Error: API key not found. Set API_KEY in your .env file or environment."
    )

# Create AI client
client = OpenAI(
    api_key=os.getenv("API_KEY")
)

print("="*40)
print("   My AI Assistant")
print("="*40)

#List to store the messages in the conversation
conversation = []

while True:
    user_input = input("You: ")

    #Save the user input in the messages list
    conversation.append({"role": "user", "content": user_input})

    if user_input.lower() in ["exit", "quit"]:
        print("\nAI : Exiting the assistant. Goodbye!")
        break

    # Send user input to the AI model
    response = client.responses.create(
        model=os.getenv("MODEL"),
        input=conversation,
        store=True,
    )

    ai_reply = response.output_text

    # Save the AI reply in the conversation
    conversation.append({"role": "assistant", "content": ai_reply})

    print(f"\nAI: {ai_reply}\n")