from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, length


class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    e_mail = StringField('e-Mail', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), length(min=6)])
    confirmation_password = PasswordField(
        'Password again',
        validators=[DataRequired(), EqualTo('password')]
    )
