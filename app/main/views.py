import os

from flask import render_template
from flask import session

from . import main
from .forms import RadioForm


@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/radio', methods=['GET', 'POST'])
def radio():
	form = RadioForm()
	if form.validate_on_submit():
		for i in form.radios:
			if i[0] == form.choice.data:
				session['choice'] = i[1]

			if form.choice.data == 'off':
				os.system("pkill mplayer &")
			else:
				os.system("pkill mplayer ; mplayer %s &" % form.choice.data)
	return render_template('radio.html', form=form, choice=session.get('choice'))
