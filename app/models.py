from app import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

# There are no intentional bugs in this file (but you can certainly add to it if you want)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    token_balance = db.Column(db.Integer, nullable=False, default=0)

class DJClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class MusicSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dj_id = db.Column(db.Integer, db.ForeignKey('dj_club.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    scope_restrictions = db.Column(db.String(255), nullable=True)

class SongRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('music_session.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    artist = db.Column(db.String(120), nullable=True)
    genre = db.Column(db.String(120), nullable=True)
    mood = db.Column(db.String(120), nullable=True)
    region = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=0)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('song_request.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# Marshmallow Schemas for Serialization/Deserialization
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class DJClubSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DJClub
        load_instance = True

class MusicSessionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MusicSession
        load_instance = True
    dj_id = auto_field()
    start_time = auto_field()
    end_time = auto_field()
    status = auto_field()
    scope_restrictions = auto_field()

class SongRequestSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SongRequest
        load_instance = True
    session_id = auto_field()
    user_id = auto_field()
    artist = auto_field()
    genre = auto_field()
    mood = auto_field()
    region = auto_field()
    status = auto_field()
    priority = auto_field()

class DonationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Donation
        load_instance = True
    request_id = auto_field()
    user_id = auto_field()
    amount = auto_field()
    timestamp = auto_field()
