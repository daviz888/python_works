class AnonymousSurvey():
    """ Collect anonymous answer to a survey questions """

    def __init__(self, question):
        """Store a questionm and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all responses that have been given."""
        print("Survery results:")
        for response in self.responses:
            print('- ' + response)


