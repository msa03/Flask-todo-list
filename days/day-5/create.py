#import the SQLAlchemy databse from __init__.py
from application import db

#create the database
db.create_all()