from flask import request, make_response, redirect, render_template, session, flash, url_for
from flask_login import login_required, current_user

import unittest

from app import create_app

from app.firestore_service import get_todos, put_todo

from app.forms import TodoForm

# creamos instancia de Flask
# app = Flask(__name__)
# bootstrap = Bootstrap4(app)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app = create_app()

# todos = ['Todo 1', 'Todo 2', 'Todo 3']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

# Error 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Error 500


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)


@app.route('/index')
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
@login_required
def hello():
    # request.cookies.get('user_ip') ==> obtiene la ip del usuario que esta almacenada en la cookie
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    # username = session.get('username')
    username = current_user.id

    todo_form = TodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        
        flash('Tu tarea se creo con éxito!')
        
        return redirect(url_for('hello'))

    # return 'Bienvenido, tu IP es {}'.format(user_ip)
    # return render_template("index.html", user_ip=user_ip, todos=todos)
    return render_template("index.html", **context)
