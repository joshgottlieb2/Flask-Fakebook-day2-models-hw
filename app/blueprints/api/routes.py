from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db



@app.route("/new_car", methods=["POST"])
def new_car():
    
    status_input_make = request.form['statusInputMake']
    status_input_model = request.form['statusInputModel']
    status_input_year = request.form['statusInputYear']
    status_input_color = request.form['statusInputColor']
    status_input_price = request.form['statusInputPrice']
    user = 1

    new_car = Car(make=status_input_make, model=status_input_model, year=status_input_year, color=status_input_color, price=status_input_price)

    db.session.add(new_car)
    db.session.commit()

    return redirect("http://127.0.0.1:5000/")
