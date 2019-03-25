from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from flask_jwt_extended import jwt_required,get_jwt_identity
from app import api
from app.model.manQuestions import QuestionDAO

ns = api.namespace('questions', description='QUESTION operations')

#data model for answer
answer = api.model('Answer',{
    'id': fields.Integer(readOnly=True, description='The answer unique identifier'),
    'username': fields.String(readOnly=True, description='Your username detail'),
    'description': fields.String(required=False, description='The answer detail'),
    'action': fields.String(required=False, description='The answer status from question owner')
})

question = api.model('Question', {
    'id': fields.Integer(readOnly=True, description='The question unique identifier'),
    'username': fields.String(readOnly=True, description='Your username detail'),
    'title': fields.String(required=True, description='The title detail'),
    'description': fields.String(required=True, description='The question detail'),
    'answers': fields.List(fields.Nested(answer)),
})

DAO = QuestionDAO()
DAO.create({'username':'Ken','title': 'Build an API','description':'Write endpoints','answers':[{'id':1,'description':'make simple endpoint for testing to understand API with Flask'}]},10)
DAO.create({'username':'Brian','title': 'Test the API','description':'Write Tests','answers':[{'id':1,'description':'Have unittests to test your endpoint functionality'},{'id':2,'description':'Ensure your tests are robust for more coverage'}]},11)
DAO.create({'username':'Sharon','title': 'Deploy the API','description':'Heroku deployment','answers':[{'id':1,'description':'Create an account on heroku and deploy your app with help of heroku CLI check https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0'}]},12)

@ns.route('/')
class QuestionList(Resource):

    '''Shows a list of all questions, and lets you POST to add new tasks'''
    @ns.doc('list_questions')
    @ns.marshal_list_with(question)
    def get(self):
        '''List all questions'''
        return DAO.questions


    @jwt_required
    @ns.doc('create_question')
    @ns.expect(question)
    @ns.marshal_with(question, code=201)
    def post(self):
        '''Create a new title'''

        user_id=get_jwt_identity()
        return DAO.create(api.payload,user_id), 201


@ns.route('/<int:id>')
@ns.response(404, 'question not found')
@ns.param('id', 'The question identifier')
class Question(Resource):
    '''Show a single question item and lets you delete them'''
    @ns.doc('get_question')
    @ns.marshal_with(question)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)



    @jwt_required
    @ns.expect(question)
    @ns.marshal_with(question)
    def put(self, id):
        '''Update a title given its identifier'''

        user_id = get_jwt_identity()
        return DAO.update_question(id, api.payload,user_id)



    @jwt_required
    @ns.doc('delete_question')
    @ns.response(204, 'question deleted')
    def delete(self, id):
        '''Delete a title given its identifier'''

        user_id = get_jwt_identity()
        DAO.delete_question(id,user_id)
        return '', 204
