from app import app
from flask import jsonify, request
from app.models import *


@app.route('/api/users/')
def get_users():
    all_users = User.query.all()
    result = UserSchema.dump(all_users)
    return jsonify(result)

@app.route('/api/users/<id>')
def user_detail(id):
    sel_user = User.query.filter_by(id=id).first()
    return UserSchema.jsonify(sel_user)

@app.route('/api/users/<id>/songrequests/')
def get_user_songrequests(id):
    all_songrequests = SongRequest.query.filter_by(user_id=id).all()
    result = SongRequestSchema.dump(all_songrequests)
    return jsonify(result)

@app.route('/api/users/<id>/donations/')
def get_user_donations(id):
    all_donations = Donation.query.filter_by(user_id=id).all()
    result = DonationSchema.dump(all_donations)
    return jsonify(result)

@app.route('/api/djclubs/')
def get_djclubs():
    all_djclubs = DJClub.query.all()
    result = DJClubSchema.dump(all_djclubs)
    return jsonify(result)

@app.route('/api/djclubs/<id>')
def djclub_detail(id):
    sel_djclub = DJClub.query.filter_by(id=id).first()
    return DJClubSchema.jsonify(sel_djclub)

@app.route('/api/djclubs/<id>/musicsessions/')
def get_djclub_musicsessions(id):
    all_musicsessions = MusicSession.query.filter_by(dj_id=id).all()
    result = MusicSessionSchema.dump(all_musicsessions)
    return jsonify(result)s

@app.route('/api/musicsessions/')
def get_musicsessions():
    all_musicsessions = MusicSession.query.all()
    result = MusicSessionSchema.dump(all_musicsessions)
    return jsonify(result)

@app.route('/api/musicsessions/<id>')
def musicsession_detail(id):
    sel_musicsession = MusicSession.query.filter_by(id=id).first()
    return MusicSessionSchema.jsonify(sel_musicsession)

@app.route('/api/musicsessions/', methods=['POST'])
def create_musicsession():
    data = request.get_json()
    new_musicsession = MusicSession(
        dj_id=data['dj_id'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        status=data['status'],
        scope_restrictions=data['scope_restrictions']
    )
    db.session.add(new_musicsession)
    db.session.commit()
    return MusicSessionSchema.jsonify(new_musicsession)

@app.route('/api/musicsessions/<id>', methods=['PUT'])
def update_musicsession(id):    
    sel_musicsession = MusicSession.query.filter_by(id=id).first()
    data = request.get_json()
    sel_musicsession.status = data['status']
    db.session.commit()
    return MusicSessionSchema.jsonify(sel_musicsession)

@app.route('/api/musicsessions/<id>', methods=['DELETE'])
def delete_musicsession(id):
    sel_musicsession = MusicSession.query.filter_by(id=id).first()
    db.session.delete(sel_musicsession)
    db.session.commit()
    return MusicSessionSchema.jsonify(sel_musicsession)

@app.route('/api/musicsessions/<id>/songrequests/')
def get_musicsession_songrequests(id):
    all_songrequests = SongRequest.query.filter_by(session_id=id).all()
    result = SongRequestSchema.dump(all_songrequests)
    return jsonify(result)

@app.route('/api/songrequests/')
def get_songrequests():
    all_songrequests = SongRequest.query.all()
    result = SongRequestSchema.dump(all_songrequests)
    return jsonify(result)

@app.route('/api/songrequests/<id>')
def songrequest_detail(id):
    sel_songrequest = SongRequest.query.filter_by(id=id).first()
    return SongRequestSchema.jsonify(sel_songrequest)

@app.route('/api/songrequests/', methods=['POST'])
def create_songrequest():
    data = request.get_json()
    new_songrequest = SongRequest(
        session_id=data['session_id'],
        user_id=data['user_id'],
        artist=data['artist'],
        genre=data['genre'],
        mood=data['mood'],
        region=data['region'],
        status=data['status'],
        priority=data['priority']
    )
    db.session.add(new_songrequest)
    db.session.commit()
    return SongRequestSchema.jsonify(new_songrequest)

@app.route('/api/songrequests/<id>', methods=['PUT'])
def update_songrequest(id):
    sel_songrequest = SongRequest.query.filter_by(id=id).first()
    data = request.get_json()
    sel_songrequest.status = data['status']
    db.session.commit()
    return SongRequestSchema.jsonify(sel_songrequest)

@app.route('/api/songrequests/<id>', methods=['DELETE'])
def delete_songrequest(id):
    sel_songrequest = SongRequest.query.filter_by(id=id).first()
    db.session.delete(sel_songrequest)
    db.session.commit()
    return SongRequestSchema.jsonify(sel_songrequest)

@app.route('/api/donations/')
def get_donations():
    all_donations = Donation.query.all()
    result = DonationSchema.dump(all_donations)
    return jsonify(result)

@app.route('/api/donations/<id>')
def donation_detail(id):
    sel_donation = Donation.query.filter_by(id=id).first()
    return DonationSchema.jsonify(sel_donation)

@app.route('/api/donations/', methods=['POST'])
def create_donation():
    data = request.get_json()
    new_donation = Donation(
        request_id=data['request_id'],
        user_id=data['user_id'],
        amount=data['amount']
    )
    db.session.add(new_donation)
    db.session.commit()
    return DonationSchema.jsonify(new_donation)

@app.route('/api/donations/<id>', methods=['PUT'])
def update_donation(id):
    sel_donation = Donation.query.filter_by(id=id).first()
    data = request.get_json()
    sel_donation.amount = data['amount']
    db.session.commit()
    return DonationSchema.jsonify(sel_donation)

@app.route('/api/donations/<id>', methods=['DELETE'])
def delete_donation(id):
    sel_donation = Donation.query.filter_by(id=id).first()
    db.session.delete(sel_donation)
    db.session.commit()
    return DonationSchema.jsonify(sel_donation)

