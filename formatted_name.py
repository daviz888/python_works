import screen
screen.clear()

def get_formatted_name(first_name, last_name, middle_name=''):
    # Return a full name, neatly formatted
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('dovvy', 'pacamalan')

print(musician)