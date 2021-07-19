"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify
import requests
from models import db, connect_db, Cupcake
from sqlalchemy import 

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

@app.route('/api/cupcakes')  #NOTE: api or no api?
def list_all_cupcakes():
	""" Returns json of cupcakes in database 
		{cupcakes:[ id, flavor, size, rating, image}...]}"""

	# query list of cupcakes from the db
	cupcakes = Cupcake.query.all()
	# serialize the data from the db and return
	serialized = [cupcake.serialize() for cupcake in cupcakes]

	return jsonify(cupcakes=serialized) 


	
