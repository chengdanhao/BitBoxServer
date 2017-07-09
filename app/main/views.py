from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from . import main
from .forms import NameForm, RadioForm


@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html', form=form, name=session.get('name'))


@main.route('/radio', methods=['GET', 'POST'])
def radio():
	form = RadioForm()
	if form.validate_on_submit():
		session['radio_status'] = form.status.data
		form.status.data = ''
		return redirect(url_for('.radio'))
	return render_template('radio.html', form=form, radio_status=session.get('radio_status'))
