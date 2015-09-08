from flask.ext.wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from wtforms import fields
from wtforms.validators import Email, InputRequired, ValidationError, NumberRange

from .models import User


class LoginForm(Form):
    email = fields.StringField(validators=[InputRequired(), Email()])
    password = fields.StringField(validators=[InputRequired()])

    # WTForms supports "inline" validators
    # which are methods of our `Form` subclass
    # with names in the form `validate_[fieldname]`.
    # This validator will run after all the
    # other validators have passed.
    def validate_password(form, field):
        try:
            user = User.query.filter(User.email == form.email.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")

        # Make the current user available
        # to calling code.
        form.user = user


class RegistrationForm(Form):
    name = fields.TextField("Nickname")
    email = fields.TextField("Email Address", validators=[InputRequired(), Email()])
    password = fields.TextField("Password", validators=[InputRequired()])

    def validate_email(form, field):
        user = User.query.filter(User.email == field.data).first()
        if user is not None:
            raise ValidationError("A user with that email already exists")

class IntForm(Form):
    int_field1 = fields.IntegerField(label="Integer1",
                                     validators=[InputRequired(),
                                                 NumberRange(max=20, message="Why so many?")],
                                     description="Integer field 1",
                                     default=5)

    dec_field1 = fields.DecimalField(label="Decimal1",
                                     validators=[InputRequired(),
                                                 NumberRange(max=1000, message="Why so much?")],
                                     description="Decimal field",
                                     default=5)

