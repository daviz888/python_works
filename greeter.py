import screen
screen.clear()

def greet_user(username):
    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is you first name? "
    name = input(prompt)
    print("Hello, " + name.title() + " and " + username.title() + " !")

greet_user('daffy')