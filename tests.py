from datetime import datetime, timedelta
import unittest
from hashlib import md5
from app import create_app, db
from app.models import User, Post
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_password_hashing(self):
        u = User(username='testuser')
        u.set_password('testuser')
        self.assertFalse(u.check_password('wrongpass'))
        self.assertTrue(u.check_password('testuser'))

    def test_avatar(self):
        u = User(username='testuser', email='test@example.org')
        email = 'test@example.org'
        digest = md5(email.lower().encode('utf-8')).hexdigest()
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/{}?d=identicon&s=128'.format(digest)))

    def test_follow(self):
        u1 = User(username='testuser1', email='testuser1@exmaple.org')
        u2 = User(username='testuser2', email='testuser2@exmaple.org')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'testuser2')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'testuser1')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u1.followers.count(), 0)

    def test_follow_post(self):
        u1 = User(username='testuser', email='testuser@example.org')
        u2 = User(username='testuser2', email='testuser2@example.org')
        u3 = User(username='testuser3', email='testuser3@example.org')
        u4 = User(username='testuser4', email='testuser4@example.org')
        db.session.add_all([u1, u2, u3, u4])

        now = datetime.utcnow()
        p1 = Post(body="post from testuser1", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from testuser2", author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from testuser3", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from testuser4", author=u4, timestamp=now + timedelta(seconds=2))

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2,p4,p1])
        self.assertEqual(f2, [p2,p3])
        self.assertEqual(f3, [p3,p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)