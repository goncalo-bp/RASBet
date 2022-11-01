import json

def parse_api_element(data):
        for i in data:
            id = i["id"]
            away_team = i["awayTeam"]
            bookmakers = i["bookmakers"]
            data_inicio = i["commenceTime"]
            completed = i["completed"]
            home_team = i["homeTeam"]
            scores = i["scores"]
            print(id,away_team,completed,home_team,scores, data_inicio)
            odds = {}
            num_odds = 0
            for j in bookmakers:
                #key = j["key"]  # nome da casa de apostas
                #last_update = j["lastUpdate"]
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
                            odds[name] += price
                        else:
                            odds[name] = price        
                    num_odds += 1

            for odd in odds.keys():
                    odds[odd] = odds[odd]/num_odds

            return id,home_team,away_team,completed,scores,data_inicio,odds
