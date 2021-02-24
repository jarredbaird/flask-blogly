"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first = db.Column(db.String(50),
                           nullable=False)
    
    last = db.Column(db.String(50),
                          nullable=True)
    
    image_url = db.Column(db.String(500),
                          nullable=True,
                          default='/static/images/avatar.png')

    @classmethod
    def get_users_by_last_name(cls, last):
        return cls.query.filter_by(last=last).all()
    
