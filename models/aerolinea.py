from config.db import db, ma, app

class Aerolinea(db.Model):
    __tablename__ = 'tblaerolinea'

    nombre = db.Column(db.String, primary_key= True)
    codigo = db.Column(db.String(10))
    pais = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class AerolineaSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'codigo', 'pais')