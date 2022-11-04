import json
from datetime import datetime

def parse_api_element(data):
    id = data["id"]
    away_team = data["awayTeam"]
    bookmakers = data["bookmakers"]
    data_inicio = data["commenceTime"]
    completed = data["completed"]
    home_team = data["homeTeam"]
    scores = data["scores"]
    odds = {}
    num_odds = 0
    last_update = []
    for j in bookmakers:
        #key = j["key"]  # nome da casa de apostas
        last_update.append(datetime.strptime(j["lastUpdate"], "%Y-%m-%dT%H:%M:%S%fZ"))
        markets = j["markets"]
        #print("-" + key)
        #print("-" + last_update)
        for m in markets:
            #key_odd = m["key"]   ##########   IMPORTANTE -> h2h
            outcomes = m["outcomes"]
            #print("--"+key_odd)
            for o in outcomes:
                name = o["name"]
                price = o["price"]
                if name in odds.keys():
                    odds[name] = odds[name] + price
                else:
                    odds[name] = price          
            num_odds += 1
    most_recent = max(last_update)
    for odd in odds.keys():
            odds[odd] = round(odds[odd]/num_odds,2)

    return id,home_team,away_team,completed,scores,data_inicio,odds,most_recent,scores
