from flask import render_template, url_for, redirect
from . import bp as app
from app.blueprints.main.models import Car
from flask_login import login_required, current_user
  
@app.route("/")
def home():

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    cars = Car.query.all()

    context = {
        "cars": cars,
        "user": current_user 
    }
    return render_template('index.html', **context)

@app.route("/about")
def about():
    return render_template('about.html')


