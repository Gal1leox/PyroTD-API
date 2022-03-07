import requests #dependency

test_api = "https://discord.com/api/webhooks/950254154562031636/gjnSjfNWlfteibab0q7o4viwSLIZ0ijZFRn4iF6pjvWIJBrLFClzCnL5T8K70SpA-cTo"



def discord_match_Post(winner, p1, p2, p3):
    url = test_api 

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "username" : "Match History",
        "avatar_url" : "https://pyrotdleague.com/wp-content/uploads/2020/07/cropped-castle-logo-2.png",
         "content" :  " Team " + winner + " is the winner\nPlayers: " + p1 + ", " + p2 + ", " + p3
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