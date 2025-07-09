from flask import Blueprint, request, jsonify
from .models import EquiposFutbol
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/equipos', methods=['GET'])
def get_equipos():
    equipos = EquiposFutbol.query.all()
    data = [vars(e).copy() for e in equipos]
    for item in data:
        item.pop('_sa_instance_state', None)
    return jsonify(data), 200

@routes.route('/equipos/<int:id>', methods=['GET'])
def get_equipo(id):
    equipo = EquiposFutbol.query.get(id)
    if not equipo:
        return jsonify({'error': 'Equipo no encontrado'}), 404
    data = vars(equipo).copy()
    data.pop('_sa_instance_state', None)
    return jsonify(data), 200

@routes.route('/equipos', methods=['POST'])
def create_equipo():
    data = request.json
    equipo = EquiposFutbol(**data)
    db.session.add(equipo)
    db.session.commit()
    return jsonify({'message': 'Equipo creado correctamente'}), 201

@routes.route('/equipos/<int:id>', methods=['PUT'])
def update_equipo(id):
    equipo = EquiposFutbol.query.get(id)
    if not equipo:
        return jsonify({'error': 'Equipo no encontrado'}), 404

    data = request.json
    for key, value in data.items():
        setattr(equipo, key, value)
    db.session.commit()
    return jsonify({'message': 'Equipo actualizado correctamente'}), 200

@routes.route('/equipos/<int:id>', methods=['DELETE'])
def delete_equipo(id):
    equipo = EquiposFutbol.query.get(id)
    if not equipo:
        return jsonify({'error': 'Equipo no encontrado'}), 404

    db.session.delete(equipo)
    db.session.commit()
    return jsonify({'message': 'Equipo eliminado correctamente'}), 200
