import time
import re
from Menu import Menu
from CheckStructure import CheckStruct

jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]

class MenuApostador:
    def __init__(self):
        self.obj = Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Notificações","Boletim","Alterar informações de perfil","Sair"])

    # NO CONTROLLER 

    # Editar ===============================================================
    def menuEditar(self):
        edit = Menu(f"  Editar Conta\n", ["Email","Nome","Sair"])
        sels = []
        data = []
        while not edit.exit:
            sel = edit.menu.show()
            if sel == 0:
                print("Insira o novo email: ")
                novo_email = input()
                if CheckStruct.check(novo_email):
                    sels.append(sel)
                    data.append(novo_email)
                else:
                    Menu.showMessage("Aviso -> Email inválido.\n", 1)
            elif sel == 1:
                print("Insira o novo nome: ")
                novo_nome = input()
                sels.append(sel)
                data.append(novo_nome)
            elif sel == 2:
                edit.exit = True
        return sels, data

    # Desportos ============================================================
    def menuDesportos(self, sportsList):
        desportos = Menu("  Desportos.\n", sportsList + ["Sair"])
        sel = desportos.menu.show()
        if sel == len(sportsList):
            desportos.exit = True
            return False
        else:
            return sportsList[sel]

    def menuJogos(self, names, info):
        jogos = Menu(" Jogos.\n", names + ["Sair"])
        boletim = []
        while not jogos.exit:
            sel = jogos.menu.show()
            if sel == len(names):
                jogos.exit = True
            else:
                res,odd = self.menuEvento(info[sel], names[sel])
                boletim += [(info[sel][0],names[sel],res,odd)]
        return boletim

# (id,nome,odd,jogaEmcasa)
    def menuEvento(self, gameInfo, name):
        opcoes = [f"{gameInfo[0][1]} : {gameInfo[0][2]}",f"{gameInfo[1][1]} : {gameInfo[1][2]}", f"{gameInfo[2][1]} : {gameInfo[2][2]}",]
        evento = Menu(f" {name}\n" , opcoes + ["Sair"])
        sel = evento.menu.show()
        if sel == len(opcoes):
            return None,0
        res,odd = opcoes[sel].split(':')
        return res,float(odd)
            
            

    # Carteira =============================================================
    #INCOMPLETO
    def menuCarteira(self, usrId, saldo):
        carteira = Menu(f"  Saldo :: {saldo} .\n",["Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])        
        while not carteira.exit:
            sel = carteira.menu.show()
            if sel == 0:
                self.menu_hist_apostas(usrId)
            elif sel == 1:
                self.menu_hist_transac(usrId)
            elif sel == 2:
                valor = self.menu_depositar(usrId)
                if valor != -1:
                    saldo += float(valor)
            elif sel == 3:
                saldo = self.menu_levantar(usrId,saldo)
            elif sel == 4:
                carteira.exit = True

    #INCOMPLETO
    def menuNotif(self, email, notifs): 
        notif = Menu("  Notificações.\n",notifs+["Sair"])
        

    # FORA DO CONTROLLER

    # (id,nome,aposta,odd)
    def menuBoletim(self,boletim,saldo):
        txt = []

        odd_total = 1
        if boletim == []:
            odd_total = 0
        else:
            for aposta in boletim:
                txt += [f"{aposta[1]} {aposta[2]} {aposta[3]}"]
                odd_total *= float(aposta[3])

        boletim = Menu(f"  Boletim | Odd Total: {'%.2f' % odd_total} | Saldo: {saldo}", txt + ["Apostar","Sair"])

        while not boletim.exit:
            sel = boletim.menu.show()
            if sel == len(txt):
                print("Insira montante a apostar: ")
                valor = input()
                if valor.isdecimal() and valor < saldo:
                    print("Aposta realizada com sucesso.\n")
                    time.sleep(1)
                else:
                    print("Aviso -> Saldo insuficiente")
                    time.sleep(1)
                boletim = []

            elif sel == len(txt)+1:
                boletim.exit = True
            #else:
            #   merdas


    def menu_hist_transac(email):
        lista_transac = ["T1","T2","T3","T4"]
        transac = Menu(f" Histórico de Transações .\n",lista_transac+["Sair"])

        while not transac.exit:
            sel = transac.menu.show()

            if sel == len(lista_transac):
                transac.exit = True


    def menu_hist_apostas(email):
        lista_aposta = ["A1","A2","A3","A4"]
        hist_aposta = Menu(f" Histórico de Apostas .\n",lista_aposta+["Sair"])

        while not hist_aposta.exit:
            sel = hist_aposta.menu.show()

            if sel == len(lista_aposta):
                hist_aposta.exit = True

    def menu_depositar(self, email):
        print("Prima Ctr+D para cancelar\n\n")
        print("-- Depositar Dinheiro\n")
        try:
            print("Quanto pretende transferir?\n")
            valor = input()
            if(valor.isdecimal):
                metodo = self.menu_transf() 
                time.sleep(1)
                print("Transferência realizada com sucesso!")
                return valor
            else:
                print("Aviso -> Valor inválido.")
                return -1
        except EOFError as e:
            return -1

    def check_IBAN(iban):
        if re.fullmatch(r'PT50\d{21}', iban):
            return True
        else:
            return False


    def menu_levantar(self, email,saldo):
        ### IR BUSCAR À BD ######
        print("Prima Ctr+D para cancelar\n\n")
        print("-- Levantar Dinheiro  \n")
        try:
            while True:
                print("Quanto pretende transferir?\n")
                valor = input()
                print("Instira IBAN")
                iban = input()
                if valor.isdecimal or valor < saldo:
                    if self.check_IBAN(iban): 
                        print("Transferência realizada com sucesso!\n")
                        time.sleep(1)
                        return saldo - float(valor)
                    else:
                        print("Aviso -> IBAN inválido!\n")
                        time.sleep(1)
                        return saldo
                else:
                    print("Aviso -> Valor inválido.\n")
                    time.sleep(1)
                    return saldo
        except EOFError as e:
            return saldo

    # 0 -> MBWay , 1 -> Transferencia
    def menu_transf():
        metodos = ["MBWay","Transferência Bancária"]
        metodo = Menu(f" Método de Transferência.\n",metodos+["Sair"])

        return metodo.menu.show()

    ### O QUE FAZER COM AS NOTIFICACOES ????


        while not notif.exit:
            sel = notif.menu.show()

            if sel == len(self.lista_notif):
                notif.exit = True

    #def menu_tenis():
    #    tenis = Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
    #
    #    while not tenis.exit:
    #        sel = tenis.menu.show()
    #        if sel == 0:
    #            print("Benfica - Chaves")
    #            menu_evento()
    #        elif sel == 1:
    #            tenis.exit = True
    #
    #def menu_basquetebol():
    #    basquetebol = Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
    #
    #    while not basquetebol.exit:
    #        sel = basquetebol.menu.show()
    #        if sel == 0:
    #            print("Benfica - Chaves")
    #            menu_evento()
    #            time.sleep(2)
    #        elif sel == 1:
    #            basquetebol.exit = True
    #
    #def menu_motogp():
    #    motogp = Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
    #
    #    while not motogp.exit:
    #        sel = motogp.menu.show()
    #        if sel == 0:
    #            print("Benfica - Chaves")
    #            menu_evento()
    #            time.sleep(2)
    #        elif sel == 1:
    #            motogp.exit = True
    #            
