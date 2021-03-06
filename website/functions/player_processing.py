from . .models import Player, processed_Match, User
from . .import db

mmr_WinChange = 25
mmr_LoseChange = 15

#checking for # in battletag
def battlenet_checker(battle_net_tag):
    if "#" not in battle_net_tag:
        return True

#to swap player ID into Battletag
def get_user_name(p_id):
    p_name = Player.query.filter_by(id=p_id).first()
    return p_name.username

#from user ID to player info
def get_player_info(u_id):
    p_name = User.query.filter_by(id=u_id).first()
    if p_name is not None:
        x = p_name.username
        u_name = Player.query.filter_by(username=x).first()
        return u_name




#to see which players won
def get_winners(winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id):
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

#match logic for
def mmr_logic(host_id, t_Winner, p1_id, p2_id, p3_id, p4_id, p5_id, p6_id):
    #create list of players in match
    p_id = [p1_id, p2_id, p3_id, p4_id, p5_id, p6_id]

    #change list to players MMR's
    i = 0
    mmr = []
    while i < 6:
        mmr.append(get_mmr(p_id[i]))
        i += 1

    #workout totals MMR of each team
    team1 = int(mmr[0]) + int(mmr[1]) + int(mmr[2])
    team2 = int(mmr[3]) + int(mmr[4]) + int(mmr[5])

    #work out averages
    avg_team1 = team1 / 3
    avg_team2 = team2 / 3

    p_mmr_change = []
    #Team 1 winner logic
    if int(t_Winner) == 1:
        i = 0
        while i < 3:
            result = round(avg_team2/int(mmr[i]), 2)
            abc = round(result * mmr_WinChange, 2)
            p_mmr_change.append(abc)
            update_player_Win(p_id[i],abc)
            i += 1
            

        y = 3
        while y < 6:
            result = round((int(mmr[y])/avg_team1),2)
            abc = round(result * mmr_LoseChange, 2)
            p_mmr_change.append(-abc)
            update_player_Loss(p_id[y],abc)
            y += 1
            
    
    #Team 2 winner logic
    else:

        y = 0
        while y < 3:
            result = round((int(mmr[y])/avg_team2), 2)
            abc = round(result * mmr_LoseChange, 2)
            p_mmr_change.append(-abc)
            update_player_Loss(p_id[y],abc)
            y += 1
        i = 3
        while i < 6:
            result = round(avg_team1/int(mmr[i]), 2)
            abc = round(result * mmr_WinChange, 2)
            p_mmr_change.append(abc)
            update_player_Win(p_id[i],abc)
            i += 1

    #adding new processed match to DB
    new_processed_match = processed_Match(host_id = host_id, winner=t_Winner, p1_id = p1_id, 
    p2_id=p2_id, p3_id=p3_id, p4_id=p4_id, p5_id=p5_id, p6_id=p6_id, p1_mmr = mmr[0], p2_mmr = mmr[1],
    p3_mmr = mmr[2], p4_mmr = mmr[3],p5_mmr = mmr[4], p6_mmr = mmr[5], t1_mmr = team1, t2_mmr = team2, 
    p1_change = p_mmr_change[0], p2_change = p_mmr_change[1], p3_change = p_mmr_change[2], 
    p4_change = p_mmr_change[3], p5_change = p_mmr_change[4], p6_change = p_mmr_change[5])
    db.session.add(new_processed_match)
    db.session.commit()
    print("Matched Processed")


#update player when they win
def update_player_Win(p_id, p_mmr):
    update = Player.query.filter_by(id=p_id).first()
    update.wins = update.wins + 1
    update.mmr = update.mmr + p_mmr
    db.session.commit()
    update.mmr = int(update.mmr)
    print("Player processed: " + get_user_name(p_id) + " updated win " + str(p_mmr) + " New MMR: " + str(update.mmr))

#update player when they lose
def update_player_Loss(p_id, p_mmr):
    update = Player.query.filter_by(id=p_id).first()
    update.loss = update.loss + 1
    update.mmr = update.mmr - p_mmr
    db.session.commit()
    update.mmr = int(update.mmr)
    print("Player processed: " + get_user_name(p_id) + " updated loss "+ str(p_mmr) + " New MMR: " + str(update.mmr))