from flask import Flask

# creamos instancia de Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return 'Welcome!'
