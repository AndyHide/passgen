from flask import render_template, flash, redirect
from app import app
from app.forms import PassForm
from app.generator import generate_password

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PassForm()
    if form.validate_on_submit():
        password = generate_password(username=form.username.data, secret=form.secret.data, length=form.length.data)
        flash(f"{password}")
        return redirect('/index')
    return render_template('index.html', title='Password Generator', form=form)