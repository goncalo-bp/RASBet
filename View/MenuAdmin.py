import Menu
import time


def menu_inicial_administrador():
    pag_inicial = Menu.Menu("  Bem Vindo à RASBET.\n",["Desportos","Promoções", "Gestão de contas com privilégios", "Sair"])

    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            menu_desportos()
        elif sel == 1:
            menu_promocoes()
        elif sel == 2:
            menu_gestao_contas()
        elif sel == 3:
            pag_inicial.exit = True


def menu_desportos():
    desportos = Menu.Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

    while not desportos.exit:
        sel = desportos.menu.show()
        if sel == 0:
            print("Futebol")
            menu_futebol()
            time.sleep(2)
        elif sel == 1:
            print("Ténis")
            menu_tenis()
            time.sleep(2)
        elif sel == 2:
            print("Basquetebol")
            menu_tenis()
            time.sleep(2)
        elif sel == 3:
            print("MotoGP")
            menu_motogp()
            time.sleep(2)
        elif sel == 4:
            desportos.exit = True

def menu_futebol():
    futebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not futebol.exit:
        sel = futebol.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_abrirfechar()
            time.sleep(2)
        elif sel == 1:
            futebol.exit = True

def menu_tenis():
    tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not tenis.exit:
        sel = tenis.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_abrirfechar()
            time.sleep(2)
        elif sel == 1:
            tenis.exit = True

def menu_basquetebol():
    basquetebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not basquetebol.exit:
        sel = basquetebol.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_abrirfechar()
            time.sleep(2)
        elif sel == 1:
            basquetebol.exit = True

def menu_motogp():
    motogp = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not motogp.exit:
        sel = motogp.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_abrirfechar()
            time.sleep(2)
        elif sel == 1:
            motogp.exit = True

def menu_abrirfechar():
    abrirfechar = Menu.Menu("Jogo.\n" , ["Abrir"] + ["Fechar"] + ["Sair"])

    while not abrirfechar.exit:
        sel = abrirfechar.menu.show()
        if sel == 2:
            abrirfechar.exit = True


def menu_promocoes():
    #receber promoções
    promotions = ["Promoção 1","Promoção 2","Promoção 3","Promoção 4"]

    promocoes = Menu.Menu("  Promoções.\n", promotions + ["Sair"])

    while not promocoes.exit:
        sel = promocoes.menu.show()
        if sel == 0:
            print("Promoção 1")
            time.sleep(2)
        elif sel == 1:
            print("Promoção 2")
            time.sleep(2)
        elif sel == 2:
            print("Promoção 3")
            time.sleep(2)
        elif sel == 3:
            print("Promoção 4")
            time.sleep(2)
        elif sel == 4:
            promocoes.exit = True

def menu_gestao_contas():
    #receber contas com privilégios
    contas = ["Conta 1","Conta 2","Conta 3"]

    gestao_contas = Menu.Menu("  Gestão de Contas.\n", contas + ["Sair"])

    while not gestao_contas.exit:
        sel = gestao_contas.menu.show()
        if sel == 0:
            print("conta 1")
            time.sleep(2)
        elif sel == 1:
            print("conta 2")
            time.sleep(2)
        elif sel == 2:
            print("Conta 3")
            time.sleep(2)
        elif sel == 3:
            gestao_contas.exit = True

def menu_conta():
    conta = Menu.Menu("  Conta.\n",["Remover", "Sair"])

    while not conta.exit:
        sel = conta.menu.show()
        if sel == 0:
            print("Remover")
            time.sleep(2)
            #remover conta
        elif sel == 1:
            conta.exit = True



