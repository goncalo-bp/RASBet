import mysql.connector

class DBQueries:
    add_desporto    = 'INSERT INTO Jogo(nomeDesporto) VALUES(":name"); '
    add_team        = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES(":name",:gameId,:odd,:home)'
    register_user   = 'INSERT INTO Utilizador (username,password,idCarteira,email) VALUES (":username",":password",walletId,":email")'
    get_log_info    = 'SELECT username, password FROM Utilizador WHERE username=":username"'
    add_wallet      = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00)'
    get_by_desporto = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = ":desporto"'
    get_game_info   = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = :gameId'
    get_desportos   = 'SELECT DISTINCT nomeDesporto FROM Jogo'

    def addDesporto(cls, cur, name):
        cur.execute(cls.add_desporto, {"name" : name})

    #NOTE - fazer sem home também ?
    def addTeam(cls, cur, name, gameId, odd, home):
        cur.execute(cls.add_team, {"name" : name}, 
                                  {"gameId" : gameId}, 
                                  {"odd" : odd}, 
                                  {"home" : home})
    
    def registerUser(cls, cur, username, password, walletId, email):
        cur.execute(cls.register_user, {"username" : username}, 
                                       {"password" : password}, 
                                       {"walletId" : walletId}, 
                                       {"email" : email})
    
    def getLoginInfo(cls, cur, username):
        cur.execute(cls.get_log_info, {"username" : username})
    
    def addWallet(cls, cur):
        cur.execute(cls.add_wallet)
    
    def getByDesporto(cls, cur, desporto):
        cur.execute(cls.get_by_desporto, {"desporto" : desporto})
    
    def getGameInfo(cls, cur, gameId):
        cur.execute(cls.get_game_info, {"gameId" : gameId})

    def getDesportos(cls, cur):
        cur.execute(cls.get_desportos)