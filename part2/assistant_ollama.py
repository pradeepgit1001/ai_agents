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
    base_url=os.getenv("BASE_URL"),
    api_key=api_key
)

print("="*40)
print("   My AI Assistant")
print("="*40)

#List to store the messages in the conversation
conversation = []

while True:
    user_input = input("\nYou: ")

    #Save the user input in the messages list
    conversation.append(
        {"role"   : "user",
         "content": user_input
        }
    )

    if user_input.lower() in ["exit", "quit"]:
        print("\nAI : Exiting the assistant. Goodbye!")
        break

    # Send user input to the AI model
    response = client.chat.completions.create(
        model      = os.getenv("MODEL"),
        messages   = conversation,
        max_tokens = 120,
        timeout    = 120,
        extra_body = {"think": False},
    )

    ai_replay = response.choices[0].message
    content = ai_replay.content or getattr(ai_replay, "reasoning", "") or ""

    if not content.strip():
        raise RuntimeError(
            "The model returned an empty response. Try a lighter model."
        )

    # Save the AI response in the conversation
    conversation.append(
        {"role"   : "assistant",
         "content": content
        }
    )
    
    print(f"\nAI: {content}")

    print("\n---------------Conversation so far-----------------------")
    for msg in conversation:
        role = msg["role"]
        content = msg["content"]
        print(f"{role.capitalize()}: {content}")    

    print("\n---------------------------------------------------------")