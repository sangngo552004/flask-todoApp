from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, current_user, login_required
user = Blueprint("user", __name__)

@user.route('/login', methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session.permanent = True
                session['user'] = user.username
                login_user(user, remember=True)
                session.permanent = True
                flash("LogIn successfully !!!!", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Wrong password !!!", category="error")
        else:
            flash("User doesn't exist!!", category="error")
    return render_template("login.html", user=current_user)

@user.route('/signup', methods=["POST","GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
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
                session.permanent = True
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            except Exception as e:
                db.session.rollback()
                flash(f"An error occurred: {e}", category="error")

    return render_template("signup.html", user=current_user)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))