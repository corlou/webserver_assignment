from app import db, ma


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    is_adult = db.Column(db.Boolean, nullable=False)
    # event_type = db.Column(db.Enum, unique=True, nullable=False)
    teacher_name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    studio_id = db.Column(db.Integer, db.ForeignKey('studios.id'))

    def __init__(self, name=None, is_adult=None, teacher_name=None, date=None):
        self.name = name
        self.is_adult = is_adult
        # self.event_type = event_type # remember to add above
        self.teacher_name = teacher_name
        self.date = date


class EventSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Event

    id = ma.auto_field()
    name = ma.auto_field()
    is_adult = ma.auto_field()
    # event_type = ma.auto_field()
    teacher_name = ma.auto_field()
    date = ma.auto_field()
