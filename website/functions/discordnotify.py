import requests #dependency

def discordpost(winner, p1, p2, p3):
    url = "https://discord.com/api/webhooks/877515157713080341/MbMLHDdTOANrFqh2rmUu1MIx6LPIr8UGtqTPtuU2hEufjq6zCpriSTId4A3eotaFY9Zs" #webhook url, from here: https://i.imgur.com/f9XnAew.png

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content1" : "Match Results",
        "username" : "API",
        "avatar_url" : "https://pyrotdleague.com/wp-content/uploads/2020/07/cropped-castle-logo-2.png",
         "content" :  " Team " + winner + " is the winner\nPlayers: " + p1 + " " + p2 + " " + p3
    }


    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))