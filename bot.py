import os
from google import genai
from google.genai import types

def load_api_key():
    try:
        # Check both possible files
        filename = "apikey.txt"
        if not os.path.exists(filename):
            filename = "api.txt"
        
        if not os.path.exists(filename):
             print("Error: neither apikey.txt nor api.txt found.")
             return None

        with open(filename, "r") as f:
            # Aggressive cleaning
            key = f.read().strip()
            key = "".join(key.split())
            return key
    except Exception as e:
        print(f"Error reading API key: {e}")
        return None

def main():
    api_key = load_api_key()
    if not api_key:
        return

    try:
        client = genai.Client(api_key=api_key)
        
        # Create a chat session
        chat = client.chats.create(model="gemini-1.5-flash")
        
        print("Bot: Hello! I'm ready to chat. Type 'quit' or 'exit' to end the session.")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Bot: Goodbye!")
                break
            
            if not user_input.strip():
                continue

            try:
                response = chat.send_message(user_input)
                print(f"Bot: {response.text}")
            except Exception as e:
                print(f"Bot: An error occurred: {e}")

    except Exception as e:
         print(f"Error initializing model: {e}")

if __name__ == "__main__":
    main()
