from flask import Blueprint, render_template
from services.swimrankings import fetch_pb
from models import TrainingSession, User
from flask_login import login_required, current_user

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/profile/<user_name>', methods=['GET'])
@login_required
def profile(user_name):
    pbs = fetch_pb(user_name)
    sessions = TrainingSession.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', pbs=pbs, sessions=sessions, user=current_user)
