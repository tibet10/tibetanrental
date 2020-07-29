from flask import Flask, jsonify, json, request, abort, render_template
from flask_sqlalchemy import SQLAlchemy

from .models import Amenity
from .database import engine, Session, Base

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def index():
    try:
        session = Session()

        Base.metadata.create_all(bind=engine)

        amenities = session.query(Amenity).filter(Amenity.name == "Gym")
        
        return render_template('index.html', result=amenities)

    except Exception as ex:
        print(ex)
        
    return 'result' 
