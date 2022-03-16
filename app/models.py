from . import db

class Property(db.Model):
    """Database"""
    __tablename__ = 'property_info'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Float)
    location = db.Column(db.String)
    price = db.Column(db.Float)
    ptype = db.Column(db.String(80))
    description = db.Column(db.String)
    photo = db.Column(db.String)

    def __init__(self, title, num_bedrooms, num_bathrooms, location, price, ptype, description, photo):
        self.title = title
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self.ptype = ptype
        self.description = description
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)