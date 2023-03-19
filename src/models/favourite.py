from app import db, ma


class Favourite(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    dancer_id = db.Column(db.Integer, db.ForeignKey('dancers.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __init__(self, dancer_id=None, event_id=None):

        self.dancer_id = dancer_id
        self.event_id = event_id


class FavouriteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Favourite

    id = ma.auto_field()
    dancer_id = ma.auto_field()
    event_id = ma.auto_field()
