from . import db

class EquiposFutbol(db.Model):
    __tablename__ = 'equipos_futbol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    eslogan = db.Column(db.String(100))
    tecnico = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    categoria = db.Column(db.String(50))
    num_goles = db.Column(db.Integer)
    num_partidos_jugados = db.Column(db.Integer)
    num_partidos_ganados = db.Column(db.Integer)
    num_campeonatos = db.Column(db.Integer)
    num_expulsiones = db.Column(db.Integer)
    num_empates = db.Column(db.Integer)
