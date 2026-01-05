from flask import Flask, render_template_string, render_template
import mysql.connector
from forms import RegisterForm, LoginForm

app = Flask(__name__)

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="rasmus",
        password="R-asmus150508",
        database="test"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/i')
def i():
    return render_template('i.html')

if __name__ == "__main__":
    app.run()