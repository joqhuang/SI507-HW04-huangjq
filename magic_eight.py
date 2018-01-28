import random

PossibleAnswers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don\'t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def get_user_question():
    user_q = input("What is your question? ")
    return user_q

def PickRandomAnswer(Answers):
    return random.choice(Answers)

user_question = ""
while user_question != "quit":
    user_question = get_user_question()
    if user_question[-1] != "?":
        print("I'm sorry, I can only answer questions. Or enter quit to end the program.")
