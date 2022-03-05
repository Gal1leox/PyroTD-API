from flask import Blueprint, request, jsonify
from flask_login import current_user
from flask_restful import Api, Resource
from . import db
from . models import get_Match, Player

#Starting MMR
MMR = 1200


apis = Blueprint("apis", __name__)


#player look up
@apis.route('/player', methods=['POST'])
def player():
    data = request.get_json()
    username = data['username']
    player_exists = Player.query.filter_by(username=username).first()

    if player_exists:
        myPlayer = Player.query.filter_by(username=username).first()
        id = myPlayer.id
        mmr = myPlayer.mmr
        wins = myPlayer.wins
        loss = myPlayer.loss
        return jsonify({'username' : username, 'ID' : id, 'MMR' : mmr, 'Wins' : wins,'Loss' : loss, 'age' : 'existing_player'})
    else:
        new_player =Player(username=username, mmr=MMR, wins=0, loss=0)
        db.session.add(new_player)
        db.session.commit()
        myPlayer = Player.query.filter_by(username=username).first()
        id = myPlayer.id
        mmr = myPlayer.mmr
        wins = myPlayer.wins
        loss = myPlayer.loss
        return jsonify({'username' : username, 'ID' : id, 'MMR' : mmr, 'Wins' : wins,'Loss' : loss, 'age' : 'new_player'})
 

#matchload record, uses get_match model to great data
@apis.route('/matches', methods=['POST'])
def matches():
    data = request.get_json()
    host_id = data['host_id']
    winner = data['winner']
    p1_id = data['p1_id']
    p2_id = data['p2_id']
    p3_id = data['p3_id']
    p4_id = data['p4_id']
    p5_id = data['p5_id']
    p6_id = data['p6_id']
    p1_mmr = data['p1_mmr']
    p2_mmr = data['p2_mmr']
    p3_mmr = data['p3_mmr']
    p4_mmr = data['p4_mmr']
    p5_mmr = data['p5_mmr']
    p6_mmr = data['p6_mmr']
    new_match = get_Match(host_id=host_id, winner=winner, p1_id=p1_id, p2_id=p2_id, p3_id=p3_id, p4_id= p4_id, p5_id=p5_id, p6_id=p6_id, 
    p1_mmr=p1_mmr, p2_mmr=p2_mmr, p3_mmr=p3_mmr, p4_mmr=p4_mmr, p5_mmr=p5_mmr, p6_mmr=p6_mmr)
    db.session.add(new_match)
    db.session.commit()
    return jsonify ({'result' : 'Success'})
