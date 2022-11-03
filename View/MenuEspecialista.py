import Menu
import time

jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]

def menu_inicial_especialista():
    pag_inicial = Menu.Menu("  Bem Vindo à RASBET.\n",["Desportos","Sair"])

    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            menu_desportos()
        elif sel == 1:
            pag_inicial.exit = True

def menu_desportos():
    desportos = Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

    while not desportos.exit:
        sel = desportos.menu.show()
        if sel == 0:
            menu_futebol()
        elif sel == 1:
            menu_tenis()
        elif sel == 2:
            menu_basquetebol()
        elif sel == 3:
            menu_motogp()
        elif sel == 4:
            desportos.exit = True


def menu_futebol():
   # jogos = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]
    futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Criar Jogo"] + ["Sair"])

    while not futebol.exit:
        futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Criar Jogo"] + ["Sair"])
        sel = futebol.menu.show()
        for i in range(len(jogosfutebol)):
            if sel == i:
                menu_evento(jogosfutebol[sel])

        if sel == len(jogosfutebol):
            futebol.exit = True

def menu_tenis():
    tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not tenis.exit:
        sel = tenis.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_evento()
        elif sel == 1:
            tenis.exit = True

def menu_basquetebol():
    basquetebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not basquetebol.exit:
        sel = basquetebol.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_evento()
            time.sleep(2)
        elif sel == 1:
            basquetebol.exit = True

def menu_motogp():
    motogp = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not motogp.exit:
        sel = motogp.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_evento()
            time.sleep(2)
        elif sel == 1:
            motogp.exit = True
            


def menu_evento(desp):

    #verificar se o jogo já começou
    jogo_comecou = False
    if jogo_comecou:
        opcao = ["Suspender jogo e alterar Odd"]
    else:
        opcao = ["Alterar Odd"]

    jogo = Menu.Menu("  Jogo.\n", opcao + ["Sair"])

    while not jogo.exit:
        sel = jogo.menu.show()
        if sel == 0:
            print("Odd")
            time.sleep(2)
        elif sel == 2:
            jogo.exit = True



