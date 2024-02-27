from . import db                     # from dot (.) means from current directory (here from init file import db )
from flask_login import UserMixin    #  To handle user authentication in Flask-Login
from sqlalchemy.sql import func


class Note(db.Model):   # Creating a class for the database model of notes
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))     # The main content of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now())   # The date when the note was created
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   # to connect users with their notes 
    # How to associate different information with different user. if we have notes and we want to have notes that are being stored for each user, like each user has multipe notes.
    #we need to setup a relationship between note-object and user-object. and this is done using a foreign key. So a foreign key essentially is a key on one of your database table
    #that references id to another database column. So foreign key is a column in your database that always references a column of another database. so in this instance every single
    # note, we want to store the ID of the user who created the note. 
    # So Its(line 10) saying the type of colöumn is integer and by specifing a foreign key we must pass a valid id of an existing user to this column when we created a note object. This call 
    #one to many rellationship that have one user and many notes(or parent child). In other words, we store a foreign key on each child-objects that referance the parent-object

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(40)) 
    notes = db.relationship("Note")