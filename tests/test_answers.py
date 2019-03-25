import pytest
from flask import json
from app import app
from tests.test_user_auth import login_token,mock_reg

mock_ans=[{"description":""},
          {"description":123546},
          {"description":"How do i add api secret key in python?"}]

def test_Answer_empty_description():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[0]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)


def test_Answer_int_description():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[1]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 400)


def test_Answer_successfull_description_post():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.post('/questions/3/answers', data=json.dumps(mock_ans[2]),content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 201)


def test_Answer_all_answers_to_question():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.get('/questions/3/answers',content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 200)


def test_AnswerActions_locate_answer_by_id():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.get('/questions/3/answers/2',content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 200)


def test_AnswerActions_delete_answer_by_id():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.delete('/questions/3/answers/2',content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        assert(response.status_code == 204)

def test_AnswerActions_delete_answer_by_id_deleted_answer():
    with app.app_context():
        result = app.test_client()
        tok=login_token(mock_reg[4].get('id'))
        response = result.delete('/questions/3/answers/2',content_type='application/json',headers={ 'Authorization': 'Bearer ' + tok })
        assert(response.status_code == 404)
