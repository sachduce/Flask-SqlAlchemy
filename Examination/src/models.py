from datetime import datetime
from src import db
from sqlalchemy import desc, func, tuple_
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(300), unique=True)
    category = db.Column(db.String(300))
    password_hash = db.Column(db.String)

    @property
    def password(self):
        raise ArithmeticError('password : write-only-field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User %r>' % self.username

class Test(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student = db.relationship('User', backref='tests')
    marks = db.Column(db.Integer, nullable= False)
    date = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def get_top5_scores():
        return Test.query.order_by(desc(Test.marks)).limit(5)

    @staticmethod
    def get_all_tests():
        return Test.query.all()

    @staticmethod
    def evaluateTest(answers):
        return Question.query.filter(tuple_(Question.id, Question.answer).in_(answers)).count()


class Question(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    teacher = db.relationship('User', backref = 'questions')
    question = db.Column(db.String(500), nullable= False)
    option1 = db.Column(db.String(500), nullable= False)
    option2 = db.Column(db.String(500), nullable=False)
    option3 = db.Column(db.String(500), nullable=False)
    option4 = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(10), nullable=False)

    @staticmethod
    def generate_test_question(num):
        return Question.query.order_by(func.random()).limit(num)

