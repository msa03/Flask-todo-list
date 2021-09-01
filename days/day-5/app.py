#import the app variable (app is the class Flask)
from application import app

#checks if the current module is 'main' - if it is, runs the application for the Flask application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')