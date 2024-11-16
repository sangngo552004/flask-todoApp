from datetime import timedelta
from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#
db = SQLAlchemy()

# Biến môi trường
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_URL = os.environ.get("DATABASE_URL")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tắt tính năng theo dõi thay đổi
    db.init_app(app)

    from .models import Note, User
    with app.app_context():
        db.create_all()

    from .user import user
    from .views import views

    app.register_blueprint(user)
    app.register_blueprint(views)

    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=5)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app
