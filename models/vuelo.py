from config.db import db, ma, app

class Vuelo(db.Model):
    __tablename__ = 'tblvuelo'

    id = db.Column(db.String, primary_key = True)
    aerolinea = db.Column(db.String())
    fechasalida = db.Column(db.String())
    fechallegada = db.Column(db.String())

    def __init__(self, id):
        self.id = id

with app.app_context():
    db.create_all()

class VueloSchema(ma.Schema):
    class Meta:
        fields = ('id', 'aerolinea', 'fechasalida', 'fechallegada')