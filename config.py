import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:martin123@db:5432/equiposdb'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-super-segura'
