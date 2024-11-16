import json
from flask import Blueprint, jsonify,render_template,redirect, url_for,request,flash
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

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    print(note)
    note_id = note["note_id"]
    result = Note.query.get(note_id)
    if result:
        if result.user_id == current_user.id:
            db.session.delete(result)
            db.session.commit()
            flash("Delete note successfully!!!", category="success")
    return jsonify({"code": 200})