from datetime import datetime

from app import db

class Estudiantes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(10), nullable=False)
    ciclo = db.Column(db.String(5), nullable=False) #Y23C2
    nombre = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(1), nullable=False)

    registros = db.relationship('Registros', back_populates="estudiante")

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.Integer, nullable=False)

    registros = db.relationship('Registros', back_populates='staff')


class Registros(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.Date(), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
    ciclo = db.Column(db.String(5), nullable=False) #? Se repite pero aha
    grupo = db.Column(db.String(1), nullable=False) #* Buscar la forma de generar el reporte con una sola consulta sql que no implique repetir los campos
    nombre = db.Column(db.String(100), nullable=False)
    lecture = db.Column(db.Integer)
    type = db.Column(db.String(2), nullable=False)
    a_j = db.Column(db.String(1), nullable=False)
    oh_week = db.Column(db.Integer)
    weekday = db.Column(db.String(15), nullable=False)
    hour = db.Column(db.String(6), nullable=False)
    duration = db.Column(db.Integer)

    staff = db.relationship('Staff', back_populates='registros')
    estudiante = db.relationship('Estudiantes', back_populates='registros')