
from flask import Flask, Blueprint
from .post.views import post_bp

app = Flask(__name__) 

app.register_blueprint(post_bp)
