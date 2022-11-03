import Menu
import time
import re

jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]

def menu_inicial_apostador(email):
    saldo = 5
    pag_inicial = Menu.Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Notificações","Boletim","Alterar informações de perfil","Sair"])
    # (id,nome,aposta,odd)
    boletim = []
    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            menu_desportos(boletim)
            
        elif sel == 1:
            menu_carteira(email,saldo)

        elif sel == 2:
            menu_notif(email)

        elif sel == 3:
            menu_boletim(boletim,email,saldo)

        elif sel == 4:
            print("Editar perfil")
            menu_editar(email)

        elif sel == 5:
            pag_inicial.exit = True


#INCOMPLETO
def menu_editar(email, nome, password):

    dados_default = email + nome + password

    editar = Menu.Menu(f"  Editar Conta\n", dados_default  + ["Sair"])

    while not editar.exit:
        sel = editar.menu.show()
        if sel == 0:
            print("Insira o novo email: ")
            novo_email = input()
            if Menu.check_email(novo_email):
                print("Email gravado com sucesso.\n")
                time.sleep(1)
            else:
                print("Email inválido.\n")
                time.sleep(1)
        elif sel == 1:
            print("Insira o novo nome: ")
            novo_nome = input()
        elif sel == 2:
            print("Insira a nova password: ")
            nova_password = input()
        elif sel == 3:
            editar.exit = True

        

# (id,nome,aposta,odd)
def menu_boletim(boletim,email,saldo):
    txt = []
    odd_total = 1
    for aposta in boletim:
        txt += [f"{aposta[0]} {aposta[1]} {aposta[2]} {aposta[3]}"]
        odd_total *= float(aposta[3])

    boletim = Menu.Menu(f"  Boletim | Odd Total: {'%.2f' % odd_total} | Saldo: {saldo}", txt + ["Apostar","Sair"])

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


def menu_carteira(email,saldo):
    ### receber o saldo ####

    carteira = Menu.Menu(f"  Saldo :: {saldo} .\n",["Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])

    while not carteira.exit:
        carteira = Menu.Menu(f"  Saldo :: {saldo} .\n",["Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])

        sel = carteira.menu.show()

        if sel == 0:
            menu_hist_apostas(email)
        
        elif sel == 1:
            menu_hist_transac(email)

        elif sel == 2:
            valor = menu_depositar(email)
            if valor != -1:
                saldo += float(valor)
        
        elif sel == 3:
            saldo = menu_levantar(email,saldo)

        elif sel == 4:
            carteira.exit = True

def menu_hist_transac(email):
    lista_transac = ["T1","T2","T3","T4"]
    transac = Menu.Menu(f" Histórico de Transações .\n",lista_transac+["Sair"])

    while not transac.exit:
        sel = transac.menu.show()

        if sel == len(lista_transac):
            transac.exit = True


def menu_hist_apostas(email):
    lista_aposta = ["A1","A2","A3","A4"]
    hist_aposta = Menu.Menu(f" Histórico de Apostas .\n",lista_aposta+["Sair"])

    while not hist_aposta.exit:
        sel = hist_aposta.menu.show()

        if sel == len(lista_aposta):
            hist_aposta.exit = True

def menu_depositar(email):
    print("Prima Ctr+D para cancelar\n\n")
    print("-- Depositar Dinheiro\n")
    try:
        print("Quanto pretende transferir?\n")
        valor = input()
        if(valor.isdecimal):
            metodo = menu_transf() 
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
    

def menu_levantar(email,saldo):
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
                if check_IBAN(iban): 
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
    metodo = Menu.Menu(f" Método de Transferência.\n",metodos+["Sair"])

    return metodo.menu.show()



def menu_notif(email):
    lista_notif = ["Not1","Not2","Not3","Not4"]
    notif = Menu.Menu("  Notificações.\n",lista_notif+["Sair"])

### O QUE FAZER COM AS NOTIFICACOES ????


    while not notif.exit:
        sel = notif.menu.show()

        if sel == len(lista_notif):
            notif.exit = True


def menu_desportos(boletim):
    list_dep = ["Futebol","Ténis","Basquetebol","MotoGP"]
    desportos = Menu.Menu("  Desportos.\n", list_dep + ["Sair"])

    while not desportos.exit:
        sel = desportos.menu.show()
        if sel == 4:
            desportos.exit = True
        else:
            menu_jogo(list_dep[sel],boletim)


def menu_jogo(desp,boletim):
    #if desp == "Futebol":
    #
    #elif desp == "Ténis":
#
    #elif desp == "Basquetebol":
#
    #elif desp == "MotoGP"
   ## jogos = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]
    futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Sair"])

    while not futebol.exit:
        futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Sair"])
        sel = futebol.menu.show()
        for i in range(len(jogosfutebol)):
            if sel == i:
                res, odd = menu_evento(jogosfutebol[sel])
                boletim += [("id",jogosfutebol[sel],res,odd)]

        if sel == len(jogosfutebol):
            futebol.exit = True

#def menu_tenis():
#    tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
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
#    basquetebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
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
#    motogp = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])
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
def menu_evento(jogo):
    opcoes = ["1: 1.90", "X: 3.50", "2: 2.80"]
    evento = Menu.Menu(f" {jogo}\n" , opcoes + ["Sair"])

    while not evento.exit:
        sel = evento.menu.show()
        for i in range(len(opcoes)):
            if sel == i:
                res,odd = opcoes[sel].split(':')
                evento.exit = True
                return  res,float(odd)
        
        if sel == len(opcoes):
            evento.exit = True
            return None,0