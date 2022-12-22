from flask import Flask, request

# creamos instancia de Flask
app = Flask(__name__)


@app.route("/")
def hello():
    #request.remote_addr ==> obtiene la ip del usuario(quien realiza la peticion)
    user_ip=request.remote_addr
    return 'Bienvenido, tu IP es {}'.format(user_ip)
