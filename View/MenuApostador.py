import Menu
import time

def menu_inicial_apostador():
    pag_inicial = Menu.Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Notificações","Boletim","Alterar informações de perfil","Sair"])

    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            menu_desportos()
            
        elif sel == 1:
            menu_carteira()

        elif sel == 2:
            menu_notif()

        elif sel == 3:
            print("Boletim")
            #menu_boletim()

        elif sel == 4:
            print("Editar perfil")
            menu_editar()

        elif sel == 5:
            pag_inicial.exit = True

def menu_editar():
    ol = 1


def menu_carteira():
    ### receber o saldo ####
    saldo = 5
    carteira = Menu.Menu(f"  Saldo :: {saldo} .\n",["Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])

    while not carteira.exit:
        sel = carteira.menu.show()

        if sel == 0:
            menu_hist_apostas()
        
        elif sel == 1:
            menu_hist_transac()

        elif sel == 2:
            menu_depositar()
        
        elif sel == 3:
            menu_levantar()

        elif sel == 4:
            carteira.exit = True

def menu_hist_transac():
    lista_transac = ["T1","T2","T3","T4"]
    transac = Menu.Menu(f" Histórico de Transações .\n",lista_transac+["Sair"])

    while not transac.exit:
        sel = transac.menu.show()

        if sel == len(lista_transac):
            transac.exit = True


def menu_hist_apostas():
    lista_aposta = ["A1","A2","A3","A4"]
    hist_aposta = Menu.Menu(f" Histórico de Apostas .\n",lista_aposta+["Sair"])

    while not hist_aposta.exit:
        sel = hist_aposta.menu.show()

        if sel == len(lista_aposta):
            hist_aposta.exit = True

def menu_depositar():
    print("-- Depositar Dinheiro\n")
    print("Quanto pretende transferir?\n")
    valor = input()
    if(valor.isdecimal):
        metodo = menu_transf() 
        time.sleep(1)
        print("Transferência realizada com sucesso!")
    else:
        print("Aviso -> Valor inválido.")
        time.sleep(1)

def menu_levantar():
    print("-- Levantar Dinheiro\n")
    print("Quanto pretende transferir?\n")
    valor = input()
    if(valor.isdecimal):
        metodo = menu_transf() 
        time.sleep(1)
        print("Transferência realizada com sucesso!")
    else:
        print("Aviso -> Valor inválido.")
        time.sleep(1)

# 0 -> MBWay , 1 -> Transferencia
def menu_transf():
    metodos = ["MBWay","Transferência Bancária"]
    metodo = Menu.Menu(f" Método de Transferência.\n",metodo+["Sair"])

    return metodo.menu.show()



def menu_notif():
    lista_notif = ["Not1","Not2","Not3","Not4"]
    notif = Menu.Menu("  Notificações.\n",lista_notif+["Sair"])

### O QUE FAZER COM AS NOTIFICACOES ????

    while not notif.exit:
        sel = notif.menu.show()

        if sel == len(lista_notif):
            notif.exit = True


def menu_desportos():
    desportos = Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

    while not desportos.exit:
        sel = desportos.menu.show()
        if sel == 0:
            print("Futebol")
            time.sleep(2)
        elif sel == 1:
            print("Ténis")
            time.sleep(2)
        elif sel == 2:
            print("Basquetebol")
            time.sleep(2)
        elif sel == 3:
            print("MotoGP")
            time.sleep(2)
        elif sel == 4:
            desportos.exit = True