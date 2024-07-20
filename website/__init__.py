from flask import Flask
from flask_sqlalchemy import SQLAlchemy         # database connection
from os import path 
from flask_login  import LoginManager                   # user authentication

db = SQLAlchemy()                               # define and initialize database
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)                   # name of the file that ran "
    app.config["SECRET_KEY"] = "secret"     # encript or secure the cookies and sesson data related to the website
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'  # connect to SQLite database
    db.init_app(app)                          # initiate the database with the application

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")   
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User, Note 

    #create_database(app)
    with app.app_context():
        db.create_all()

    login_manager  = LoginManager()              # set up user authentication
    login_manager.login_view = 'auth.login'      # redirect users to the login page
    login_manager.init_app(app)                # link login manager to the application

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))       # get user by their ID

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):                # check if the database already exists
        db.create_all(app=app)                              # if it doesn't exist, then create it
        print("Database Created!!!")