from app import db, ma


class Dancer(db.Model):
    __tablename__ = "dancers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    # studio_id = db.Column(db.Integer, db.ForeignKey('studios.id'))

    def __init__(self, name=None, password=None, email=None, date_of_birth=None):
        self.name = name
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth


class DancerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dancer

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    date_of_birth = ma.auto_field()
