from marjong import db

class Tiles(db.Model):
    __tablename__ = 'tiles'
    id = db.Column(db.Integer,primary_key=True)
    tilename = db.Column(db.String(2))
    link = db.Column(db.String(2))

    def __init__(self, id=None, tilename=None, link=None):
        self.id = id
        self.tilename = tilename
        self.link = link

    def __repr__(self):
        return '<Title id:{} name:{} link:{}>'.format(self.id, self.tilename, self.link)

