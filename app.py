from flask import Flask, redirect, render_template_string
from database import db
from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from flask_session import Session
#from Forms import *
#from helpers import *
from Models import *
from sqlalchemy import or_, desc
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Mysql.90210@localhost/attendance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #   Trackear las modificaciones realizadas
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)



app.config['SECRET_KEY'] = "MBDTF_21THCSM"

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=["GET", "POST"])
def inicio():  # put application's code here
    estudiantes = Estudiantes.query.order_by('id')

    if request.method == "POST":
        print("Se manda algo")


    return render_template('index.html', estudiantes=estudiantes)

@app.route('/procesar', methods=["GET", "POST"])
def procesar():
    print("Llega a procesar")
    try:
        data = request.get_json()
        estudiante = data.get("estudiantes")
        grupo = data.get("grupos")
        semana = data.get("semana")
        dia = data.get("dia")
        bloque = data.get("bloque")
        cumplimiento = data.get("cumplimiento")
        comentario = data.get("comentario")


        print(estudiante)
        print(grupo)
        print(semana)
        print(dia)
        print(bloque)
        print(cumplimiento)
        print(comentario)





        print(len(estudiante))

        for a in range(len(estudiante)):
            print(f"Estudiante: {estudiante[a]}: Grupo: {grupo[a]}")
    except:
        print("dato invalido")
        #Crear una ruta para decir que hay un error

        #estudiantes = request.get_data("est")
    #print(estudiantes)
    #datos_estudiantes =  request.get_data("est")
    #datos_str = datos_estudiantes.decode('utf-8')

    #datos_grupo = request.get_data("grup")
    #grupo_str = datos_grupo.decode('utf-8')

    #estudiantes_lista = datos_str.split(',')
    #grupo_lista = grupo_str.split(',')

    #print(estudiantes_lista)
    #print(grupo_lista)





    return redirect(url_for("inicio"))




if __name__ == '__main__':
    app.run()
