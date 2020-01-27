from flask import url_for
from flask_testing import TestCase
import src
from src.models import User


class QuizTestCase(TestCase):

    def create_app(self):
        return src.create_app('test')

    def setUp(self):
        self.db = src.db
        self.db.create_all()
        self.client = self.app.test_client()

        u = User(username='test', email='test@example.com', password='test', category='student')

        self.db.session.add(u)
        self.db.session.commit()

        self.client.post(url_for('auth.login'),
                         data=dict(username='test', password='test'))

    def tearDown(self):
        src.db.session.remove()
        src.db.drop_all()

    def test_take_quiz(self):
        response = self.client.post(
            url_for('tests.take'),
            data=dict(
                answers = ['option1', 'option2']
            ),
            follow_redirects=True
        )

        assert response.status_code == 200





