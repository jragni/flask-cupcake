"""Flask app for Cupcakes"""

from typing import Sized
from flask import Flask, request, jsonify
from flask.templating import render_template_string
from models import db, connect_db, Cupcake
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

@app.route('/')
def root():
    pass

@app.route('/api/cupcakes')  
def list_all_cupcakes():
    """ Returns json of cupcakes in database 
    {cupcakes:[ id, flavor, size, rating, image}...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized) 


@app.route('/api/cupcakes/<int:cupcake_id>')
def list_single_cupcake(cupcake_id):
    """Return JSON {'cupcake': {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake from form data & return it.
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}"""

    flavor = request.json["flavor"]
    size = request.json["size"] 
    rating = request.json["rating"] 
    image = request.json["image"] 

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)
        
