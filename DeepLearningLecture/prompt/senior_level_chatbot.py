def get_user_name():
    """Ask for the user's name and return it."""
    name = input("Hi! What's your name? ").strip()
    return name if name else "Student"

def greet_user(name):
    """Greet the user."""
    print(f"\nHello, {name}! 👋")
    print("I'm your Python chatbot. Type 'exit' anytime to quit.\n")

def respond(user_input):
    """Return a response based on user input."""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just code, but I'm running perfectly 😄"
    elif "python" in user_input:
        return "Python is a great choice! Clean, powerful, and beginner-friendly."
    elif "help" in user_input:
        return "You can ask me about Python, greetings, or just chat a bit."
    elif user_input == "exit":
        return None
    else:
        return "I'm still learning, so I don't understand that yet."

def run_chatbot():
    """Main function to run the chatbot."""
    name = get_user_name()
    greet_user(name)

    while True:
        user_input = input(f"{name}: ")
        response = respond(user_input)

        if response is None:
            print("Chatbot: Goodbye! 👋")
            break

        print(f"Chatbot: {response}")


if __name__ == "__main__":
    run_chatbot()

"""
Reflection:
The chatbot works pretty good compared to Task 1, but it’s also very limited. It only responds to specific inputs, and if the user asks something else, it just says “I don’t understand yet.” It doesn’t fully meet my expectations because it lacks flexibility. What’s missing is more responses and a smarter way to understand different user questions.
"""

