from flask import Blueprint

views = Blueprint("views", __name__)

@views.route('/home')
def home():
    return "Home page"

