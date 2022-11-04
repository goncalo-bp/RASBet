from Menu import Menu
import time
import datetime


jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]


class MenuEspecialista:

    def __init__(self):
        self.obj = Menu("  Bem Vindo à RASBET.\n",["Desportos","Sair"])

    def menuDesportos(self, sportsList):
        desportos = Menu("  Desportos.\n", sportsList + ["Sair"])
        sel = desportos.menu.show()
        if sel == len(sportsList):
            desportos.exit = True
        else:
            return sportsList[sel]


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
                

    def menuJogos(self, names, info):
        jogos = Menu(" Jogos.\n", names + ["Sair"])
        while not jogos.exit:
            sel = jogos.menu.show()

            for i in range(len(names)):
                if sel == i:
                    return names[sel], info[sel]
            if sel == len(names):
                jogos.exit = True


    def menu_evento(self, names, ended, game_date, info):
        
        #verificar se o jogo ja começou
        if game_date > datetime.datetime.now():
            alterar = "Alterar Odd no: "
        else:
            alterar = "Suspender aposta e alterar Odd no: "

        #verificar se o jogo já acabou
        if not ended:
            alterar = ""
            terminado = "Jogo terminado"
        else:
            terminado = ""

        opcoes = []
        for res in info:
            opcoes.append(f"{res[1]} : {res[2]}")

        print(opcoes)
        jogo = Menu(alterar + names + terminado + "\n" , opcoes + ["Sair"])

        while not jogo.exit:
            sel = jogo.menu.show()
            for i in range(len(opcoes)):
                if sel == i:
                    #falta alterar as odds na base de dados
                    return opcoes[sel]
            if sel == len(opcoes):
                jogo.exit = True



