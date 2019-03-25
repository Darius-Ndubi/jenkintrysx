import pytest
from flask import json
from app import app
from flask_jwt_extended import create_access_token

mock_reg=[{"email":"","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelightgmail.com","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":123454,"username":"delight","password":"delight","confirm_password":"delight"},

          {"id":1,"email":"yagamidelight@gmail.com","username":"delight","password":"string@12","confirm_password":"string@12"},

          {"email":"yagamidelight@gmail.com","username":"delight","password":123,"confirm_password":123},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight@11","confirm_password":"delight@1"},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight","confirm_password":"delight"},

          {"email":"yagamidelight@gmail.com","username":12334,"password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"      ","password":"delight","confirm_password":"delight"}
]

mock_log=[{"email":123,"password":"delight"},
          {"email":"","password":"delight"},
          {"email":"yagamidelight.com","password":"delight"},
          {"email":"yagamidelight@gmail","password":"delight"},

          {"email":"yagamidelight@gmail.com","password":123},
          {"email":"yagamidelight@gmail.com","password":"deli"},

          {"email":"yagamidelight@gmail","password":"string@12"}            
]

#create_login_token
def login_token(user_id):
    access_token = create_access_token(user_id)
    return access_token


#email checks
def test_signup_empty_email():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[0]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    #assert response == {"Email: {} is not well formatted (Must have @ and .com".format(mock_reg[0].get('email'))}
    assert(response.status_code == 400)

def test_signup_wrong_email1():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[1]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_wrong_email2():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[2]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_int_email():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[3]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#password checks
def test_signup_int_password():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[5]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    #assert response == {"Email: {} is not well formatted (Must have @ and .com".format(mock_reg[0].get('email'))}
    assert(response.status_code == 400)

def test_signup_passwords_unmatching():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[6]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_poor_passwords():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[7]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#username checks
def test_signup_int_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[8]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_empty_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[9]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_spaces_username():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[10]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

#test correct data
def test_signup_correct_data():
    result = app.test_client()
    response = result.post('/auth/signup', data=json.dumps(mock_reg[4]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert (response.status_code == 201)


#test signin
def test_signin_int_email():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[0]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signin_empty_email():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[1]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signin_wrong_email1():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[2]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signin_wrong_email2():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[3]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signin_int_password():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[4]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signup_poor_password():
    result = app.test_client()
    response = result.post('/auth/signin', data=json.dumps(mock_log[5]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)


def test_signin_correct_data():
    with app.app_context():
        result = app.test_client()
        response = result.post('/auth/signin', data=json.dumps(mock_log[6]),content_type='application/json')
        json.loads(response.data.decode('utf-8'))
        user_id=mock_reg[4].get('id')
        assert response != login_token(user_id)