"""
All views are defined in this document
"""
# flask_tracking/users/views.py
from flask import flash, redirect, render_template, request, url_for, abort
from flask.ext.login import login_required, login_user, logout_user

from app import app

from app import db
from .forms import LoginForm, RegistrationForm, IntForm
from .models import User, Nums


@app.route('/')
@app.route('/index/')
def index():
    return "Index Page"

@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Let Flask-Login know that this user
        # has been authenticated and should be
        # associated with the current session.
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template('login.html', form=form)


@app.route('/registration/', methods=('GET', 'POST'))
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        print request.args.get("next")
        return redirect(request.args.get("next") or url_for('index'))
    return render_template('registration.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the
    # session->User connection for this session.
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('index'))


@app.route('/testpage/')
@login_required
def test():
    return "Hi There"

@app.route('/int_decs', methods=('POST', 'GET'))
def ints_decs():

    form = IntForm()
    if form.validate_on_submit():
        num = Nums()
        form.populate_obj(num)
        db.session.add(num)
        db.session.commit()
        return render_template('int_dec.html', form=form)
    return render_template('int_dec.html', form=form)