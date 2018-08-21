import screen
screen.clear()

prompt = "\nPlease enter the name of the City you have visited:"
prompt += "\n(Enter 'quit' when you ae finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")