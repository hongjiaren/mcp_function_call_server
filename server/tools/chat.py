def chat_with_ai(message):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a program, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }
    return responses.get(message.lower(), "I'm sorry, I didn't understand that.")
