from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email address already exists!")

    username = StringField(label='username', validators=[Length(min=3), DataRequired()])
    email_address = StringField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password1', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')



# validate_username and validate_email_address;
# here username and email_adddress in name, is taken because of username/email_address field. to check the match.


class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='SignIn')














