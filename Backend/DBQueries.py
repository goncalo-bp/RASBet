import mysql.connector # pip install mysql-connector-python
from .DBConstants import DBConstants

class DBQueries:
    add_sport       = 'INSERT INTO Jogo(nomeDesporto) VALUES(":name"); '
    add_team        = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES(":name",:gameId,:odd,:home)'
    register_user   = 'INSERT INTO Utilizador (username,password,idCarteira,email) VALUES (":username",":password",walletId,":email")'
    get_log_info    = 'SELECT username, password FROM Utilizador WHERE username=":username"'
    add_wallet      = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00)'
    get_sports      = 'SELECT DISTINCT nomeDesporto FROM Jogo'
    get_by_sport    = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = ":sport"'
    get_game_info   = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = :gameId'


    def __init__(self):
        self.mydb = mysql.connector.connect(host = DBConstants.host, 
                                            port = DBConstants.port, 
                                            user = DBConstants.username, 
                                            password = DBConstants.password, 
                                            database = DBConstants.database) 
    
    def registerUser(self, cls, username, password, walletId, email):
        cursor = self.mydb.cursor()
        cursor.execute(cls.register_user, {"username" : username}, 
                                          {"password" : password}, 
                                          {"walletId" : walletId}, 
                                          {"email" : email})
        self.mydb.commit()
        cursor.close()
    
    def loginUser(self, cls, username, password):
        cursor = self.mydb.cursor()
        cursor.execute(cls.get_log_info, {"username" : username})

        data = cursor.fetchall()

        r = "Entrou"
        if cursor.rowcount() == 0:
            r = "Conta não existente"
        elif password != data[0][1]:
            r = "Password incorreta"
        
        cursor.close()
        return r

    def addSport(self, cls, name):
        cursor = self.mydb.cursor()
        cursor.execute(cls.add_sport, {"name" : name})
        self.mydb.commit()
        cursor.close()

    #NOTE - fazer sem home também ?
    def addTeam(self, cls, name, gameId, odd, home):
        cursor = self.mydb.cursor()
        cursor.execute(cls.add_team, {"name" : name}, 
                                     {"gameId" : gameId}, 
                                     {"odd" : odd}, 
                                     {"home" : home})
        self.mydb.commit()
        cursor.close()

    def addWallet(self, cls):
        cursor = self.mydb.cursor()
        cursor.execute(cls.add_wallet)
        self.mydb.commit()
        cursor.close()

    def getSports(self, cls):
        cursor = self.mydb.cursor()
        cursor.execute(cls.get_sports)
        
        data = cursor.fetchall()
        l = []
        for elem in data:
            l.append(elem[0])

        cursor.close()
        return l

    def getBySport(self, cls, sport):
        cursor = self.mydb.cursor()
        cursor.execute(cls.get_by_sport, {"sport" : sport})

        data = cursor.fetchall()
        l = []
        for gameId in data:
            l.append(gameId[0])

        cursor.close()
        return l

    def getGameInfo(self, cls, gameId):
        cursor = self.mydb.cursor()
        cursor.execute(cls.get_game_info, {"gameId" : gameId})

        data = cursor.fetchall()
        l = []
        for elem in data[0]:
            l.append(elem[0])        

        cursor.close()
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