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
        if sport == "Futebol":
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

        datetimeX = dbQueries.getGameDate(id)[0]
        print(datetimeX)

        perGame['date'] = (str(datetimeX.year) + "/" + str(datetimeX.month) + "/" + str(datetimeX.day))
        perGame['hour'] = (str(datetimeX.hour) + ":" + str(datetimeX.minute))
        perGame['id'] = id
        
        toJson.append(perGame)
        jogo += 1

    return toJson,200

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5002)