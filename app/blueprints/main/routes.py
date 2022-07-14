from flask import render_template
from . import bp as app
from app.blueprints.main.models import Car

  
@app.route("/")
def home():
    cars = Car.query.all()



    context = {
        "cars": cars,
        "user": "jen" 
    }
    return render_template('index.html', **context)

@app.route("/about")
def about():
    return render_template('about.html')


