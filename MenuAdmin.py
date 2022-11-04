from Menu import Menu
import time


jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]


class MenuAdmin:

    def __init__(self):
        self.obj = Menu("  Bem Vindo à RASBET.\n",["Desportos","Promoções", "Gestão de contas com privilégios", "Sair"])

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

    def menu_evento(self, names, ended, game_date, info):

        #verificar se o jogo já acabou
        if not ended:
            opcoes = ["Fechar Jogo"]
            terminado = "--> Jogo terminado"
        else:
            terminado = ""

        jogo = Menu(names + terminado + "\n" , opcoes + ["Sair"])

        while not jogo.exit:
            sel = jogo.menu.show()
            if sel == len(opcoes)-1:
                return True
            elif sel == len(opcoes):
                jogo.exit = True
#   \\\\\\
#  / o  o \
#(|   /\   |)
#  \ ____ /
#   \____/
#   /    \
#  /      \
# /        \
#(____| || | ______)
#  | |     | |
#  | |     | |
#  / /      \ \
# /_/        \_\
#(__________)

    def menu_abrirfechar(jogo):
        opcoes = ["Abrir", "Fechar"]
        abrirfechar = Menu.Menu(f" {jogo}\n" , opcoes + ["Sair"])

        while not abrirfechar.exit:
            sel = abrirfechar.menu.show()
            for i in range(len(opcoes)):
                if sel == i:
                    print(f"<3{sel}\n")
                    time.sleep(1)
            
            if sel == len(opcoes):
                abrirfechar.exit = True

    def menu_criarjogo(self):
        criar = Menu.Menu("Criar novo jogo.\n", ["Inserir Equipas"] + ["Sair"])

        while not criar.exit:
            sel = criar.menu.show()
            if sel == 0:
                print("Inserir Equipa da Casa:")
                equipaCasa = input()
                print("Inserir Equipa Visitante:")
                equipaFora = input()
                novoJogo = (equipaCasa + " - " + equipaFora)
                print(novoJogo)
                jogosfutebol.append(novoJogo)
                criar.exit = True
            elif sel == 1:
                criar.exit = True
            


    def menuPromocoes(self,proms):
        #receber promoções
        promotions = []
        for elem in proms:
            promotions += [f"Promoção {elem[0]} : IdJogo -> {elem[1]} : Valor -> {elem[2]}"]
        #promotions = ["Promoção 1","Promoção 2","Promoção 3","Promoção 4"]
        promocoes = Menu("  Promoções\n", promotions + ["Adiciona Promoção","Sair"])

        while not promocoes.exit:
            promocoes = Menu("  Promoções.\n", promotions + ["Adiciona Promoção","Sair"])
            sel = promocoes.menu.show()
            if sel < len(promotions):
                return proms[sel][0]
            elif sel == len(promotions):
                return "A"
            else:
                return 0


    def menuRemoverPromocao(self,id):
        remover = Menu(f"Promoção {id}.\n" , ["Remover"] + ["Sair"])
        sel = remover.menu.show()
        if sel == 0:
            return id
        else:
            return -1

    def menuAdicionarPromocao(self):
        print("Prima Ctr+D para cancelar\n\n")
        try:
            print("Inserir id do jogo\n")
            id = input()
            print("Inserir valor da promoção (valor entre 0 e 1)\n")
            valor = input()

            return id,valor

        except EOFError as e:
            return None,None


    def menuGestaoContas(self,cont):
        #receber contas com privilégios
        contas = []
        for elem in cont:
            contas += [f"{elem[1]}"] 

        gestao_contas = Menu("  Gestão de Contas.\n", contas + ["Adicionar Conta","Sair"])
        sel = gestao_contas.menu.show()

        if sel == len(contas)+1:
            return 0
        
        elif sel == len(contas):
            return "A"
        else:
            return cont[sel][0]
            
    def menuConta(self,id):
        conta = Menu(f"  {id}.\n",["Remover", "Sair"])

        while not conta.exit:
            sel = conta.menu.show()
            if sel == 0:
                return id
                #remover conta
            elif sel == 1:
                conta.exit = True
                return -1

    def menuAdicionarConta(self):
        print("Prima Ctr+D para cancelar\n\n")
        try:
            print("Inserir email da conta\n")
            email = input()
            print("Inserir password da conta\n")
            passw = input()
            print("Inserir tipo da conta (1 -> Especialista | 2 -> Administrador)\n")
            tipo = input()

            return email,passw,tipo

        except EOFError as e:
            return 0,0,0



