#importing the SQLAlchemy database
from application import db

#creating the table named Todos - part of the SQL database
class Todos(db.Model):
    #creating the individual colunms, assigning data values and constraints
    #need to assign primary key - usually the id of the table
    id = db.Column(db.Integer, primary_key=True)

    task = db.Column(db.String(30), unique=True)

    complete = db.Column(db.Boolean, default=False)