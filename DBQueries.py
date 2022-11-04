import mysql.connector # pip install mysql-connector-python
from DBConstants import DBConstants
from Database import Database
from passlib.hash import sha256_crypt

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
            self.mydb.execute(DBConstants.register_user,(nome, email, password, self.mydb.lastrowid(), date, nif, isAdmin, isEspecialista))     
            self.mydb.commit()
        else:
            r = 0 
        return r
    
    def registerSpecialUser(self, nome, email, password, isAdmin, isEspecialista):
        r = 1
        alreadyExists = self.alreadyExists(email)
        if not alreadyExists:
            self.mydb.execute(DBConstants.register_user,(nome, email, password, None, None, None, isAdmin, isEspecialista))
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
        usrId = data[0][2]
        if len(data) == 0:
            r = -1
            usrId = False
        elif password != data[0][1]:
            r = 0 
            usrId = False
        elif data[0][3]:
            r = 2
        elif data[0][4]:
            r = 3
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
        return self.mydb.query(DBConstants.get_balance, (usrId,))

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
    def getHistoricoApostas(self, usrId):
        return self.mydb.query(DBConstants.get_history_bets, (usrId,))
        
    def getHistoricoTransacoes(self, usrId):
        return self.mydb.query(DBConstants.get_history_trans, (usrId,))

    def registerTransaction(self, usrId, valorApostado):
        bal = self.getBalance(usrId)
        self.mydb.execute(DBConstants.reg_transaction,((bal,valorApostado,usrId)))
        self.mydb.commit()

    #Jogos Apostados = [(idJogo, resultadoApostado)]
    def criarAposta(self, email, valor, jogosApostados):
        self.mydb.execute(DBConstants.reg_aposta, (email,valor))
        numAposta = self.mydb.lastrowid()
        for (idJogo, resultadoApostado) in jogosApostados:
            odd = self.mydb.query(DBConstants.get_odd_by_game,(idJogo, resultadoApostado))
            self.mydb.execute(DBConstants.add_game_to_bet, (numAposta,idJogo,odd,resultadoApostado))
        self.mydb.commit()
        self.registerTransaction(email,(-1)*valor,'A')

    def criarJogo(self, idJogo, nomeDesporto, dataJogo, equipasPresentes):
        self.mydb.execute(DBConstants.create_game, (idJogo, nomeDesporto, dataJogo))
        for (nomeEquipa,odd,jogaEmCasa) in equipasPresentes:
            self.mydb.execute(DBConstants.add_team, (nomeEquipa,idJogo,odd,jogaEmCasa))
        self.mydb.commit()
    
    def existingGame(self, idJogo):
        listaJogos = self.mydb.query(DBConstants.get_game,(idJogo,))
        return len(listaJogos) == 1

    def getLastUpdate(self, idJogo):
        return self.mydb.query(DBConstants.get_last_update,(idJogo,))[0]

    def setGameState(self, started, idJogo):
        return self.mydb.execute(DBConstants.get_game_state,(started, idJogo,))

    def getGameState(self, idJogo):
        return self.mydb.execute(DBConstants.set_game_state,(idJogo,))[0]

    def setWinner(self, idJogo, winner):
        self.mydb.execute(DBConstants.set_winner,(winner,idJogo))

    def updateOdds(self, idJogo, nomeEquipa, odd):
        self.mydb.execute(DBConstants.update_odds,(odd,idJogo,nomeEquipa))
        self.mydb.commit()

    def registerTransaction(self, usrId, valorApostado):
        bal = self.getBalance(usrId)
        self.mydb.execute(DBConstants.reg_transaction,((bal,valorApostado,usrId)))
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
         
