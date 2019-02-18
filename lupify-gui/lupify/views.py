from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user

from lupify.forms import LoginForm
from lupify.models import User

from lupify import app, login_manager, db

from uuid import uuid4

@login_manager.user_loader
def load_user(userid):
    return User.get_user(userid)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/host')
@login_required
def host():
    scans = None
    try:
        scans = db.scans.find()
    except Exception as e:
        print("Failed")

    return render_template('host.html', scans=scans)

@app.route('/login', methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username is None:
            flash('Please enter a username', 'danger')
            return render_template("login.html", form=form)
        if password is None:
            flash('Please enter a password', 'danger')
            return render_template("login.html", form=form)

        if User.try_login(username, password):
            user = User(username)
            user.save()
            login_user(user, form.remember.data)

            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash('Something went wrong!', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#######
#######
# Error handlers
# TODO: Fix templates for 404 and server errors
#######
#######
#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404
#
#@app.errorhandler(500)
#def server_error(e):
#    return render_template('500.html'), 500