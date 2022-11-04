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
                    self.execEspecialista(usrId)

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
                self.execDesportos(menuApostador, boletim)
            elif sel == 1:
                self.execCarteira(menuApostador, usrId)
            elif sel == 2:
                self.execNotif(menuApostador, usrId)
            elif sel == 3:
                self.execBoletim(menuApostador, usrId, boletim)
            elif sel == 4:
                self.execEdit(menuApostador, usrId)
            elif sel == 5:
                menuApostador.obj.exit = True

    # =============================   DESPORTOS   ==================================
    def execDesportos(self, ma, boletim):
        sportsList = self.dbq.getSports()
        desporto = sportsList[0]
        while desporto in sportsList:
            desporto = ma.menuDesportos(sportsList)
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
            if len(names) > 0:
                r = ma.menuJogos(names, info)
                boletim += r
            sportsList = self.dbq.getSports()

    # ===============================   EDITAR   =================================== FEITO
    def execEdit(self, ma, userId):
        sels, data = ma.menuEditar() # 0=email ; 1=nome
        for i in range(len(sels)):
            self.dbq.updateUserField(sels[i], data[i], userId)
        self.view.showMessage(" -> Informação atualizada", 2)

    # ==============================   CARTEIRA   ================================== 
    def execCarteira(self, ma, usrId):
        balance = self.dbq.getBalance(usrId)
        valor,tipo = ma.menuCarteira(usrId,balance)
        if valor != None:
            if tipo == "D":
                self.dbq.registerTransaction(usrId,float(valor),"D")
            elif tipo == "L":
                if self.dbq.registerTransaction(usrId,0-float(valor),"L") == -1:
                    self.view.showMessage(" -> Saldo insuficiente", 2)
        

    # ============================   NOTIFICACAO   =================================
    def execNotif(self, ma, email):
        notifs = ["Not1","Not2","Not3","Not4"] # SACAR DA BD
        ma.menuNotif(email, notifs)

    # ==============================   BOLETIM   ===================================
    def execBoletim(self, ma, usrId, boletim):
        balance = self.dbq.getBalance(usrId)[0][0]
        ma.menuBoletim(boletim,balance)


    # ==============================================================================
    # ===============================   ADMIN   ====================================
    # ==============================================================================

    def execAdmin(self):
        
        menuAdmin = MenuAdmin()

        while not menuAdmin.obj.exit:
            sel = menuAdmin.obj.menu.show()
            if sel == 0:
                MenuAdmin.menu_desportos()
            elif sel == 1:
                self.execPromocoes(menuAdmin)
            elif sel == 2:
                self.execGestaoContas(menuAdmin)
            elif sel == 3:
                MenuAdmin.obj.exit = True

    # =============================   PROMOCOES   ================================== FEITO
    def execPromocoes(self,mAdmin):
        promos = self.dbq.getPromotions()
        sel = mAdmin.menuPromocoes(promos)
        if sel == "A":
            self.execAddPromo(mAdmin)
        elif sel == 0:
            return
        else:
            for elem in promos:
                print(elem)
                print(sel)
                time.sleep(3)
                if elem[0] == sel:
                    self.execRemovePromo(mAdmin, elem)
                    break

    def execAddPromo(self,mAdmin):
        id,valor = mAdmin.menuAdicionarPromocao()
        if id != None:
            self.dbq.addPromotion(id,float(valor))
            self.view.showMessage(" -> Promoção adicionada", 2)

    def execRemovePromo(self,mAdmin, promo):
        if mAdmin.menuRemoverPromocao(promo) != -1:
            self.dbq.removePromotion(promo[0])
            self.view.showMessage(" -> Promoção removida", 2)

    # =============================   GESTAO DE CONTAS   ================================== FEITO

    def execGestaoContas(self, mAdmin):
        users = self.dbq.getSpecialUser()
        sel = mAdmin.menuGestaoContas(users)
        if sel == "A":
            self.execAddUser(mAdmin)
        elif sel == 0:
            return
        else:
            for elem in users:
                if elem[0] == sel:
                    self.execRemoveUser(mAdmin, elem)
                    break

    def execAddUser(self, mAdmin):
        email,passw,tipo = mAdmin.menuAdicionarConta()
        if email != 0:
            if tipo == 1:
                r = self.dbq.registerSpecialUser("", email, passw,0,1)
                if r == 1:
                    self.view.showMessage(" -> Conta adicionada", 2)
            else:
                r = self.dbq.registerSpecialUser("", email, passw,1,0)
                if r == 1:
                    self.view.showMessage(" -> Conta adicionada", 2)
            
    def execRemoveUser(self, mAdmin, user):
        if mAdmin.menuConta(user) != -1:
            self.dbq.removeSpecialUser(user[0])
            self.view.showMessage(" -> Conta removida", 2)

    # ==============================================================================
    # ============================   ESPECIALISTA   ================================
    # ==============================================================================

    def execEspecialista(self, usrId):
        menuEspecialista = MenuEspecialista()
        
        while not menuEspecialista.obj.exit:
            sel = menuEspecialista.obj.menu.show()
            if sel == 0:
                self.execDesportosEspecialista(menuEspecialista, usrId)
            elif sel == 1:
                menuEspecialista.obj.exit = True


    # ==============================================================================
    # ==============================   DESPORTOS   =================================
    # ==============================================================================
    def execDesportosEspecialista(self, me, usrId):
            sportsList = self.dbq.getSports()
            desporto = me.menuDesportos(sportsList)
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
            game_name, check_info = me.menuJogos(names, info)
            started = self.dbq.getGameState(check_info[0][0])
            game_date = self.dbq.getGameDate(check_info[0][0])
            new_odd = me.menu_evento(game_name, started, game_date[0][0], check_info)
            self.dbq.updateOdds(check_info[0][0],new_odd)

            #add apostas e etc
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