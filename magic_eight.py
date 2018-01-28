def get_user_question():
    user_q = input("What is your question? ")
    return user_q

user_question = ""
while user_question != "quit":
    user_question = get_user_question()
    if user_question[-1] != "?":
        print("I'm sorry, I can only answer questions. Or enter quit to end the program.")
