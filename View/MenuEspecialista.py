import Menu
import time


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
        if sel == 4:
            desportos.exit = True

        else:
            menu_jogo(sel)
            


def menu_jogo(desp):

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



