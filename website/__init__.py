from threading import Thread
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import subprocess
import time

# Create SQLAlchemy instance
db = SQLAlchemy()

# Set database name
DB_NAME = "database.db"


def create_app():
    """
    Create and configure Flask app.

    Returns:
        Flask app instance.
    """
    # Create Flask app instance
    app = Flask(__name__)

    # Set secret key for app
    app.config["SECRET_KEY"] = "qaplweiucalkjdsfhaloei"

    # Set database uri
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # Initialize SQLAlchemy with app
    db.init_app(app)

    # Create LoginManager instance
    login_manager = LoginManager()

    # Set login view
    login_manager.login_view = "auth.login"

    # Initialize LoginManager with app
    login_manager.init_app(app)

    # Register blueprints
    from .views import views
    from .auth import auth
    from .training import training
    from .admin import admin

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(training, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")

    # Import models
    from .models import Block, BlockOfBlocks, TrainingSession, User

    # Create database if it doesn't exist
    create_database(app)

    # Load user by ID
    @login_manager.user_loader
    def load_user(id):
        """
        Load user by ID.

        Args:
            id (int): User ID.

        Returns:
            User instance.
        """
        return User.query.get(int(id))

    # Restart ssh tunnel every hour
    def restart_tunnel():
        while True:
            subprocess.run(["killall", "ssh"])
            subprocess.Popen(["ssh", "-R", "aqua-metrics:80:localhost:5000", "serveo.net"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            time.sleep(3600)

    # Start tunnel restart loop in background
    app.logger.info("Starting ssh tunnel restart loop")
    Thread(target=restart_tunnel).start()

    return app


def create_database(app):
    """
    Create database if it doesn't exist.

    Args:
        app (Flask app instance): Flask app instance.
    """
    # Check if database file exists
    if not path.exists("website/" + DB_NAME):
        # Create tables in database
        with app.app_context():
            db.create_all()

