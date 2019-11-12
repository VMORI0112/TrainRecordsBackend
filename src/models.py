from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    bp = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120) )
    password = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(220), default='avatar.png')
    

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "avatar": self.avatar,
            "wallet": self.wallet
        }

class AircraftTrainRecords(db.Model):
    bp = db.Column(db.Integer, primary_key=True)
    coursenumber = db.Column(db.Integer)
    hasrecu = db.Column(db.String(1)) 
    

