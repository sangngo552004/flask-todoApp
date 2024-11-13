from flask import Blueprint, render_template, request, flash
from .models import User, Note
from werkzeug.security import generate_password_hash
from . import db
user = Blueprint("user", __name__)

@user.route('/login')
def login():
    return "Login page"

@user.route('/signup', methods=["POST","GET"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        user = User.query.filter_by(email = email).first()
        if user:
            flash("User existed", category="error")
        elif len(password) < 8:
            flash("Password must be have at least 8 characters.", category = "error")
        elif password != confirm_password:
            flash("Password doesn't match!", category="error")
        else:
            password = generate_password_hash(password, method="sha256")
            new_user = User(email, password, username)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("User created!", category="success")
            except Exception as e:
                db.session.rollback()
                flash(f"An error occurred: {e}", category="error")

    return render_template("signup.html")

@user.route('/logout')
def logout():
    return "Logout Page"