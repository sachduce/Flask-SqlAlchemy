from flask import url_for
from flask_testing import TestCase
import src
from src.models import User, Question


class QuestionTestCase(TestCase):

    def create_app(self):
        return src.create_app('test')

    def setUp(self):
        self.db = src.db
        self.db.create_all()
        self.client = self.app.test_client()

        u = User(username='test', email='test@example.com', password='test', category='teacher')

        question = Question(question="Are you test?", option1="Yes", option2="No", option3="May be",
                            option4="Don't know", answer="option1", teacher=u)
        self.db.session.add(u)
        self.db.session.add(question)
        self.db.session.commit()

        self.client.post(url_for('auth.login'),
                         data=dict(username='test', password='test'))

    def tearDown(self):
        src.db.session.remove()
        src.db.drop_all()

    def test_edit_question(self):
        response = self.client.post(
            url_for('questions.edit', question_id=1),
            data=dict(
                question="Are you the great test app?", option1="Yes", option2="No", option3="May be",
                option4="Can't say", answer="option1"
            ),
            follow_redirects=True
        )

        assert response.status_code == 200
        question = Question.query.get(1)
        assert question.question == "Are you the great test app?"

    def test_delete_question(self):
        response = self.client.post(
            url_for('questions.delete', question_id=1),
            follow_redirects=True
        )
        assert response.status_code == 200

