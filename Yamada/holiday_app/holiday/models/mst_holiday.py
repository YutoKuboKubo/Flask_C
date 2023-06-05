from holiday import db
from datetime import datetime

class Holiday (db.Model):
    __tablename__ = 'holidays'
    holi_date = db.Column(db.DateTime, primary_key=True)
    holi_text = db.Column(db.String(20))

def __init__(self, holi_text=None):
    self.holi_date = datetime.utcnow()
    self.hoki_text = holi_text

