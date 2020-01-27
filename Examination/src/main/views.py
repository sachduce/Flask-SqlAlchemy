from flask import render_template, abort
from flask_login import current_user
from . import main
from .. import login_manager
from ..models import User, Test

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@main.route('/')
def index():
    return render_template('index.html', user = current_user)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user =user)


@main.app_context_processor
def inject_tags():
    return dict(top5_tests=Test.get_top5_scores(),
                all_tests = Test.get_all_tests())
