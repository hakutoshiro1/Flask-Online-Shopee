from market import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60),nullable=False,unique=True)
    email=db.Column(db.String(60),nullable=False,unique=True)
    password_hash = db.Column(db.String(60),nullable=False)
    budget=db.Column(db.Integer,nullable=False,default=1000)
    items=db.relationship('Item',backref="owned_user",lazy=True)
    def __repr__(self):
        return f'{self.username} {self.id}'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),nullable=False,unique=True)
    barcode = db.Column(db.String(12),nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1024),nullable=False,unique=True)
    owner=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return f'{self.name} {self.id}'