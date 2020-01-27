from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user
from . import tests
from .. import db
from ..models import Test, Question

from manage import app

@tests.route('/test', methods=['GET', 'POST'])
@login_required
def take():
    if current_user.category != 'student':
        abort(403)
    questions = Question.generate_test_question(10);
    if request.method == 'POST':
        answers = list(request.form.items())
        app.logger.info(str(answers).strip('[]'))
        marks = Test.evaluateTest(answers)
        test = Test(student=current_user, marks=marks)
        db.session.add(test)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('test_form.html', questions=questions)
