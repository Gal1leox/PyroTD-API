import requests #dependency

test_api = "https://discord.com/api/webhooks/950641398959472740/MqJPK2l9y9aJ0ZRMMF_8jZQ9g3T3W3scThB6MsCbM4KKa-IHUvuoEAdxA4XSSJW77bzQ"



def discord_match_Post(winner, p1, p2, p3):
    url = test_api 

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "username" : "Match History",
        "avatar_url" : "https://pyrotdleague.com/wp-content/uploads/2020/07/cropped-castle-logo-2.png",
         "content" :  " **Team " + winner + "** is the winner\n**Players:** " + p1 + ", " + p2 + ", " + p3
    }


    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))



def discord_message_Post(message):
    url = test_api 

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "username" : "Announcement",
        "avatar_url" : "https://pyrotdleague.com/wp-content/uploads/2020/07/cropped-castle-logo-2.png",
         "content" :  message
    }


    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))