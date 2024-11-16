from flask import Blueprint,render_template,redirect, url_for,request,flash
from flask_login import current_user, login_required
from .models import Note
from . import db

views = Blueprint("views", __name__)

@views.route('/home', methods=["POST","GET"])
@views.route('/', methods=["POST","GET"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1 :
            flash("Note is empty!!!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!!", category="success")
    return render_template("home.html", user=current_user)


