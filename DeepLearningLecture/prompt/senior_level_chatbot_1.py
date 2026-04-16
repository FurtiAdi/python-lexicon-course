# A simple terminal chatbot for students (clean + beginner-friendly)
def get_user_name():
    # Ask the user for their name
    name = input("Hi! What's your name? ").strip()
    return name if name else "Student"  # Default if empty input


def greet_user(name):
    # Greet the user using their name
    print(f"\nHello, {name}! 👋")
    print("I'm your Python chatbot. Type 'exit' to quit.\n")


def get_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()

    # Simple rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"
    elif "python" in user_input:
        return "Python is great for beginners and very powerful."
    elif "help" in user_input:
        return "You can ask me simple questions about Python."
    elif user_input == "exit":
        return None  # Signal to exit the chat
    else:
        return "I'm still learning. Try asking something else!"


def run_chatbot():
    # Main function that runs the chatbot loop
    name = get_user_name()     # Step 1: get user's name
    greet_user(name)           # Step 2: greet the user

    while True:                # Step 3: keep chatting until user exits
        user_input = input(f"{name}: ")  # Get user input
        response = get_response(user_input)  # Generate response
        if response is None:   # Exit condition
            print("Chatbot: Goodbye! 👋")
            break
        print(f"Chatbot: {response}")  # Show chatbot reply


# Entry point of the program
if __name__ == "__main__":
    run_chatbot()

"""
This code is cleaner and more structured than the second one. It uses clear functions and adds comments, which makes it much easier for a beginner to understand what each part does. It also feels more organized and easier to extend later. This shows that with better planning, code becomes more readable and user-friendly.
"""