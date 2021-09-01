#importing existing modules after installing necessary module packages
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

#importing our table as a class, from the models file
from application.models import Todos

#creating a class and passing in the parameter 
class TodoForm(FlaskForm):
    #creating a variable called task, defining a data type, giving it a lable and validator
    task = StringField('Task',
        validators = [
            DataRequired(),
        ]    
    )
    #creates a submit button with the lable 'Submit' - at the end of a form
    submit = SubmitField('Submit')

    #defining a new method with two parameters
    #calls on the task variable in line 12
    def validate_task(self, task):

        #new variable that searches the Todos table 
        todos = Todos.query.all()
        #iteration through each instance in the table
        for todo in todos:
            #checks if current task already exists in Todo
            if todo.task == task.data:
                #raises error message if it already exists
                raise ValidationError('You already added this Todo')

#creates a class
class OrderTodo(FlaskForm):
    #creates a dropdown list with options, with label and choices
    order_with = SelectField('Order With',
        #("what_is_read_on_backend", "what_is_shown_on_front_end")
        choices=[
            ("complete", "Completed"),
            ("id", "Recent"),
            ("old", "Old"),
            ('incomplete', "Incomplete")
        ]
    )
    #submit button with label
    submit = SubmitField('Order')