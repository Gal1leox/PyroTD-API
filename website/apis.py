from flask import Blueprint, request, jsonify, flash
from flask_login import current_user
from flask_restful import Api, Resource
from . import db
from . models import get_Match, Player
from . functions.discordnotify import discord_match_Post
from . functions.player_processing import get_player_name, get_winners, mmr_logic, get_mmr
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
        print('Sucess: Player looked up')
        return jsonify({'username' : username, 'ID' : id, 'MMR' : int(mmr), 'Wins' : wins,'Loss' : loss, 'age' : 'existing_player'})
    else:
        new_player = Player(username=username, mmr=MMR, wins=0, loss=0)
        db.session.add(new_player)
        db.session.commit()
        myPlayer = Player.query.filter_by(username=username).first()
        id = myPlayer.id
        mmr = myPlayer.mmr
        wins = myPlayer.wins
        loss = myPlayer.loss
        print('Sucess: New user created')
        return jsonify({'username' : username, 'ID' : id, 'MMR' : int(mmr), 'Wins' : wins,'Loss' : loss, 'age' : 'new_player'})
 

#matchload record, uses get_match model to get data
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
    p1_ban = data['p1_ban']
    p2_ban = data['p2_ban']
    p3_ban = data['p3_ban']
    p4_ban = data['p4_ban']
    p5_ban = data['p5_ban']
    p6_ban = data['p6_ban']
    new_match = get_Match(host_id=host_id, winner=winner, p1_id=p1_id, p2_id=p2_id, p3_id=p3_id, p4_id= p4_id, p5_id=p5_id, p6_id=p6_id, 
    p1_ban=p1_ban, p2_ban=p2_ban, p3_ban=p3_ban, p4_ban=p4_ban, p5_ban=p5_ban, p6_ban=p6_ban)

    winner_player = get_winners(winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id)

    if int(winner_player[0]) == 0:
        print ("error importing match")
        return jsonify ({'result' : 'Error', 'match status' : 'failed to Import'})

    else:
    #playername logic to go here
        p_Name1 = get_player_name(winner_player[0])
        p_Name2 = get_player_name(winner_player[1])
        p_Name3 = get_player_name(winner_player[2])
        discord_match_Post(winner, p_Name1, p_Name2, p_Name3)
        db.session.add(new_match)
        db.session.commit()
        print("Match imported")
        return jsonify ({'result' : 'Success', 'match status' : 'imported'})

@apis.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    # p1_id = data['username']
    # a = get_mmr(p1_id)
    # print(a)
    host_id = data['host_id']
    t_winner = data['t_winner']
    p1_id = data['p1_id']
    p2_id = data['p2_id']
    p3_id = data['p3_id']
    p4_id = data['p4_id']
    p5_id = data['p5_id']
    p6_id = data['p6_id']

    mmr_logic(host_id, t_winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id)
    return jsonify ({'result' : 'Success', 'player status' : 'updated'})