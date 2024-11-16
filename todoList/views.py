from flask import Blueprint,render_template,redirect, url_for
from flask_login import current_user, login_required

views = Blueprint("views", __name__)

@views.route('/home')
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


