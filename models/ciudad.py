from config.db import db, ma, app

class Ciudad(db.Model):
    __tablename__ = 'tblciudad'

    nombre = db.Column(db.String, primary_key = True)
    pais = db.Column(db.String())

    def __init__(self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class CiudadSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'pais')