class LoginMsgs:
    account_exists    = "Email já existe"
    register_success  = "Conta criada com sucesso"

    @staticmethod
    def getLoginMsg(cls, code):
        if code == 0:
            return cls.account_exists
        return cls.register_success