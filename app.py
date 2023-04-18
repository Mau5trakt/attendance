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
    data = request.get_json()
    estudiante = data.get("estudiantes")
    grupo = data.get("grupos")
    semana = data.get("semana")
    dia = data.get("dia")
    bloque = data.get("bloque")
    cumplimiento = data.get("cumplimiento")
    comentario = data.get("comentario")
    staff_id = 1 #! Obtenerlo del login

    for a in range(len(estudiante)):
        obj_estudiante = Estudiantes.query.filter_by(nombre=estudiante[a]).first()
        print(f"obj_estudiante: {obj_estudiante}")
        if obj_estudiante:
            print(f"Nombre: {obj_estudiante.nombre} Codigo: {obj_estudiante.codigo} Grupo: {obj_estudiante.grupo}")
            insercion = Registros(staff_id=staff_id,
                                  estudiante_id=obj_estudiante.id,
                                  ciclo=obj_estudiante.ciclo,
                                  grupo=obj_estudiante.grupo,
                                  nombre=obj_estudiante.nombre,
                                  type="OH",
                                  a_j="A",
                                  oh_week=semana[a],
                                  weekday=dia[a],
                                  hour=bloque[a],
                                  duration=cumplimiento[a])
            db.session.add(insercion)
            db.session.commit()
        #print(f"Estudiante: {estudiante[a]}: Grupo: {grupo[a]} Semana: {semana[a]} Dia: {dia[a]} Bloque: {bloque[a]} "  )
    return redirect(url_for("inicio"))




if __name__ == '__main__':
    app.run()
