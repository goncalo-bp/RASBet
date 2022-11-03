import mysql.connector # pip install mysql-connector-python
from DBConstants import DBConstants
from Database import Database

class DBQueries:

    def __init__(self):
        self.mydb = Database()

    def __exit__(self):
        self.mydb.close()

    def alreadyExists(self, email):
        lines = self.mydb.query(DBConstants.get_log_info,(email,))
        return len(lines) > 0

    def registerUser(self, email, password, nome, nif, date, isAdmin, isEspecialista):
        r = 1
        alreadyExists = self.alreadyExists(email)

        if not alreadyExists:
            self.mydb.execute(DBConstants.add_wallet)
            self.mydb.execute(DBConstants.register_user,(email, password, nome, self.mydb.lastrowid(), date, nif, isAdmin, isEspecialista))     
            self.mydb.commit()
        else:
            r = 0 
        return r
    
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
        print(prom)
        
        if len(prom) == 0:
            #Não existe
            pass
        else:
            self.mydb.execute(DBConstants.boosted_odds,(1/float(prom[0][1]), prom[0][2],))
            self.mydb.execute(DBConstants.remove_promotion,(idProm,))
            self.mydb.commit()

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

    def updateOdds(self, idJogo, nomeEquipa, odd):
        self.mydb.execute(DBConstants.update_odds,(odd,idJogo,nomeEquipa))
        self.mydb.commit()
    def registerTransaction(self, usrId, valorApostado):
        bal = self.getBalance(usrId)
        self.mydb.execute(DBConstants.reg_transaction,((bal,valorApostado,usrId)))
        self.mydb.commit()

    def updateUserField(self, index, value, usrId): #atualizar
        if index == 0:
            name = "email"
        elif index == 1:
            name = "nome"
        self.mydb.execute(DBConstants.update_user_field, (name, value, usrId))

    def getTeamsGame(self, gameId):
        return self.mydb.query(DBConstants.get_teams_by_game, (gameId, ))

    def getGameDate(self, gameId):
        return self.mydb.query(DBConstants.get_game_date, (gameId, ))

