import screen 
from survey import AnonymousSurvey

screen.clear()

# Define a questions, and make a survey.
question = "What language did you first learn to speack?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThat you to everyone who participated in the survey!")
my_survey.show_results()
