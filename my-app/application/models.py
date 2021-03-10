from datetime import datetime
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #category column marked as Index so as to be able to group by Category
    category = db.Column(db.String(50),index=True)
    attribute = db.Column(db.String(50),index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
