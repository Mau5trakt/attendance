from flask import Flask, redirect, render_template_string
from database import db
from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from flask_session import Session
from Models import *
from sqlalchemy import desc
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)


with open('cred.txt', 'r') as f:
    primera_linea = f.readline()

app.config['SQLALCHEMY_DATABASE_URI'] = primera_linea
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #   Trackear las modificaciones realizadas
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)



app.config['SECRET_KEY'] = "MBDTF_21THCSM"

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/ohAttendance', methods=["GET", "POST"])
def inicio():  # put application's code here
    estudiantes = Estudiantes.query.order_by('id')
    if request.method == "POST":
        print("Se manda algo")


    return render_template('ohattendance.html', estudiantes=estudiantes)

@app.route('/classAttendance', methods=["GET", "POST"])
def classAttendance():  # put application's code here
    estudiantes = Estudiantes.query.order_by('id')
    return render_template('classAttendance.html', estudiantes=estudiantes)

@app.route('/procesarOH', methods=["GET", "POST"])
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
        obj_estudiante = Estudiantes.query.filter_by(student=estudiante[a]).first()
        print(f"obj_estudiante: {obj_estudiante}")
        if obj_estudiante:
            print(f"Nombre: {obj_estudiante.student} Codigo: {obj_estudiante.code} Grupo: {obj_estudiante.group}")
            insercion = Registros(staff_id=staff_id,
                                  student_id=obj_estudiante.id,
                                  cicle=obj_estudiante.cicle,
                                  group=obj_estudiante.group,
                                  student_name=obj_estudiante.student,
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


@app.route('/procesarClass', methods=["GET", "POST"])
def procesarClass():
    data = request.get_json()
    estudiante = data.get("estudiantes")
    grupo = data.get("grupos")
    lectures = data.get("lectures")
    a_j = data.get("a_j")
    comentario = data.get("comentario")

    staff_id = 1  # ! Obtenerlo del login
    for a in range(len(estudiante)):
        print(f"Estudiante: {estudiante[a]} Grupo: {grupo[a]} Lecture: {lectures[a]} A/J = [{a_j[a]}]")
        obj_estudiante = Estudiantes.query.filter_by(student=estudiante[a]).first()
        if obj_estudiante:
            insercion = Registros(staff_id=staff_id,
                                  student_id=obj_estudiante.id,
                                  cicle=obj_estudiante.cicle,
                                  group=obj_estudiante.group,
                                  student_name=obj_estudiante.student,
                                  type="C",
                                  a_j= a_j[a],
                                  lecture=lectures[a])
            db.session.add(insercion)
            db.session.commit()



    return(redirect(url_for("inicio")))

@app.route('/registros', methods=["GET", "POST"])
def allregisters():  # put application's code here
    registros = Registros.query.order_by(desc('id')).limit(150).all()

    for registro in registros:
        print(registro.id)


    return render_template('registros.html', registros=registros)

if __name__ == '__main__':
    app.run()
