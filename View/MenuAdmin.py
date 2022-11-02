import Menu
import time


jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]

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
            menu_futebol()
        elif sel == 1:
            menu_tenis()
        elif sel == 2:
            menu_tenis()
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
                menu_abrirfechar(jogosfutebol[sel])

        if sel == len(jogosfutebol):
            menu_criarjogo()

        if sel == len(jogosfutebol)+1:
            futebol.exit = True

def menu_tenis():
    tenis = Menu.Menu(" Jogos.\n", ["Benfica - Chaves"] + ["Sair"])

    while not tenis.exit:
        sel = tenis.menu.show()
        if sel == 0:
            print("Benfica - Chaves")
            menu_abrirfechar()
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
        


def menu_promocoes():
    #receber promoções
    promotions = ["Promoção 1","Promoção 2","Promoção 3","Promoção 4"]
    promocoes = Menu.Menu("  Promoções\n", promotions + ["Adiciona Promoção","Sair"])

    while not promocoes.exit:
        promocoes = Menu.Menu("  Promoções.\n", promotions + ["Adiciona Promoção","Sair"])
        sel = promocoes.menu.show()
        if sel == len(promotions):
            promotions += menu_adicionar_promocao()

        elif sel == len(promotions) + 1:
            promocoes.exit = True

        else:
            id = menu_remover_promocao(promotions[sel])
            if id != -1:
                promotions.remove(id)

def menu_remover_promocao(id):
    remover = Menu.Menu(f"Promoção {id}.\n" , ["Remover"] + ["Sair"])

    while not remover.exit:
        sel = remover.menu.show()
        if sel == 0:
            ###### atualizar BD ######
            print("Promoção removida com sucesso!")
            time.sleep(1)
            return id

        if sel == 1:
            remover.exit = True
            return -1

def menu_adicionar_promocao():
    print("Prima Ctr+D para cancelar\n\n")
    try:
        print("Inserir valor da promoção\n")
        valor = input()
        print("Inserir id do jogo\n")
        id = input()

        #adicionar promoção
        if True:
            #### ATUALIZAR BD ####
            #### ENVIAR NOTIFICACAO (ATUALIZARA BD?) ####
            print("-- Promoção adicionada com sucesso!")
            time.sleep(1)
            return [id]
        else:
            print("-- Erro ao adicionar promoção")
            time.sleep(1)

    except EOFError as e:
        return


def menu_gestao_contas():
    #receber contas com privilégios
    contas = ["Conta 1","Conta 2","Conta 3"]

    gestao_contas = Menu.Menu("  Gestão de Contas.\n", contas + ["Adicionar Conta","Sair"])

    while not gestao_contas.exit:
        gestao_contas = Menu.Menu("  Gestão de Contas.\n", contas + ["Adicionar Conta","Sair"])
        sel = gestao_contas.menu.show()
        if sel == len(contas)+1:
            gestao_contas.exit = True
        
        elif sel == len(contas):
            contas += menu_adicionar_conta()
        else:
            id = menu_conta(contas[sel])
            if id != -1:
                contas.remove(id)
        
def menu_conta(id):
    conta = Menu.Menu(f"  {id}.\n",["Remover", "Sair"])

    while not conta.exit:
        sel = conta.menu.show()
        if sel == 0:
            ###### ATUALIZAR BD ######
            print("-- Conta removida com sucesso!")
            time.sleep(2)
            return id
            #remover conta
        elif sel == 1:
            conta.exit = True
            return -1

def menu_adicionar_conta():
    print("Prima Ctr+D para cancelar\n\n")
    try:
        print("Inserir email da conta\n")
        email = input()
        print("Inserir password da conta\n")
        passw = input()
        print("Inserir tipo da conta (1 -> Especialista | 2 -> Administrador)\n")
        tipo = input()

        ## check conta
        #adicionar promoção
        if True:
            #### ATUALIZAR BD ####
            print("-- Conta adicionada com sucesso!")
            time.sleep(1)
            return [email]
        else:
            print("-- Erro ao adicionar conta")
            time.sleep(1)

    except EOFError as e:
        return



