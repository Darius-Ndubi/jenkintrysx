from app import api
import re

class UserAuthValidator(object):
    def __init__(self,email,username,password,conPassword):
        self.email=email
        self.username=username
        self.password=password
        self.conPassword=conPassword

    def signupValidator(self):
        
    
        #check if email has @ and .com and is type string
        if type(self.email) != str:
            api.abort(400, "An email is a string not a number:{} ".format(self.email))
        
        elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , self.email):
            api.abort(400, "Email: {} is not well formatted (Must have @ and .com)".format(self.email))

        #password check
        elif type(self.password) != str:
            api.abort(400, "A password is a string not a number:{} ".format(self.password))

        elif self.password !=self.conPassword:
            api.abort(400, "Password: {} and confirm_password: {} don't match".format(self.password,self.conPassword))

        elif not re.match(r"[A-Za-z0-9@#$&*]{8,12}",self.password):
             api.abort(400, "Password: {} is not well formatted".format(self.password))
        
        #username check
        elif type(self.username) != str or self.username.isspace() or len(self.username)==0:
            api.abort(400, "A username is not a number or empty: {} ".format(self.username))

        return True
    
    @staticmethod
    def signinValidator(email,password):
        #check if email has @ and .com and is type string
        if type(email) != str:
            api.abort(400, "An email is a string not a number:{} ".format(email))
        
        elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , email):
            api.abort(400, "Email: {} is not well formatted (Must have @ and .com)".format(email))

        elif type(password) != str:
            api.abort(400, "A password is a string not a number:{} ".format(password))

        elif not re.match(r"[A-Za-z0-9@#$&*]{8,12}",password):
             api.abort(400, "Password: {} is not well formatted".format(password))
        
        return True

