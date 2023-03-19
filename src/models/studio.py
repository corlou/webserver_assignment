from app import db, ma


class Studio(db.Model):
    __tablename__ = "studios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    street_num = db.Column(db.String)
    street_name = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    contact_num = db.Column(db.String, nullable=False)

    def __init__(self, name=None, street_num=None, street_name=None, postcode=None, contact_num=None):
        self.name = name
        self.street_num = street_num
        self.street_name = street_name
        self.postcode = postcode
        self.contact_num = contact_num


class StudioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Studio

    id = ma.auto_field()
    name = ma.auto_field()
    street_num = ma.auto_field()
    street_name = ma.auto_field()
    postcode = ma.auto_field()
    contact_num = ma.auto_field()
