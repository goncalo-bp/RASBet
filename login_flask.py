from DBQueries import DBQueries
from flask import Flask, request, redirect, jsonify
from datetime import datetime
from flask_cors import CORS,cross_origin
from passlib.hash import sha256_crypt
import string 
import random

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
    r, usrId, nome = dbQueries.loginUser(email,password)
    vIsAdmin=False
    vIsEspecialista=False

    if r == -1:
        return {"msg": "Wrong email"}, 401

    elif r == 0:
        return {"msg": "Wrong password"}, 401
    
    elif r == 2:
        vIsAdmin = True
        saldo = 0
        
    elif r == 3:
        vIsEspecialista = True
        saldo = 0
  
    else:
        saldo = dbQueries.getBalance(usrId)

    return jsonify(id=usrId,isAdmin=vIsAdmin,isEspecialista=vIsEspecialista,name=nome,wallet=saldo), 200

@app.route('/register', methods = ['POST'])
@cross_origin()
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    nif = request.json.get("nif", None)
    nome = request.json.get("name", None)
   # print(email,password,nif)
    dataNascimento = datetime.strptime(request.json.get("date", None),"%Y-%m-%d")

    try:
        r = dbQueries.registerUser(nome,email,password,nif,dataNascimento, 0, 0)
        vIsAdmin=False
        vIsEspecialista=False

        if r == 0:
            return {"msg": "Email or NIF already existent"}, 401

        return jsonify(success="True"),200
    except:
        return {"msg": "Email or NIF already existent"}, 401
    
@app.route('/transactions', methods = ['POST'])
@cross_origin()
def get_historico_transacoes():
    id = request.json.get("id", None)
    transactionList = dbQueries.getHistoricoTransacoes(id)
    toJson = []
    i = 0

    for transaction in transactionList:
        perTransaction = {}
        datetimeX = transaction[1]
        perTransaction['date'] = (str(datetimeX.year) + "/" + str(datetimeX.month) + "/" + str(datetimeX.day))
        #perTransaction['hour'] = (str(datetimeX.hour) + ":" + str(datetimeX.minute))
        perTransaction['value'] = transaction[3]
        perTransaction['saldoapos'] = transaction[4] + transaction[3]
        k = ""
        if transaction[2] == 'A':
            k = "Aposta colocada"
        elif transaction[2] == 'D':
            k = "Depósito"
        elif transaction[2] == 'L':
            k = "Levantamento"
        elif transaction[2] == 'G':
            k = "Aposta ganha"
        perTransaction['description'] = k

        toJson.append(perTransaction)
        i += 1

    return toJson, 200

@app.route('/saldoCarteira', methods = ['POST'])
@cross_origin()
def get_saldoCarteira():
    id = request.json.get("id", None)

    saldo = dbQueries.getBalance(id)
    toJSON = {}

    toJSON['saldo'] = saldo

    return toJSON, 200

@app.route('/registoaposta', methods = ['POST'])
@cross_origin()
def register_aposta():
    listaJogos = request.json.get("listaJogos", None)
    montante = request.json.get("valor", None)
    id = request.json.get("id", None)

    #criarAposta(id, montante, listaJogos)

    return 200

@app.route('/apostas', methods = ['POST'])
@cross_origin()
def get_betListId():
    id = request.json.get("id", None)
    dict = {}
    dict['simples'] = getBetListId(id,'simples')
    dict['multipla'] = getBetListId(id,'multipla')
    return dict


def getBetListId(id,tipo):
    betList = dbQueries.getHistoricoApostas(id)
    toJson = []

    for bet in betList:
        betId = bet[0]
        perBet = {}
        print(betId)
        #RETURN (listaJogo) -> (<MontanteApostado>,<total ganho>,[([(Estoril,jogaEmCasa)],<Quem ganhou>)])
        listaJogo = dbQueries.listaJogosPorAposta(betId)
        if (tipo == 'simples' and len(listaJogo[2]) > 1) or (tipo == 'multipla' and len(listaJogo[2]) < 2):
            continue
 
        perBet['jogo'] = []
        for jogo in listaJogo[2]:
            equipasNoJogo = ""
            print(jogo)
            for equipa in jogo:
                #print('EQUIPA:' + equipa + " " + str(len(jogo[0])))
                if len(jogo) == 3:
                    
                    if equipa[0] == 'Draw':
                        continue

                    if equipa[1] == 1:
                        equipasNoJogo = equipa[0] + " x " + equipasNoJogo
                    else:
                        equipasNoJogo = equipasNoJogo + equipa[0]
            
            resultado = jogo[1][0]
            perBet['jogo'].append((equipasNoJogo, resultado))
        
        
        perBet['montante'] = listaJogo[0]
        perBet['ganho'] = listaJogo[1]
            

        print(toJson)
        print(perBet)

        toJson.append(perBet)   

    return toJson, 200

@app.route('/sports/<sport>', methods = ['GET'])
@cross_origin()
def get_gamess(sport):
    toJson = []
    jogo = 0
    idList = dbQueries.getBySport(sport,0)
    for id in idList:
        perGame = {}
        game = dbQueries.getGameInfo(id)
        i=0
        perGame['equipas'] = []

        perGame['nome'] = ""
        ordenado = {}

        for team in game:
            equipa = {}
            equipa['name'] = team[0]
            equipa['odd'] = team[1]
            if len(game) == 3:
                if team[0] == 'Draw':
                    ordenado['team1'] = equipa
                elif team[2] == 1:
                    perGame['nome'] = team[0] + " x " + perGame['nome']
                    ordenado['team0'] = equipa
                else:
                    perGame['nome'] += team[0]
                    ordenado['team2'] = equipa
            else:
                perGame['equipas'].append(equipa)
                i = i+1

        if len(game) == 3:
            for i in range(3):
                perGame['equipas'].append(ordenado[f'team{i}'])

        elif len(game) == 2: # BASQUETEBOL E TENIS
            perGame['nome'] = game[0][0] + " x " + game[1][0]

        else: # MOTOGP
            perGame['nome'] = "Grand Prix"


        datetimeX = dbQueries.getGameDate(id)[0]

        perGame['date'] = (str(datetimeX.year) + "/" + str(datetimeX.month) + "/" + str(datetimeX.day))

        if int(datetimeX.hour) < 10 and int(datetimeX.minute) < 10:
            perGame['hour'] = ("0" + str(datetimeX.hour) + ":0" + str(datetimeX.minute))
        
        elif int(datetimeX.hour) < 10:
            perGame['hour'] = ("0" + str(datetimeX.hour) + ":" + str(datetimeX.minute))
        
        elif int(datetimeX.minute) < 10:
            perGame['hour'] = (str(datetimeX.hour) + ":0" + str(datetimeX.minute))

        else:
            perGame['hour'] = (str(datetimeX.hour) + ":" + str(datetimeX.minute))
        
        perGame['id'] = id
        
        toJson.append(perGame)
        jogo += 1

    return toJson,200

@app.route('/mudarcampo', methods = ['POST'])
@cross_origin()
def mudar_campo():
    changePassword = True
    changeName = True
    id = request.json.get("id", None)

    password = request.json.get("password", None)
    if password == None:
        changePassword = False
    
    name = request.json.get("name", None)
    if name == None:
        changeName = False

    if changePassword:
        dbQueries.updateUserField(0, sha256_crypt.hash(password,salt="RAS2022"), id)

    if changeName:
        dbQueries.updateUserField(1, name, id)

    return [200]

@app.route('/transacao', methods = ['POST'])
@cross_origin()
def get_desportos():    
    id = request.json.get("id", None)
    value = request.json.get("value", None)
    type = request.json.get("type",None)

    dbQueries.registerTransaction(id,value,type)

    return [200]

@app.route('/apostas/registo/<tipo>', methods = ['POST'])
@cross_origin()
def get_betList(tipo):
    id = request.json.get("id", None)
    listaBets = request.json.get("boletim", None)
    montante = request.json.get("montante",None)

    if tipo == 'simples':
        for bet in listaBets:
            dbQueries.criarAposta(id,montante,[(bet,listaBets[bet])])
    else:
        bets = []
        for bet in listaBets:
            bets += [(bet,listaBets[bet])]

        dbQueries.criarAposta(id,montante,bets)

    return [200]

@app.route('/sports/<sport>/addJogo', methods = ['POST'])
@cross_origin()
def add_Jogo(sport):
    
    id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 35)) 
    nomeEquipa1 = request.json.get("nomeEquipa1", None)
    nomeEquipa2 = request.json.get("nomeEquipa2", None)
    data = request.json.get("data", None)
    hora = request.json.get("hora", None)
    datetimeV = data + hora

    print(datetimeV)

    dbQueries.addJogo(id, sport, datetimeV, 0)
    dbQueries.addTeam(nomeEquipa1, id, 0, 1)
    dbQueries.addTeam("Draw", id, 0, 0)
    dbQueries.addTeam(nomeEquipa2, id, 0, 0)
    return [200]

@app.route('/promocoes', methods = ['GET'])
@cross_origin()
def get_promotionstodas():
    promotions = []
    promotionsRow = dbQueries.getPromotions()

    for row in promotionsRow:
        dictP = {}
        dictP['idProm'] = row[0]
        dictP['idJogo'] = row[1]
        teams = dbQueries.getTeamsGame(row[1])
        nome = ""
        for team in teams:
            if team[3] == 1:
                nome = team[1] + " vs " + nome
            elif team[1] != 'Draw':
                nome = nome + team[1]

        dictP['nome'] = nome
        dictP['aumento'] = row[2]
        promotions.append(dictP)
    
    return promotions, 200


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5002)