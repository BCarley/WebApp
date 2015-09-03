"""
All views are defined in this document
"""
from flask import render_template
from app import app
from forms import SubmitForm, RegistrationForm

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    """
    Main landing page
    """
    form = SubmitForm()
    return render_template("login.html", form=form)

@app.route('/registration')
def registration():
    """
    Registration page
    """
    form = RegistrationForm()

    if form.validate_on_submit():

