from app import api
from resources.user_auth import UAO
from app.utility.validQues_Ans import UserQuestionValidator

class QuestionDAO(object):
    

    def __init__(self):
        self.counter = 0
        self.questions = []
    

    def get_username(self,user_id):
        for user in UAO.users:
            if user.get('id') == user_id:
                return user['username']
            else:
                api.abort(403, "You are not the creator of question {} ".format(id))
    
    def get(self, id):
        # if id <= 0:
        #    api.abort(400, "Request {} could not be fulfilled due to bad request".format(id)) 
        
        # else:
        for question in self.questions:
            if question['id'] == id:
                return question
        api.abort(404, "question {} doesn't exist".format(id))
        

    def create(self, data,user_id):
        #validate user data
        questionValidatorO = UserQuestionValidator(data['title'],data['description'])
        data_check = questionValidatorO.questionValidator()

        if data_check == True:

            uname=self.get_username(user_id)
            question = data
            question['id'] = self.counter = self.counter + 1    
            question['username']=uname
            self.questions.append(question)
            
            return question


    def update_question(self, id, data, user_id):

        questionValidatorO = UserQuestionValidator(data['title'],data['description'])
        data_check = questionValidatorO.questionValidator()

        if data_check == True:

            uname = self.get_username(user_id)
            question = self.get(id)
            if question.get('username') == uname:
                question.update(data)
                return question

            else:       
                api.abort(403, "You are not the creator of question {} ".format(id))


    def delete_question(self, id,user_id):
        uname=self.get_username(user_id)
        question = self.get(id)
        
        if question.get('username') == uname:
            self.questions.remove(question)
        else:       
            api.abort(403, "You are not the creator of question {} ".format(id))