from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .models import Amenity
from ..database import session_scope

from . import post_bp

@post_bp.route('/post/one', methods=['GET'])
def one():
    try:
        with session_scope() as session:
            amenities = session.query(Amenity).filter(Amenity.name == "Laundry")
        
            return render_template('index.html', result=amenities)

    except Exception as ex:
        print(ex)
        
    return 'result' 

@post_bp.route('/post/two', methods=['GET'])
def two():
    try:
        with session_scope() as session:
            amenities = session.query(Amenity).filter(Amenity.name == "Gym")
        
            return render_template('index.html', result=amenities)

    except Exception as ex:
        print(ex)
        
    return 'result' 