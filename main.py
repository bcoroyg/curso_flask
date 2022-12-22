from flask import Flask, request, make_response, redirect, render_template

# creamos instancia de Flask
app = Flask(__name__)

todos = ['Todo 1', 'Todo 2', 'Todo 3']


@app.route('/')
def index():
    # request.remote_addr ==> obtiene la ip del usuario(quien realiza la peticion)
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip) ===> Almacena la ip en la cookie del navegador
    response.set_cookie('user_ip', user_ip)

    return response


@app.route("/hello")
def hello():
    # request.cookies.get('user_ip') ==> obtiene la ip del usuario que esta almacenada en la cookie
    user_ip = request.cookies.get('user_ip')

    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    # return 'Bienvenido, tu IP es {}'.format(user_ip)
    # return render_template("index.html", user_ip=user_ip, todos=todos)
    return render_template("index.html", **context)
