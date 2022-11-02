import datetime
from Backend.DBQueries import DBQueries
from Utilities.LoginMsgs import LoginMsgs
from Utilities.RegisterMsgs import RegisterMsgs

class Controller:
    def __init__(self):
        self.dbq = DBQueries()

    def login(self):
        email = "private@gmail.com"
        password = "jotinha53"

        code = self.dbq.loginUser(email, "cskdn")
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))

        code = self.dbq.loginUser("sdknc", "skdnc")
        # Coordenar com a view quando houver
        print(LoginMsgs.getLoginMsg(code))

        code = self.dbq.loginUser(email, password)
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
    
    def register(self):
        email = "private@gmail.com"
        password = "jotinha53"

        code = self.dbq.registerUser(email, password, 530_053_530, datetime.date(2001, 6, 1))
        print(RegisterMsgs.getRegisterMsgs(code))

        if code != 1:
            return False
        return True