from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class SubmitForm(Form):
	user_name = StringField('user', validators=[DataRequired])

class RegistrationForm(Form):
    name = StringField("Nickname")
    email = StringField(validators=[DataRequired(), Email()])
    password = StringField(validators=[DataRequired()])

    def validate_email(form, field):
        user = User.query.filter(User.email == field.data).first()
        if user is not None:
            raise ValidationError("A user with that email already exists")