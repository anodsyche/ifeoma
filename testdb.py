from app import db
from app.models import User, MusicSession, SongRequest, Donation, DJClub

def create_test_db():
    # Drop the existing test database (if it exists)
    db.drop_all()

    # Create a new test database
    db.create_all()

    # Add some sample data for testing
    user1 = User(username='testuser1', email='test1@example.com', password='password', token_balance=100)
    user2 = User(username='testuser2', email='test2@example.com', password='password', token_balance=100)
    
    dj1 = DJClub(name='Test DJ 1', email='dj1@example.com', password='password')
    dj2 = DJClub(name='Test DJ 2', email='dj2@example.com', password='password')

    session1 = MusicSession(dj_id=1, start_time='2021-01-01 20:00:00', end_time='2021-01-01 23:00:00', status='open', scope_restrictions='genre:pop')
    session2 = MusicSession(dj_id=2, start_time='2021-01-02 21:00:00', end_time='2021-01-02 23:00:00', status='open', scope_restrictions='genre:rock')

    request1 = SongRequest(session_id=1, user_id=1, artist='Artist 1', genre='pop', mood='happy', region='USA', status='pending', priority=1)
    request2 = SongRequest(session_id=2, user_id=2, artist='Artist 2', genre='rock', mood='energetic', region='UK', status='pending', priority=2)

    donation1 = Donation(request_id=1, user_id=2, amount=10, timestamp='2021-01-01 20:30:00')
    donation2 = Donation(request_id=2, user_id=1, amount=20, timestamp='2021-01-02 21:30:00')

    # Add the sample data to the session and commit
    db.session.add_all([user1, user2, dj1, dj2, session1, session2, request1, request2, donation1, donation2])
    db.session.commit()

    print('Test database created successfully.')

if __name__ == '__main__':
    create_test_db()
