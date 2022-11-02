from Backend.DBQueries import DBQueries
from Utilities.LoginMsgs import LoginMsgs

class Controller:
    def __init__(self):
        self.dbq = DBQueries()

    def login(self):
        email = "a"
        password = "a"

        code = self.dbq.loginUser(email, "b")
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))

        code = self.dbq.loginUser("b", password)
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))

        code = self.dbq.loginUser(email, password)
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))

        if code != 1:
            return False
        return True

    def allSports(self):
        self.dbq.addSport("Futebol")
        self.dbq.addSport("Basquetebol")
        self.dbq.addSport("MotoGP")
        self.dbq.addSport("Ténis")
        l = self.dbq.getSports()

        print(l)
        
    def gamesBySport(self):
        gameId = 1

        info = self.dbq.loginUser(gameId)

        # Coordenar com a view quando houver
        print(info)
    
    def gameInfo(self):
        gameId = 1

        info = self.dbq.loginUser(gameId)

        # Coordenar com a view quando houver
        print(info)
