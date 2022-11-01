class LoginMsgs:
    no_account     = "Conta não existente"
    wrong_password = "Password incorreta"
    login_success  = "Login efetuado com sucesso"

    @staticmethod
    def getLoginMsg(cls, code):
        if code == 0:
            return cls.wrong_password
        if code == -1:
            return cls.no_account
        return cls.login_success