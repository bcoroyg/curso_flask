from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from dotenv import load_dotenv
import os

# creamos instancia de Flask
app = Flask(__name__)
bootstrap = Bootstrap4(app)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

todos = ['Todo 1', 'Todo 2', 'Todo 3']


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Enviar')


# Error 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Error 500


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    # request.remote_addr ==> obtiene la ip del usuario(quien realiza la peticion)
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip) ===> Almacena la ip en la cookie del navegador
    # response.set_cookie('user_ip', user_ip)

    session['user_ip'] = user_ip

    return response


@app.route("/hello", methods=['GET', 'POST'])
def hello():
    # request.cookies.get('user_ip') ==> obtiene la ip del usuario que esta almacenada en la cookie
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }
    
    if login_form.validate_on_submit():
        username= login_form.username.data
        session['username'] = username
        
        flash('Nombre de usuario registrado con éxito!')
        
        return redirect(url_for('index'))

    # return 'Bienvenido, tu IP es {}'.format(user_ip)
    # return render_template("index.html", user_ip=user_ip, todos=todos)
    return render_template("index.html", **context)
