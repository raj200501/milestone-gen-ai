# src/cli.py
from chatbot import Chatbot


def main():
    bot = Chatbot()
    print("Welcome to the Milestone Chatbot!")
    print("Type 'exit' to quit.")
    
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        response = bot.get_response(query)
        print(f"Chatbot: {response[0][0]}")


if __name__ == "__main__":
    main()
