from app import api

class UserQuestionValidator(object):

    def __init__(self,title,description):
        self.title=title
        self.description=description

    def questionValidator(self):
        #title check
        if type(self.title) != str or self.title.isspace() or len(self.title) < 6:
            api.abort(400, "Question Title is not a number or empty or less than 6 characters. Your input is: {} ".format(self.title))

        #description check
        elif type(self.description) != str or self.description.isspace() or len(self.description) < 10:
            api.abort(400, "Descriptino is not a number or empty or less than 10 characters. Your input is: {} ".format(self.description))

        return True

    @staticmethod
    def answerValidator(description):
        #description check
        if type(description) != str or description.isspace() or len(description) < 10:
            api.abort(400, "Descriptino is not a number or empty or less than 10 characters. Your input is: {} ".format(description))

        return True