from View.Menu import Menu
import time

jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]


class MenuEspecialista:

    def __init__(self):
        self.menuEspecialista = Menu("  Bem Vindo à RASBET.\n",["Desportos","Sair"])

    def menu_desportos(self):
        desportos = Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

        while not desportos.exit:
            sel = desportos.menu.show()
            if sel == 0:
                self.menu_futebol()
            elif sel == 1:
                self.menu_tenis()
            elif sel == 2:
                self.menu_basquetebol()
            elif sel == 3:
                self.menu_motogp()
            elif sel == 4:
                desportos.exit = True


    def menu_futebol(self):
    # jogos = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]
        futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Criar Jogo"] + ["Sair"])

        while not futebol.exit:
            futebol = Menu.Menu(" Jogos.\n", jogosfutebol + ["Criar Jogo"] + ["Sair"])
            sel = futebol.menu.show()
            for i in range(len(jogosfutebol)):
                if sel == i:
                    self.menu_evento(jogosfutebol[sel])

            if sel == len(jogosfutebol):
                futebol.exit = True

    def menu_tenis(self):
        tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not tenis.exit:
            sel = tenis.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_evento()
            elif sel == 1:
                tenis.exit = True

    def menu_basquetebol(self):
        basquetebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not basquetebol.exit:
            sel = basquetebol.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_evento()
                time.sleep(2)
            elif sel == 1:
                basquetebol.exit = True

    def menu_motogp(self):
        motogp = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not motogp.exit:
            sel = motogp.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_evento()
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



