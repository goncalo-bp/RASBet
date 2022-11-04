from Menu import Menu
import time


jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]


class MenuAdmin:

    def __init__(self):
        self.obj = Menu("  Bem Vindo à RASBET.\n",["Desportos","Promoções", "Gestão de contas com privilégios", "Sair"])

    def menu_desportos(self):
        desportos = Menu.Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

        while not desportos.exit:
            sel = desportos.menu.show()
            if sel == 0:
                self.menu_futebol()
            elif sel == 1:
                self.menu_tenis()
            elif sel == 2:
                self.menu_tenis()
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
                    self.menu_abrirfechar(jogosfutebol[sel])

            if sel == len(jogosfutebol):
                self.menu_criarjogo()

            if sel == len(jogosfutebol)+1:
                futebol.exit = True

    def menu_tenis(self):
        tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not tenis.exit:
            sel = tenis.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_abrirfechar()
            elif sel == 1:
                tenis.exit = True

    def menu_basquetebol(self):
        basquetebol = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not basquetebol.exit:
            sel = basquetebol.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_abrirfechar()
                time.sleep(2)
            elif sel == 1:
                basquetebol.exit = True

    def menu_motogp(self):
        motogp = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

        while not motogp.exit:
            sel = motogp.menu.show()
            if sel == 0:
                print("Benfica - Chaves")
                self.menu_abrirfechar()
                time.sleep(2)
            elif sel == 1:
                motogp.exit = True

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

    def menu_criarjogo():
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



