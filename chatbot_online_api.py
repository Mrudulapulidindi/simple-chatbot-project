# chatbot_online_api.py

import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_API_KEY"

def ask_chatbot(question):
    """
    Sends a question to the OpenAI ChatGPT model and returns the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content.strip()

def main():
    print("Welcome to the Online ChatGPT Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        reply = ask_chatbot(user_input)
        print("Chatbot:", reply)

if __name__ == "__main__":
    main()
