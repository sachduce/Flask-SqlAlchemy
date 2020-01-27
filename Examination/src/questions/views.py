from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user
from . import questions
from .forms import QuestionForm
from .. import db
from ..models import Question


@questions.route('/addQuestion', methods=['GET', 'POST'])
@login_required
def add():
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.question.data
        option1 = form.option1.data
        option2 = form.option2.data
        option3 = form.option3.data
        option4 = form.option4.data
        answer = form.answer.data
        newQuestion = Question(teacher=current_user, question=question, option1=option1, option2=option2,
                               option3=option3,
                               option4=option4, answer=answer)
        db.session.add(newQuestion)
        db.session.commit()
        flash("New Question created by '{}'".format(newQuestion.teacher.username))
        return redirect(url_for('main.user', username=current_user.username))
    return render_template('question_form.html', form=form, title="Add Question")


@questions.route('/editQuestion/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit(question_id):
    question = Question.query.get_or_404(question_id)
    if current_user != question.teacher:
        abort(403)
    form = QuestionForm(obj=question)
    if form.validate_on_submit():
        form.populate_obj(question)
        db.session.commit()
        flash("Edited Question by '{}'".format(question.teacher.username))
        return redirect(url_for('main.user', username=current_user.username))
    return render_template('question_form.html', form=form, title="Edit question")


@questions.route('/delete/<int:question_id>', methods=['GET', 'POST'])
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if current_user != question.teacher:
        abort(403)
    if request.method == "POST":
        db.session.delete(question)
        db.session.commit()
        flash("Deleted question by'{}'".format(question.teacher.username))
        return redirect(url_for('main.user', username=current_user.username))
    else:
        flash("Please confirm deleting the bookmark.")
    return render_template('confirm_delete.html')
