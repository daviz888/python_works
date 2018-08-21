import screen
screen.clear()

prompt = "Tell me something, and i will repeat it back to you:"
prompt += "\nEnter '[Q]uit the program. "

active = True
message = ""
while active:
    message = input(prompt)

    if message == 'quit' or message.upper() == 'Q':
        active = False
    else:
        print(message)
