import mysql.connector # pip install mysql-connector-python
from .Database import Database
from .DBConstants import DBConstants

class DBQueries:

    def __init__(self):
        self.mydb = Database()

    def __exit__(self):
        self.mydb.close()


    def alreadyExists(self, email):
        lines = self.mydb.query(DBConstants.get_log_info,(email))
        return len(lines) > 0

    def register(self, email, password, nif, date):
        r = 1
        alreadyExists = self.alreadyExists(email)
        if not alreadyExists:
            self.mydb.execute(DBConstants.add_wallet)
            self.mydb.execute(DBConstants.register_user,(email, password, date, nif))     
            self.mydb.commit()
        else:
            r = 0 
        return r


    def registerUser(self, username, password, walletId, email):
        self.mydb.execute(DBConstants.register_user, username,
                                             password, 
                                             walletId, 
                                             email)
        self.mydb.commit()
        self.mydb.close()
    
    def loginUser(self, username, password):
        data = self.mydb.query(DBConstants.get_log_info, username)
        r = 1
        if len(data) == 0:
            r = -1
        elif password != data[0][1]:
            r = 0     
        return r

    def addSport(self, name):
        self.mydb.execute(DBConstants.add_sport, (name))
        self.mydb.commit()
        self.cursor.close()

    #NOTE - fazer sem home também ?
    def addTeam(self, name, gameId, odd, home):
        self.mydb.execute(DBConstants.add_team, (name, gameId, odd, home))
        self.mydb.commit()

    def addWallet(self):
        self.mydb.execute(self.mydb.add_wallet)
        self.mydb.commit()

    def getSports(self):
        data = self.mydb.query(DBConstants.get_sports)
        
        l = []
        for elem in data:
            l.append(elem[0])

        return l

    def getBySport(self, sport):
        data = self.mydb.query(DBConstants.get_by_sport, (sport))

        l = []
        for gameId in data:
            l.append(gameId[0])

        return l

    def getGameInfo(self, gameId):
        data = self.mydb.query(DBConstants.get_game_info, (gameId))

        l = []
        for elem in data[0]:
            l.append(elem[0])        

        return l



#Problema aqui, podemos criar a carteira e depois não dar para criar o utilizador ... o que fazer?
#def register(username, password, email, mydb):
#    cursor = mydb.cursor(buffered=True)
#    temp = "Conta criada com êxito"
#    try:
#        cursor.execute("INSERT INTO Carteira (saldoCarteira) VALUES(0.00)")
#        cursor.execute(f'INSERT INTO Utilizador (username,password,idCarteira,email) VALUES ("{username}","{password}","{cursor.lastrowid}","{email}")')     
#        # Make sure data is committed to the database
#        mydb.commit()
#    except Exception:
#        temp = "Username ou email já existe"
#    
#    cursor.close()
#    
#    return temp
#
#def getListaEventos(mydb, desporto):
#    eventos = []
#    cursor = mydb.cursor(buffered=True,named_tuple=True)
#
#    #Lista de IdJogos do desporto
#    cursor.execute(f'SELECT idJogo FROM Jogo WHERE nomeDesporto = "{desporto}"')
#    listaIdJogo = cursor.fetchall()
#
#    for id in listaIdJogo:
#        cursor.execute(f'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = {id[0]}')
#        evento = cursor.fetchall()
#        eventos.append(evento)
#
#    cursor.close()
#
#    return eventos
#
#def getAllAccounts(mydb):
#    cursor = mydb.cursor()
#    cursor.execute(f'SELECT username, password FROM Utilizador')
#    for i in cursor.fetchall():
#        print(i[0] + " - " + i[1])
#    cursor.close()