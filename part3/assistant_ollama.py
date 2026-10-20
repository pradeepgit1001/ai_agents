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

#Define the roles for the AI assistant
roles = {
    "1": "You are a friendly school teacher. Explain every concept in simple language with real life examples.",
    "2": "You are a senior Python developer. Explain programming concepts clearly and alwasy include Python examples.",
    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",
    "4": "You are a motivation coach. Encourage the user and give practical advice with a positive attitude.",
    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

#Select the optional role for the AI assistant
print("\nSelect a role for the AI assistant:")
print("1. School Teacher")
print("2. Python Developer")
print("3. Travel Guide")
print("4. Motivation Coach")
print("5. Interviewer")

choice = input("\nEnter your choice: ")

#Add the system prompt to the conversation list to set the context for the AI model
conversation = [
    {
        "role"    : "system",
        "content" : roles.get(choice, "You are a friendly AI teacher. Explain every concept in simple language with real life examples.")
    }
]

# Conversation loop
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

    ai_reply = response.choices[0].message
    content = ai_reply.content or getattr(ai_reply, "reasoning", "") or ""

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