from app.model.manQuestions import QuestionDAO
from app.utility.validQues_Ans import UserQuestionValidator
from app import api
from resources.questions import DAO

class AnswerDAO(QuestionDAO):

    def __init__(self):
        self.answer_id_counter=0
        QuestionDAO.__init__(self)

    def create_answer(self, question_id, data,user_id):
        #check user answer data input
        data_check = UserQuestionValidator.answerValidator(data['description'])

        if data_check == True:
            
            uname=DAO.get_username(user_id)

            if question_id < 0:
                api.abort(400, "Request {} could not be fulfilled due to bad request".format(id)) 
            elif question_id > 0:
                answer = data
                answer['username']=uname
                questions = DAO.questions
                for question in questions:
                    if question.get('id') == question_id:
                        num_ans = len(question['answers'])
                        answer['id'] = num_ans+1
                        question['answers'].append(answer)
                        return answer
            api.abort(404, "question {} dont exist".format(question_id))   


    def find_all_answers_to_question(self,question_id):
        
        for question in DAO.questions:
            if question.get('id') == question_id:
                answers=question['answers']
                return answers

        api.abort(404, "answers for question {} dont exist".format(question_id))
        

    def find_specific_answer_to_question(self,question_id,answer_id):
        answers=self.find_all_answers_to_question(question_id)

        for answer in answers:
            if answer.get('id') == answer_id:
                answer=answer
                return answer
                

        api.abort(404, "The answer {} dont exist".format(answer_id))


    def delete_specific_answer_by_question(self,question_id,answer_id,user_id):
        uname=DAO.get_username(user_id)

        to_delete = self.find_specific_answer_to_question(question_id,answer_id)

        answers=self.find_all_answers_to_question(question_id)
        
        if to_delete.get('username') == uname:
            answers.remove(to_delete)
        else:
            api.abort(403, "You are not the creator of answer {} ".format(answer_id))
                