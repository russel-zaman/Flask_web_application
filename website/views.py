from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)        # This(view) file is a blueprint of our application which means  
                                            # it has bunch of roots, url defined in it. It just a way to  organize or saperate our app so we dont have to have all of our views defined in one file. we can have them defined in multiple file split up and nicely organize. 
@views.route("/", methods=["GET", "POST"])           # with a decorater, defining root(slash '/') of the website
@login_required
def home():                 # we define home page as our root, so it will show whatever in home page
    if request.method == "POST":  # If the method used to access
        note = request.form.get("note")     # get data from HTML form by name="note"

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)       # Add this new note into database session
            db.session.commit()             # Save all changes made in this session
            flash("New note has been added.",  category="success")
    return render_template("home.html", user=current_user)


@views.route("/delet-note", methods=["POST"])      # /delete-note is the URL for deleting notes and using POST method
def delete_note():
    note = json.loads(request.data)         # Get id of the note that needs to be deleted
    noteId = note["noteId"]
    note = Note.query.get(noteId)          # Find the note with given Id
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})