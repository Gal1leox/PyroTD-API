from asyncio.windows_events import NULL
from . .models import Player
from .. import db
#checking for # in battletag

mmr_WinChange = 25
mmr_LoseChange = 15


def battlenet_checker(battle_net_tag):
    if "#" not in battle_net_tag:
        return True

#to swap player ID into Battletag
def get_player_name(p_id):
    p_name = Player.query.filter_by(id=p_id).first()
    return p_name.username



#to see which players won
def get_winners(winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id):
    print(winner)
    if int(winner) == 1:
        return p1_id, p2_id, p3_id
    
    elif int(winner) == 2:
        return p4_id, p5_id, p6_id

    else:
        print("error in player processing unknown input")
        return 0, 0, 0

#find player MMR
def get_mmr(p_id):
    p_name = Player.query.filter_by(id=p_id).first()
    return p_name.mmr


def mmr_logic(t_Winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id):
    #create list of players in match
    p_id = [p1_id, p2_id, p3_id, p4_id, p5_id, p6_id]
    mmr = []
    #change list to MMR's
    for x in range(len(p_id)):
        mmr.append(get_mmr(p_id[x]))

    #workout totals of each team
    team1 = int(mmr[0]) + int(mmr[1]) + int(mmr[2])
    team2 = int(mmr[3]) + int(mmr[4]) + int(mmr[5])

    #work out averages
    avg_team1 = team1 / 3
    avg_team2 = team2 / 3

    #Team 1 winner logic
    if int(t_Winner) == 1:
        i = 0
        while i < 3:
            result = round(avg_team2/int(mmr[i]), 2)
            abc = round(result * mmr_WinChange, 2)
            update_player_Win(p_id[i],abc)
            i += 1
            

        y = 3
        while y < 6:
            result = round((int(mmr[y])/avg_team1), 2)
            abc = round(result * mmr_LoseChange, 2)
            update_player_Loss(p_id[y],abc)
            y += 1
            
    
    #Team 2 winner logic
    else:
        i = 3
        while i < 6:
            result = round(avg_team1/int(mmr[i]), 2)
            abc = round(result * mmr_WinChange, 2)
            update_player_Win(p_id[i],abc)
            i += 1
            

        y = 0
        while y < 3:
            result = round((int(mmr[y])/avg_team2), 2)
            abc = round(result * mmr_LoseChange, 2)
            update_player_Loss(p_id[y],abc)
            y += 1
            


def update_player_Win(p_id, p_mmr):
    update = Player.query.filter_by(id=p_id).first()
    update.wins = update.wins + 1
    update.mmr = update.mmr + p_mmr
    db.session.commit()

    print("Player: " + get_player_name(p_id) + " updated win " + str(p_mmr))

    return "Player updated"

def update_player_Loss(p_id, p_mmr):
    update = Player.query.filter_by(id=p_id).first()
    update.loss = update.loss - 1
    update.mmr = update.mmr - p_mmr
    db.session.commit()

    print("Player: " + get_player_name(p_id) + " updated loss "+ str(p_mmr))

    return "Player updated"