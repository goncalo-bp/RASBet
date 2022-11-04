import requests
import time
from DBQueries import DBQueries
import Parser as ps
from datetime import datetime

def parse_header(header):
    date = header["Date"]
    _,charset = header["Content-Type"].split(';')
    _,ch = charset.split('=')
    length = header["Content-Length"]
    return date,ch,length

dbq = DBQueries()

def atualiza():
    while True: #Infinite loop
        #Execute the function
        headers = { 'accept': 'application/json',}
        api_url = "http://ucras.di.uminho.pt/v1/games/"
        response = requests.get(api_url, headers=headers)
        data = response.json()
        for i in data:
            #id,home_team,away_team,completed,scores,data_inicio,odds,most_recent
            jogo = ps.parse_api_element(i)
            equipasPresentes = [(jogo[1],float(jogo[6][jogo[1]]),1),(jogo[2],float(jogo[6][jogo[2]]),0),('Draw',float(jogo[6]['Draw']),0)]
            if dbq.existingGame(jogo[0]):
                lastUpdate = dbq.getLastUpdate(jogo[0]) 
                
                if lastUpdate != jogo[7]:
                    for equipa in equipasPresentes:
                        dbq.updateOdds(jogo[0],equipa[0],equipa[1])
                
                if int(dbq.getGameState(jogo[0])[0]) != int(jogo[3]):
                    
                    dbq.setGameState(1,jogo[0])

                    resultado = jogo[4].split('x')
                    ganhador = ""
                    if resultado[0] > resultado[1]:
                        ganhador = jogo[1]
                    elif resultado[1] > resultado[0]:
                        ganhador = jogo[2]
                    else:
                        ganhador = 'Draw'
                    dbq.setWinner(ganhador)
                    dbq.atualizaResultadoApostas(jogo[0],ganhador)
            else:
                dbq.criarJogo(jogo[0],'Futebol',datetime.strptime(jogo[5], "%Y-%m-%dT%H:%M:%S.%fZ"),equipasPresentes)

        date,ch,length = parse_header(response.headers)
        time.sleep(600) #Wait 600s (10 min) before re-entering the cycle

atualiza()
# equipasPresentes = [(nomeEquipa,odd,jogaEmCasa)]
#def criarJogo(self, idJogo, nomeDesporto, dataJogo, equipasPresentes):
#        self.mydb.execute(DBConstants.create_game, (idJogo, nomeDesporto, dataJogo))
#        for (nomeEquipa,odd,jogaEmCasa) in equipasPresentes:
#            self.mydb.execute(DBConstants.add_team, (nomeEquipa,idJogo,odd,jogaEmCasa))
#        self.mydb.commit()

#id,home_team,away_team,completed,scores,data_inicio,odds

#('538136a794711c8c9bc24b48353c396c', 'Gil Vicente', 'Portimonense', False, None, '2022-11-04T20:15:00.000Z', {'Gil Vicente': 2.2046666666666668, 'Portimonense': 3.336, 'Draw': 3.426666666666667})
#('be09fd32746c6c2f11a64157039dc992', 'Vizela', 'Arouca', False, None, '2022-11-05T15:30:00.000Z', {'Arouca': 4.248, 'Vizela': 1.9606666666666668, 'Draw': 3.329333333333333})
#('c8d53fadc30913fa823bea3999311b81', 'FC Porto', 'Pacos de Ferreira', False, None, '2022-11-05T18:00:00.000Z', {'FC Porto': 1.1213333333333333, 'Pacos de Ferreira': 78.87400000000001, 'Draw': 8.952})
#('6ae5f22198593f180590bf8161bbf910', 'Sporting Lisbon', 'Vitória SC', False, None, '2022-11-05T20:30:00.000Z', {'Sporting Lisbon': 1.3364285714285715, 'Vitória SC': 9.774999999999997, 'Draw': 5.239285714285714})
#('72cdea24cebb5465e577b8fe3f3cdfeb', 'Rio Ave FC', 'Boavista Porto', False, None, '2022-11-06T15:30:00.000Z', {'Boavista Porto': 3.0976923076923075, 'Rio Ave FC': 2.4223076923076925, 'Draw': 3.160769230769231})
#('c7ede9e77ceb9af1e3d037b8dcd44116', 'Braga', 'Casa Pia', False, None, '2022-11-06T18:00:00.000Z', {'Braga': 1.412307692307692, 'Casa Pia': 73.22461538461538, 'Draw': 77.07153846153845})
#('7ad4bb5d9ab1e9c67014a87403edf80a', 'CS Maritimo', 'Famalicão', False, None, '2022-11-06T18:00:00.000Z', {'CS Maritimo': 2.759230769230769, 'Famalicão': 2.6384615384615384, 'Draw': 3.044615384615385})
#('0db34ba8228c8124f7d026b0ce1724d2', 'Estoril', 'Benfica', False, None, '2022-11-06T20:30:00.000Z', {'Benfica': 1.3000000000000003, 'Estoril': 74.80923076923077, 'Draw': 78.00461538461538})
#('5a673392e3835c2b073ccd468d652593', 'Chaves', 'Santa Clara', False, None, '2022-11-07T20:15:00.000Z', {'Chaves': 2.3623076923076924, 'Santa Clara': 3.2600000000000002, 'Draw': 3.098461538461538})