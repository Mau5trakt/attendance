from flask import Flask, redirect, render_template_string
from consultas import *
from database import db
from flask import Flask, render_template, request, url_for, session
from flask_migrate import Migrate
from flask_session import Session
from functions import *
from tempfile import mkdtemp
from Models import *
from sqlalchemy import desc
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'attendamce.db') #TODO: Change the name for attendance

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #   Trackear las modificaciones realizadas
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)



app.config['SECRET_KEY'] = "MBDTF_21THCSM"

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/iniciar', methods=["GET", "POST"])
def login():
    session.clear()
    if request.method =="POST":
        if not request.form.get("user"):
            return apology("Ingrese su usuario", 403)

        if not request.form.get("password"):
            return apology("Ingrese su contraseña", 403)

        user = request.form.get("user")
        passw = request.form.get("password")

        print("user", user)

        staff = Staff.query.filter_by(code=user).first()
        print("staff", staff)

        if staff is None or not check_password_hash(staff.password, passw):
            return apology("Usuario o Clave Incorrecto", 403)

        session["code"] = staff.code

        return render_template("ohattendance.html")






    return render_template('login.html')  # put application's code here



# Ruta principal

@app.route('/', methods=["GET", "POST"])
@login_required
def inicio():  # put application's code here
    estudiantes = Estudiantes.query.order_by('id')
    if request.method == "POST":
        print("Se manda algo")


    return render_template('ohattendance.html', estudiantes=estudiantes)

@app.route('/classAttendance', methods=["GET", "POST"])
@login_required
def classAttendance():  # put application's code here
    estudiantes = Estudiantes.query.order_by('id')
    return render_template('classAttendance.html', estudiantes=estudiantes)

@app.route('/procesarOH', methods=["GET", "POST"])
@login_required
def procesar():
    data = request.get_json()
    estudiante = data.get("estudiantes")
    grupo = data.get("grupos")
    semana = data.get("semana")
    dia = data.get("dia")
    bloque = data.get("bloque")
    cumplimiento = data.get("cumplimiento")
    comentario = data.get("comentario")
    staff_id = session["code"] #! Obtenerlo del login

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
                                  duration=cumplimiento[a],
                                  comment=comentario[a])
            db.session.add(insercion)
            db.session.commit()
        #print(f"Estudiante: {estudiante[a]}: Grupo: {grupo[a]} Semana: {semana[a]} Dia: {dia[a]} Bloque: {bloque[a]} "  )
    return redirect(url_for("inicio"))


@app.route('/procesarClass', methods=["GET", "POST"])
@login_required
def procesarClass():
    data = request.get_json()
    estudiante = data.get("estudiantes")
    grupo = data.get("grupos")
    lectures = data.get("lectures")
    a_j = data.get("a_j")
    comentario = data.get("comentario")

    staff_id = session["code"]  # ! Obtenerlo del login
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
                                  lecture=lectures[a],
                                  comment=comentario[a])

            db.session.add(insercion)
            db.session.commit()



    return(redirect(url_for("inicio")))

@app.route('/registros', methods=["GET", "POST"])
@login_required
def allregisters():
    registros = Registros.query.order_by(desc('id')).limit(150).all()
    query = db.session.execute(reporteOhMembers).fetchall()

    for registro in registros:
        print(registro.id)

    print(type(registros))

    return render_template('registros.html', registros=registros, query=query)

@app.route('/membersOH', methods=["GET", "POST"])
@login_required
def members():
    #query = db.session.execute('SELECT estudiantes.*, COALESCE(sum(registros.duration), 0) as cantidad FROM estudiantes LEFT JOIN registros ON estudiantes.student = registros.student_name WHERE estudiantes.cicle = "Y23C1" GROUP BY estudiantes.student ORDER BY estudiantes.id;').fetchall()
    query = db.session.execute(reporteOhMembers).fetchall()
    #reporteOhMembers es la consulta importada de `consultas.py`
    for consulta in query:
        print(consulta)

    print(type(query))







    return render_template('membersOH.html', query=query)


if __name__ == '__main__':
    app.run()
