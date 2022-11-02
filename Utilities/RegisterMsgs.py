class RegisterMsgs:
    account_exists    = "Email já existe"
    register_success  = "Conta criada com sucesso"

    @classmethod
    def getRegisterMsgs(cls, code):
        if code == 0:
            return cls.account_exists
        return cls.register_success