from config.db import db, ma, app

class Avion(db.Model):
    __tablename__ = 'tblavion'

    id = db.Column(db.String, primary_key = True)
    tipo = db._Column(db.String())
    capacidad  = db.Column(db.String())

    def __init__(self, id):
        self.id = id

with app.app_context():
    db.create_all()

class AvionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipo', 'capacidad')

        