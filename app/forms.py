from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PassForm(FlaskForm):
    username = StringField('Username or Website', validators=[DataRequired()])
    secret = PasswordField('Your secret', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    submit = SubmitField('Generate!')