from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from flask_jwt_extended import JWTManager
from datetime import timedelta


app = Flask(__name__)
jwt = JWTManager(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config['JWT_SECRET_KEY'] = '\xe7\x06K\x86\xe5\x98/\x11\x06\xfbJA\x86'
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(minutes=5)

api = Api(app, version='1.0', title='Ask It API',
    description='A simple Question & Answer API',)

from resources.user_auth import ns as auth
api.add_namespace(auth)

from resources.questions import ns as questions
api.add_namespace (questions)

from resources.answers import ns as questions
api.add_namespace (questions)