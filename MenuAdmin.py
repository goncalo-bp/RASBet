from Menu import Menu
import time
import re
import random, string

#######  #     #  #######  #######  #######  #     #           #######  #######  #     #
#        #     #  #     #  #        #         #   #            #        #     #   #   #
#######  #######  #######  #   ###  #   ###     #              #   ###  #######     #
      #  #     #  #     #  #     #  #     #     #              #     #  #     #     #
#######  #     #  #     #  #######  #######     #              #######  #     #     #
 

#######          #######  #######  ##    #  #######  #       #######  #######  #######  #######
#                #     #  #     #  # #   #  #        #       #           #     #     #  #     #
####             #######  #######  #  #  #  ####     #       ####        #     #######  #     #
#                #        #     #  #   # #  #        #       #           #     #   #    #     #
#######          #        #     #  #    ##  #######  ####### #######  #######  #     #  #######
    

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
        jogos = Menu(" Jogos.\n", names + ["Abrir jogo"] + ["Sair"])
        sel = jogos.menu.show()
        for i in range(len(names)):
            if sel == i:
                return names[sel], info[sel]
        if sel == len(names):
            return None,"A"
        elif sel == len(names)+1:
            return None,None
                

    def menu_evento(self, names, ended):

        
        jogo = Menu(names + "\n" , ["1", "X", "2", "Sair"])
        print(names)
        names.split("X")
        while not jogo.exit:
            sel = jogo.menu.show()
            if sel == 0:
                return names[0]
            elif sel == 1:
                return names[1]
            elif sel == 2:
                return names[2] 
            elif sel == 3:
                jogo.exit = True


    def menu_criarjogo(self, desporto):
        criar = Menu("Criar novo jogo.\n", ["Inserir Equipas"] + ["Sair"])
        equipas = []
        while not criar.exit:
            sel = criar.menu.show()
            if sel == 0:
                if desporto == 'Futebol' or desporto == 'Basquetebol' or desporto == 'Ténis':
                    print("Inserir Equipa da Casa:")
                    equipaCasa = input()
                    flag = False
                    while not flag:
                        print("Insira Odd Equipa da Casa:")
                        oddCasa = input()
                        if len(oddCasa.rsplit('.')[-1]) == 2:
                            flag = True
                        else:print("Odd Inválida")
                    equipaCasa = (equipaCasa,oddCasa,1)
                    equipas.append(equipaCasa)
                    print("Inserir Equipa Visitante:")
                    equipaFora = input()
                    flag = False
                    while not flag:
                        print("Insira Odd Equipa Visitante:")
                        oddFora = input()
                        if len(oddFora.rsplit('.')[-1]) == 2:
                            flag = True
                        else:print("Odd Inválida")
                    equipaFora = (equipaFora,oddFora,0)
                    equipas.append(equipaFora)
                    flag = False
                    while not flag:
                        print("Insira a Odd do empate:")
                        oddEmpate = input()
                        if len(oddEmpate.rsplit('.')[-1]) == 2:
                            flag = True
                        else:print("Odd Inválida")
                    equipaEmpate = ("Draw",oddEmpate,0)
                    equipas.append(equipaEmpate)
                elif desporto == 'MotoGP':
                    print("Iserir nome do Grande Pŕemio")
                    nome = input()
                    i=0
                    while i<20:
                        print("Inserir Piloto:")
                        piloto = input()
                        flag = False
                        while not flag:
                            print("Inserir Odd Piloto:")
                            oddPiloto = input()
                            if len(oddPiloto.rsplit('.')[-1]) == 2:
                                flag = True
                            else:print("Odd Inválida")
                        piloto = (piloto,oddPiloto)
                        equipas.append(piloto)
                        i+=1
                flag = False
                while not flag:
                    print("Inserir data do Jogo: AAAA-MM-DD HH:MM:SS")
                    dataJogo = input()
                    test = re.search('[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]', dataJogo)
                    if test:
                        flag = True
                    else:
                        print("Formato Inválido")
                        time.sleep(2)
                idJogo = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
                return idJogo, equipas, dataJogo
            elif sel == 1:
                return None, None, None, None



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



