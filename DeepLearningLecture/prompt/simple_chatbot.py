responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "bye": "Goodbye!"
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot:", responses["bye"])
            break

        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", responses[key])
                found = True
                break

        if not found:
            print("Chatbot: I don't understand yet.")

chatbot()

"""
The chatbot works, but it’s very limited. It only responds to specific inputs, and if the user asks something else, it just says “I don’t understand yet.” It doesn’t fully meet my expectations because it lacks flexibility. What’s missing is more responses and a smarter way to understand different user questions.
"""