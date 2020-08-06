from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Todo App Home"

@app.route('/add')
def add():
    return "Add a new Todo"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')