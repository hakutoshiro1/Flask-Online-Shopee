from market import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),nullable=False,unique=True)
    barcode = db.Column(db.String(12),nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1024),nullable=False,unique=True)
    def __repr__(self):
        return f'{self.name} {self.id}'