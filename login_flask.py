from DBQueries import DBQueries
from flask import Flask, request, redirect, jsonify
from datetime import datetime
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False
dbQueries = DBQueries()

@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    r, usrId = dbQueries.loginUser(email,password)
    vIsAdmin=False
    vIsEspecialista=False
    
    if r == -1:
        return {"msg": "Wrong email"}, 401

    elif r == 0:
        return {"msg": "Wrong password"}, 401
    
    elif r == 2:
        vIsAdmin = True

    elif r == 3:
        vIsEspecialista = True
  
    return jsonify(id=usrId,isAdmin=vIsAdmin,isEspecialista=vIsEspecialista), 200

@app.route('/register', methods = ['POST'])
@cross_origin()
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    nif = request.json.get("nif", None)
   # print(email,password,nif)
    dataNascimento = datetime.strptime(request.json.get("date", None),"%Y-%m-%d")

    try:
        r = dbQueries.registerUser("a",email,password,nif,dataNascimento, 0, 0)
        vIsAdmin=False
        vIsEspecialista=False

        if r == 0:
            return {"msg": "Email or NIF already existent"}, 401

        return jsonify(success="True"),200
    except:
        return {"msg": "Email or NIF already existent"}, 401

@app.route('/games', methods = ['POST'])
@cross_origin()
def get_games():
    sport = request.json.get("sport", None)
    suspenso = request.json.get("suspenso", None)
    toJson = {}
    jogo = 0
    idList = dbQueries.getBySport(sport,suspenso)
    for id in idList:
        perGame = {}
        game = dbQueries.getGameInfo(id)
        i=0
        for team in game:
            equipa = {}
            equipa['name'] = team[0]
            equipa['odd'] = team[1]
            if len(game) == 3:
                if team[0] == 'Draw':
                    perGame[f'equipa1'] = equipa
                elif team[2] == 1:
                    perGame[f'equipa0'] = equipa
                else:
                    perGame[f'equipa2'] = equipa
            
            else:
                perGame[f'equipa{i}'] = equipa
                i = i+1
        
        datetimeX = dbQueries.getGameDate(id)[0]
        print(datetimeX)

        perGame['date'] = (str(datetimeX.year) + "/" + str(datetimeX.month) + "/" + str(datetimeX.day))
        perGame['hour'] = (str(datetimeX.hour) + ":" + str(datetimeX.minute))
        
        
        toJson[f'jogo{jogo}'] = perGame
        jogo += 1

    return toJson,200
    
if __name__ == '__main__':
   app.run()