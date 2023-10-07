from config.db import db, ma, app

class DetalleVuelo(db.Model):
    __tablename__ = 'tbldetallevuelo'

    idVuelo = db.Column(db.String, primary_key = True)
    aerolinea = db.Column(db.String())
    fechasalida = db.Column(db.String())
    fechallegada = db.Column(db.String())
    duracion = db.Column(db.String())
    origen = db.Column(db.String())
    destino = db.Column(db.String())

    def __init__(self, idVuelo):
        self.idVuelo = idVuelo 

with app.app_context():
    db.create_all()

    class DetalleVueloSchema(ma.Schema):
        class Meta:
            fields = ('idVuelo', 'aerolinea', 'fechasalida', 'fechallegada', 'duracion', 'origen', 'destino' )

