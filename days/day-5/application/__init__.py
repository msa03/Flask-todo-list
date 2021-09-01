#import relevant pre-existing modules for use in my code
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

# define our app variable
app = Flask(__name__)
#assigning an environment variable to the key = SQLAlchemy_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI') 
#MUST have a secret key
app.config['SECRET_KEY'] = "my-secret"

# setting our database to a class and passing in the parameter app
#the app variable is a class called Flask
db = SQLAlchemy(app)

#import our routes file from the application directory
from application import routes
