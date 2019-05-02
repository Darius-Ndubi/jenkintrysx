import pytest
from flask import json
from app import app
from tests.test_user_auth import login_token,mock_reg

mock_ques=[{"title":"","description":"How do i add api secret key in python?"},
           {"title":"Secret API","description":""},
           {"title":"Secret API","description":"How do i add api secret key in python?"}]

def test_QuestionList_empty_title():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/', data=json.dumps(mock_ques[0]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)

def test_QuestionList_empty_description():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/', data=json.dumps(mock_ques[1]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)

def test_QuestionList_successfull_post():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/', data=json.dumps(mock_ques[2]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        assert(response.status_code == 201)

def test_QuestionList_successfull_get():
    result = app.test_client()
    response = result.get('/questions/',content_type='application/json')
    assert(response.status_code == 200)


def test_Question_successfull_get():
    result = app.test_client()
    response = result.get('/questions/1',content_type='application/json')
    assert(response.status_code == 200)

#test on user edit question

def test_QuestionList_successfull_put():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.put('/questions/4', data=json.dumps(mock_ques[2]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        assert(response.status_code == 200)


"""
    test delete question
"""
def test_QuestionList_successfull_delete():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.delete('/questions/4', data=json.dumps(mock_ques[2]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        assert(response.status_code == 204)