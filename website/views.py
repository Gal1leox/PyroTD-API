from flask import Blueprint, render_template, jsonify, session
from flask_login import login_required, current_user
from .models import Player 
from .functions.player_processing import get_user_name, get_player_info
from sqlalchemy import desc


views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home ():
    if current_user.is_authenticated:
        player = get_player_info(current_user.id)
        return render_template('home.html', user=current_user, player=player)
    else:
        return render_template('home.html', user=current_user)

@views.route('/matches')
@login_required
def matches ():
    player = get_player_info(current_user.id)
    return render_template('matches.html', user=current_user, player=player)

@views.route('/profile')
@login_required
def player():
    #username_exists = Player.query.filter_by(username=username).first()
    player = get_player_info(current_user.id)
    return render_template('profile.html',user=current_user, player=player)

@views.route('/leaderboard')
def leaderboard():
    leaderboard_current = Player.query.order_by(desc(Player.mmr))
    if current_user.is_authenticated:
        player = get_player_info(current_user.id)
        return render_template('leaderboard.html',user=current_user, player=player, leaderboard=leaderboard_current)
    else:
        return render_template('leaderboard.html',user=current_user, leaderboard=leaderboard_current)