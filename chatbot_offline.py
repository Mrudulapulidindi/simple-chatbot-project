# chatbot_offline.py

def chatbot_response(user_input):
    """
    Returns a response based on predefined inputs.
    """
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "nice to meet you":"I'm glad to meet you too.",
        "what's you're name":"my name is chattybotty",
        "what are you doing":" nothing just chilling with you, what about you",
        "how are you": "I'm doing great, thank you!",
        "what is ai": "AI stands for Artificial Intelligence.",
        "bye": "Goodbye!"
    }
    
    return responses.get(user_input.lower(), "I don't understand that.")

def main():
    print("Welcome to the Offline Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: See you next time!")
            break
        reply = chatbot_response(user_input)
        print("Chatbot:", reply)

if __name__ == "__main__":
    main()
