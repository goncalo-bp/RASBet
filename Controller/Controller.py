from Backend.DBQueries import DBQueries
from Utilities.LoginMsgs import LoginMsgs

class Controller:
    def __init__(self):
        self.dbq = DBQueries()

    def login(self):
        user = "teste"
        password = "teste123"

        code = self.dbq.loginUser(user, password)
        
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))
        if code != 1:
            return False
        return True

    def allSports(self):
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
