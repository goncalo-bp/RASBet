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
            
            jogo = ps.parse_api_element(i)
            equipasPresentes = [(jogo[1],float(jogo[6][jogo[1]]),1),(jogo[2],float(jogo[6][jogo[2]]),0),('Draw',float(jogo[6]['Draw']),0)]
            
            if dbq.existingGame(jogo[0]):
            
                lastUpdate = dbq.getLastUpdate(jogo[0]) 
                
                if lastUpdate != datetime.strptime(jogo[7], "%Y-%m-%dT%H:%M:%S.%fZ"):

                    for equipa in equipasPresentes:
                        dbq.updateOdds(jogo[0],equipa[0],equipa[1])
                    
                    print(f'Atualizei odds para o jogo {jogo[1]} vs {jogo[2]}')
                
                if dbq.getGameState(jogo[0]) != jogo[3]:
                    
                    dbq.setGameState(1,jogo[0])

                    resultado = jogo[7].split('x')
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