class LoginMsgs:
    no_account     = "\nAviso -> Conta não existente"
    wrong_password = "\nAviso -> Credenciais incorretas"
    login_success  = " -> Sessão iniciada"

    @classmethod
    def getLoginMsg(cls, code):
        if code == 0:
            return cls.wrong_password
        if code == -1:
            return cls.no_account
        if code == 1:
            return ("\nUtilizador" + cls.login_success)
        if code == 2:
            return ("\nAdministrador" + cls.login_success)
        return ("\nEspecialista" + cls.login_success)