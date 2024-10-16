from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from models import db, User
from routes.auth import auth
from routes.training_sessions import training_sessions
from routes.user_profile import user_profile
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints for routes
app.register_blueprint(auth)
app.register_blueprint(training_sessions)
app.register_blueprint(user_profile)

if __name__ == '__main__':
    app.run(debug=True)
