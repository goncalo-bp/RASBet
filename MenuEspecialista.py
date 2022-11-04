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
                

    def menuJogos(self, names, info):
        jogos = Menu(" Jogos.\n", names + ["Sair"])
        while not jogos.exit:
            sel = jogos.menu.show()

            for i in range(len(names)):
                if sel == i:
                    return names[sel], info[sel]
            if sel == len(names):
                jogos.exit = True


    def menu_evento(self, names, ended, info):
        
        #verificar se o jogo ja começou
        #if game_date > datetime.datetime.now():
            #alterar = "Alterar Odd no: "
        #else:
        alterar = "Suspender aposta e alterar Odd no: "

        #verificar se o jogo já acabou
        if not ended:
            alterar = ""
            terminado = "--> Jogo terminado"
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
                    flag = False
                    while not flag:
                        print("Insira nova Odd")
                        new_odd = input()
                        if len(new_odd.rsplit('.')[-1]) == 2:
                            flag = True
                            return opcoes[sel].split(':'),new_odd
                        else:
                            print("Odd inválida! Por favor insira uma Odd com duas casas decimais")
                            time.sleep(2)
            if sel == len(opcoes):
                jogo.exit = True


