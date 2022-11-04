import datetime
from DBQueries import DBQueries
from LoginMsgs import LoginMsgs
from CheckStructure import *
from Menu import *
from MenuAdmin import MenuAdmin
from MenuEspecialista import MenuEspecialista
from MenuApostador import MenuApostador


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
                tipo,usrId = self.execLogIn()
                if tipo == 1:
                    self.execApostador(usrId)
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
                code = -1
                usrId = None
            else:
                code,usrId = self.dbq.loginUser(email, password)
                self.view.showMessage(LoginMsgs.getLoginMsg(code), 2)
                if code == 0:
                    self.view.exit = False
        return code,usrId

    # ==============================================================================
    # ==============================   REGISTER   ==================================
    # ==============================================================================
    
    def check_registo(self, email, date, nif):
        if CheckStructure.check(email):
            if len(nif) == 9 and nif.isdigit():
                data = CheckStructure.check_data(date)
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
            code = self.dbq.registerUser("",email, password, nif, date, 0, 0)
            if code == 0:
                self.view.showMessage("\n-> Conta já existente", 2)
            else:
                self.view.showMessage("\n-> Conta registada com sucesso", 2)
        

    # ==============================================================================
    # =============================   APOSTADOR   ==================================
    # ==============================================================================

    def execApostador(self, usrId):
        boletim = []
        menuApostador = MenuApostador()
        while not menuApostador.obj.exit:
            sel = menuApostador.obj.menu.show()
            if sel == 0:
                self.execDesportos(menuApostador, usrId,boletim)
            elif sel == 1:
                self.execCarteira(menuApostador, usrId)
            elif sel == 2:
                self.execNotif(menuApostador, usrId)
            elif sel == 3:
                balance = self.dbq.getBalance(usrId)[0][0]
                menuApostador.menuBoletim(boletim,usrId,balance)
            elif sel == 4:
                self.execEdit(menuApostador, usrId)
            elif sel == 5:
                menuApostador.obj.exit = True

    # =============================   DESPORTOS   ==================================
    def execDesportos(self, ma, usrId,boletim):
        sportsList = self.dbq.getSports()
        md = ma.menuDesportos(sportsList)
        #while not md
        desporto = None
        jogos = self.dbq.getBySport(desporto)
        names = []
        info = []
        for idJogo in jogos:
            data = self.dbq.getTeamsGame(idJogo)
            if desporto == "Futebol":
                for i in range(3):
                    if data[i][1] == "Draw":
                        draw = i
                    elif data[i][3]:
                        home = i
                names.append(f"{data[home][1]} X {data[3-draw-home][1]}")
            elif desporto == "Basquetebol":
                for i in range(2):
                    if data[i][4]:
                        home = i
                names.append(f"{data[home][1]} - {data[2-draw-home][1]}")
                info.append(data) # id ; nome ; odd ; joga_em_casa
            elif desporto == "Ténis":
                names.append(f"{data[home][1]} - {data[2][1]}")
                info.append(data) # id ; nome ; odd ; joga_em_casa
            elif desporto == "MotoGP":
                date = self.dbq.getGameDate[0]
                names.append(f"GP : {date}")
            info.append(data) # id ; nome ; odd ; joga_em_casa
        boletim += ma.menuJogos(names, info)

        #add apostas e etc


    # ===============================   EDITAR   =================================== FEITO
    def execEdit(self, ma, userId):
        sels, data = ma.menuEditar() # 0=email ; 1=nome
        for i in range(len(sels)):
            self.dbq.updateUserField(sels[i], data[i], userId)
        self.view.showMessage(" -> Informação atualizada", 2)

    # ==============================   CARTEIRA   ================================== 
    def execCarteira(self, ma, usrId):
        balance = self.dbq.getBalance(usrId)[0][0]
        ma.menuCarteira(usrId,balance)
        

    # ============================   NOTIFICACAO   =================================
    def execNotif(self, ma, email):
        notifs = ["Not1","Not2","Not3","Not4"] # SACAR DA BD
        ma.menuNotif(email, notifs)

    # ==============================   BOLETIM   ===================================


    # ==============================================================================
    # ===============================   ADMIN   ====================================
    # ==============================================================================

    def execAdmin():
        
        menuAdmin = MenuAdmin()

        while not menuAdmin.exit:
            sel = menuAdmin.menu.show()
            if sel == 0:
                MenuAdmin.menu_desportos()
            elif sel == 1:
                MenuAdmin.menu_promocoes()
            elif sel == 2:
                MenuAdmin.menu_gestao_contas()
            elif sel == 3:
                MenuAdmin.menuAdmi.exit = True

    # ==============================================================================
    # ============================   ESPECIALISTA   ================================
    # ==============================================================================

    def execEspecialista():
        menuEspecialista = MenuEspecialista()
        
        while not menuEspecialista.exit:
            sel = menuEspecialista.menu.show()
            if sel == 0:
                MenuEspecialista.menu_desportos()
            elif sel == 1:
                menuEspecialista.exit = True

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