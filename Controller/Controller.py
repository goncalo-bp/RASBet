import datetime
from Backend.DBQueries import DBQueries
from Utilities.LoginMsgs import LoginMsgs
from Utilities.CheckStructure import *
from View.Menu import *
from View.MenuAdmin import *
from View.MenuEspecialista import *
from View.MenuApostador import *

class Controller:
    def __init__(self):
        self.dbq = DBQueries()
        self.view = Menu("  RASBET.\n",["Login", "Registo", "Sair"])
    
    def __exit__(self):
        self.dbq.close()

    def exec(self):
        while not self.view.exit:
            main_sel = self.view.menu.show()
            if main_sel == 0:
                ##### LOGIN #######
                tipo, email = self.execLogIn()
                if tipo == 1:
                    self.execApostador(email)
                elif tipo == 2:
                    self.execAdmin()
                elif tipo == 3:
                    self.execEspecialista()

                self.view.exit = False

            elif main_sel == 1:
                ##### REGISTO #######
                self.execRegisterUser()

            elif main_sel == 2:
                ###### SAIR #######
                self.view.showMessage("\nSaindo...", 1)
                self.view.exit = True


    # ==============================================================================
    # ==============================   LOG IN   ====================================
    # ==============================================================================

    def execLogIn(self):
        while not self.view.exit:
            self.view.exit = True
            error,email,password = self.view.menu_login()
            if error:
                return -1, None
            code = self.dbq.loginUser(email, password)
            self.view.showMessage(LoginMsgs.getLoginMsg(code), 2)
            if code == 0:
                self.view.exit = False
        return code, email

    # ==============================================================================
    # ==============================   REGISTER   ==================================
    # ==============================================================================
    
    def check_registo(self, email, date, nif):
        if CheckStruct.check(email):
            if len(nif) == 9 and nif.isdigit():
                data = CheckStruct.check_data(date)
                if data == True:
                    self.view.showMessage("\n-> Data de nascimento inválida", 2)
                    return False
                elif data == False:
                    self.view.showMessage("\n-> Data de nascimento inválida", 2)
                    return False
            else:
                self.view.showMessage("\n-> NIF inválido", 2)
                return False
        else:
            self.view.showMessage("\n-> Email inválido", 2)
            return False
        return True

    def execRegisterUser(self):
        email,password,date,nif = self.view.menu_registar()
        if self.check_registo(email, date, nif):
            code = self.dbq.registerUser(email, password, nif, date, 0, 0)
            if code == 0:
                self.view.showMessage("\n-> Conta já existente", 2)
            else:
                self.view.showMessage("\n-> Conta registada com sucesso", 2)
        

    # ==============================================================================
    # =============================   APOSTADOR   ==================================
    # ==============================================================================

    def execApostador(email):
        MenuApostador.menu_inicial_apostador(email)
        pass

    # ==============================================================================
    # ===============================   ADMIN   ====================================
    # ==============================================================================

    def execAdmin():
        #MenuAdmin.menu_inicial_administrador()
        pass

    # ==============================================================================
    # ============================   ESPECIALISTA   ================================
    # ==============================================================================

    def execEspecialista():
        #MenuEspecialista.menu_inicial_especialista()
        pass

    # ==============================================================================
    # ==============================   EXTRAS   ====================================
    # ==============================================================================

    def allSports(self):
        l = self.dbq.getSports()
        print(l)
        
    def gamesBySport(self):
        gameId = 1

        info = self.dbq.loginUser(gameId)

        # Coordenar com a view quando houver
        print(info)
    
    def gameInfo(self, gameId):
        info = self.dbq.loginUser(gameId)

        # Coordenar com a view quando houver
        print(info)