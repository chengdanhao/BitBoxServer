from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
	name = StringField('What\'s your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')


class RadioForm(FlaskForm):
	status = StringField('ChangeStatus', validators=[DataRequired()])
	submit = SubmitField('Submit')
