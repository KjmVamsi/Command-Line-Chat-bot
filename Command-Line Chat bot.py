import time

def chatbot():
    print("Hello! I'm your friendly command-line chatbot.")
    print("You can ask me questions or give me tasks like setting reminders.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'your name' in user_input:
            print("Chatbot: I'm a chatbot created by you!")
        elif 'time' in user_input:
            print(f"Chatbot: The current time is {time.strftime('%H:%M:%S')}.")
        elif 'reminder' in user_input:
            print("Chatbot: What would you like me to remind you about?")
            reminder = input("You: ")
            print(f"Chatbot: Reminder set for: {reminder}")
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

if __name__ == "__main__":
    chatbot()
    

