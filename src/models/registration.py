from app import db, ma


class Registration(db.Model):
    __tablename__ = "registrations"
    id = db.Column(db.Integer, primary_key=True)
    dancer_id = db.Column(db.Integer, db.ForeignKey('dancers.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    date_registered = db.Column(db.Date, nullable=False)

    def __init__(self, dancer_id=None, event_id=None, date_registered=None):
        self.dancer_id = dancer_id
        self.event_id = event_id
        self.date_registered = date_registered


class RegistrationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Registration

    id = ma.auto_field()
    dancer_id = ma.auto_field()
    event_id = ma.auto_field()
    date_registered = ma.auto_field()
