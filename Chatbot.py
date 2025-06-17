def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    elif "What are you doing" in user_input:
        return "I am helping you"
    elif "Who is the current presodent of Bangladesh" in user_input:
        return "Mohammad Younus"
    elif "How about you" in user_input:
        return "I am doing well"
    elif "Whats your favourite movie" in user_input:
        return "I don't have any personal favourite cause I am just a chatbot"
    elif "Do you like Pizza" in user_input:
        return "I can't test cause I am a machine"
    elif "Which religion is you from" in user_input:
        return "I don't follow any spesific religion"
    elif "Where are you live" in user_input:
        return "I am living in your Heart"
    elif "Where are you from" in user_input:
        return "I am from your Computer"
    elif "Sorry" in user_input:
        return "Its okay, my dear"
    elif "Thank You" in user_input:
        return "You are most welcome"
    elif "I love you" in user_input:
        return "I love you too my dear"
    else:
        return "Sorry, I didn't understand that."


print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
