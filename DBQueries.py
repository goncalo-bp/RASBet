import mysql.connector # pip install mysql-connector-python
from DBConstants import DBConstants
from Database import Database
from passlib.hash import sha256_crypt
import numpy as np

class DBQueries:

    def __init__(self):
        self.mydb = Database()

    def __exit__(self):
        self.mydb.close()

    def alreadyExists(self, email):
        lines = self.mydb.query(DBConstants.get_log_info,(email,))
        return len(lines) > 0

    def registerUser(self, nome, email, password, nif, date, isAdmin, isEspecialista):
        r = 1
        alreadyExists = self.alreadyExists(email)

        if not alreadyExists:
            self.mydb.execute(DBConstants.add_wallet)
            self.mydb.execute(DBConstants.register_user,(nome, email, sha256_crypt.hash(password,salt="caldasgay"), self.mydb.lastrowid(), date, nif, isAdmin, isEspecialista))     
            self.mydb.commit()
        else:
            r = 0 
        return r
    
    def registerSpecialUser(self, nome, email, password, isAdmin, isEspecialista):
        r = 1
        alreadyExists = self.alreadyExists(email)
        if not alreadyExists:
            self.mydb.execute(DBConstants.register_user,(nome, email, sha256_crypt.hash(password,salt="caldasgay"), None, None, None, isAdmin, isEspecialista))
            self.mydb.commit()
        else:
            r = 0
        return r
    
    def removeSpecialUser(self, id):
        prom = self.mydb.query(DBConstants.get_user, (id,))
        if len(prom) == 0:
            #Não existe
            pass
        else:
            self.mydb.execute(DBConstants.remove_special_user,(id,))
            self.mydb.commit()

    def getSpecialUser(self):
        return self.mydb.query(DBConstants.get_special_users)


    def loginUser(self, email, password):
        data = self.mydb.query(DBConstants.get_log_info, (email,))
        r = 1
        usrId = True
        print(data[0][1])
        if len(data) == 0:
            r = -1
            usrId = False
        elif not sha256_crypt.verify(password,data[0][1]):
            r = 0 
            usrId = False
        elif data[0][3]:
            r = 2
        elif data[0][4]:
            r = 3
        if usrId:
            usrId = data[0][2]
        return r, usrId

    def addTeam(self, name, gameId, odd, home):
        self.mydb.execute(DBConstants.add_team, (name, gameId, odd, home))
        self.mydb.commit()

    def getSports(self):
        data = self.mydb.query(DBConstants.get_sports)
        l = []
        for elem in data:
            l.append(elem[0])
        return l

    def getBySport(self, sport):
        data = self.mydb.query(DBConstants.get_by_sport, (sport,))
        l = []
        for gameId in data:
            l.append(gameId[0])
        return l

    def getGameInfo(self, gameId):
        data = self.mydb.query(DBConstants.get_game_info, (gameId,))
        l = []
        for elem in data[0]:
            l.append(elem[0])        
        return l

    def getBalance(self, usrId):
        return self.mydb.query(DBConstants.get_balance, (usrId,))[0][0]

    # TODO Definir o erro
    def addPromotion(self, gameId, value):
        try:
            self.mydb.execute(DBConstants.create_promotion,(gameId, 1+value,))
            self.mydb.execute(DBConstants.boosted_odds,(1+value, gameId,))
            self.mydb.commit()
        except Exception:
            #erro
            pass
    
    # TODO Definir o erro
    def removePromotion(self, idProm):
        prom = self.mydb.query(DBConstants.get_promotion, (idProm,))
        if len(prom) == 0:
            #Não existe
            pass
        else:
            self.mydb.execute(DBConstants.boosted_odds,(1/float(prom[0][1]), prom[0][2],))
            self.mydb.execute(DBConstants.remove_promotion,(idProm,))
            self.mydb.commit()

    def getPromotions(self):
        return self.mydb.query(DBConstants.get_promotions)

        # Históricos
    def getHistoricoApostas(self, idUser):
        return self.mydb.query(DBConstants.get_history_bets, (idUser,))
        
    def getHistoricoTransacoes(self, idUser):
        return self.mydb.query(DBConstants.get_history_trans, (idUser,))

    def registerTransaction(self, idUser, valor, descricao):
        bal = float(self.getBalance(idUser))
        if valor < 0 and valor*(-1) > bal:
            return -1
        else:
            idW = self.mydb.query(DBConstants.get_wallet, (idUser,))[0][0]
            self.mydb.execute(DBConstants.reg_transaction,((bal,valor,idUser,descricao)))
            self.mydb.execute(DBConstants.update_wallet,(bal+valor,idW))
            self.mydb.commit()
            return 0

      #Jogos Apostados = [(idJogo, resultadoApostado)]
    def criarAposta(self, idUser, valor, jogosApostados):
        wallet = self.mydb.query(DBConstants.get_wallet, (idUser,))
        if len(wallet) == 0 or self.registerTransaction(idUser,(-1)*valor,'A') == -1:
            return -1 #SEM CARTEIRA, É ADMIN OU ESPECIALISTA OU NÃO TEM DINHEIRO

        #Jogo Ainda não começou
        idJogosApostados = [x for x in jogosApostados[0]]
        datas = []
        #for id in jogosApostados:
        #    datas.append(self.mydb.query(DBConstants.get_game_date, (id[0],)))

        #if datetime.now() > min(datas):
        #    return -2 #UM OU MAIS JOGOS JÁ COMEÇARAM

        self.mydb.execute(DBConstants.reg_aposta, (idUser,valor))
        numAposta = self.mydb.lastrowid()
        for (idJogo, resultadoApostado) in jogosApostados:
            odd = self.mydb.query(DBConstants.get_odd_by_game,(idJogo, resultadoApostado))
            self.mydb.execute(DBConstants.add_game_to_bet, (numAposta,idJogo,odd[0][0],resultadoApostado))
        self.mydb.commit()
        
    def criarJogo(self, idJogo, nomeDesporto, dataJogo, equipasPresentes):
        self.mydb.execute(DBConstants.create_game, (idJogo, nomeDesporto, dataJogo))
        for (nomeEquipa,odd,jogaEmCasa) in equipasPresentes:
            self.mydb.execute(DBConstants.add_team, (nomeEquipa,idJogo,odd,jogaEmCasa))
        self.mydb.commit()
    
    def datasDisponiveis(self):
        return self.mydb.execute(DBConstants.get_games_calendar, ())

    def jogoPorData(self, data):
        return self.mydb.execute(DBConstants.get_game_by_day, (data,))
    
    def existingGame(self, idJogo):
        listaJogos = self.mydb.query(DBConstants.get_game_by_ID,(idJogo,))
        return len(listaJogos) == 1

    def getLastUpdate(self, idJogo):
        return self.mydb.query(DBConstants.get_last_update,(idJogo,))[0]

    def setGameState(self, started, idJogo):
        self.mydb.execute(DBConstants.set_game_state,(started, idJogo,))
        self.mydb.commit()

    def getGameState(self, idJogo):
        return self.mydb.query(DBConstants.get_game_state,(idJogo,))[0]

    def setWinner(self, idJogo, winner):
        self.mydb.execute(DBConstants.set_winner,(winner,idJogo))

    def updateOdds(self, idJogo, nomeEquipa, odd):
        self.mydb.execute(DBConstants.update_odds,(odd,idJogo,nomeEquipa))
        self.mydb.commit()

    def updateUserField(self, index, value, usrId): #atualizar
        if index == 0:
            self.mydb.execute(DBConstants.update_email_field, (value, usrId))
        elif index == 1:
            self.mydb.execute(DBConstants.update_nome_field, (value, usrId))
        self.mydb.commit()
        
    def getTeamsGame(self, gameId):
        return self.mydb.query(DBConstants.get_teams_by_game, (gameId, ))

    #Isto não te retorna o que queres acho, Blanc (retorna lista, faz [0] para retornar o valor)
    def getGameDate(self, gameId):
        return self.mydb.query(DBConstants.get_game_date, (gameId, ))

    def atualizaResultadoApostas(self, idJogo, winner):
        self.mydb.execute(DBConstants.set_bet_winner,(idJogo, winner))
        self.mydb.execute(DBConstants.set_bet_loser,(idJogo, winner))
        apostasOndeEstavaJogoGanho = [x[0] for x in self.mydb.query(DBConstants.get_bets_winner,(idJogo,winner))]
        apostasOndeEstavaJogoPerdido = [x[0] for x in self.mydb.query(DBConstants.get_bets_winner,(idJogo,winner))]
        
        for idAposta in apostasOndeEstavaJogoGanho:
            ganhos = self.mydb.query(DBConstants.ganho_por_aposta,(idAposta,))
            apostaGanha = 1
            for ganho in ganhos:
                if ganho[0] != 1:
                    apostaGanha = 0
            
            if apostaGanha == 1:
                self.setApostaGanha(idAposta)

        for idAposta in apostasOndeEstavaJogoPerdido:
            self.mydb.execute(DBConstants.set_aposta,(0,idAposta,))

        self.mydb.commit()
                
    def setApostaGanha(self, idAposta):

        self.mydb.execute(DBConstants.set_aposta,(1,idAposta,))

        (idUser, valor) = self.mydb.query(DBConstants.get_userid_by_bet,(idAposta,))[0]
        
        oddsList = self.mydb.query(DBConstants.get_odd_total,(idAposta,))
        oddsTotal = 1
        for odd in oddsList:
            oddsTotal = oddsTotal * odd[0]

        print(oddsTotal)
        
        self.registerTransaction(idUser,float(valor*oddsTotal),'G') 

    def getGanhos(self, idAposta):
        return self.mydb.query(DBConstants.ganho_por_aposta,(idAposta,))

    def suspensaoJogo(self, suspende, idJogo):
        self.mydb.execute(DBConstants.suspende_game, (suspende, idJogo))
        self.mydb.commit()

    #RETURN -> [[(Equipa1 do Jogo1, Joga em casa),(Equipa2 do Jogo1, Joga em Casa)],[(Equipa1 do Jogo2, Joga em casa 2),(Equipa2 do Jogo1, Joga em Casa 2)]]
    def listaJogosPorAposta(self, idAposta):
        listaIdJogos = self.mydb.query(DBConstants.idJogos_aposta,(idAposta,))
        listaJogos = []
        for idJogo in listaIdJogos:
            listaJogos.append([(x[1],x[3]) for x in self.mydb.query(DBConstants.get_teams_by_game,(idJogo[0],))])    