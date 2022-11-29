import mysql.connector # pip install mysql-connector-python
from DBConstants import DBConstants
from Database import Database
from passlib.hash import sha256_crypt
from datetime import datetime

import time

class DBQueries:

    def __init__(self):
        self.mydb = Database()

    def __exit__(self):
        self.mydb.close()

    def alreadyExists(self, email):
        '''
            Função que permite saber se um email já existe na base de dados
        '''
        lines = self.mydb.query(DBConstants.get_log_info,(email,))
        return len(lines) > 0

    def registerUser(self, nome, email, password, nif, date, isAdmin, isEspecialista):
        '''
            Função que permite registar um apostador registar-se
                a "password" será encriptada em SHA-256
        '''
        r = 1
        alreadyExists = self.alreadyExists(email)

        if not alreadyExists:
            self.mydb.execute(DBConstants.add_wallet)
            self.mydb.execute(DBConstants.register_user,(nome, email, sha256_crypt.hash(password,salt="RAS2022"), self.mydb.lastrowid(), date, nif, isAdmin, isEspecialista))     
            self.mydb.commit()
        else:
            r = 0 
        return r
    
    def registerSpecialUser(self, nome, email, password, isAdmin, isEspecialista):
        '''
            Função que permite registar um administrador ou um especialista
        '''
        r = 1
        alreadyExists = self.alreadyExists(email)
        if not alreadyExists:
            self.mydb.execute(DBConstants.register_user,(nome, email, sha256_crypt.hash(password,salt="RAS2022"), None, None, None, isAdmin, isEspecialista))
            self.mydb.commit()
        else:
            r = 0
        return r
    
    def removeSpecialUser(self, id):
        '''
            Função que permite remover um administrador ou um especialista
        '''
        prom = self.mydb.query(DBConstants.get_user, (id,))
        if len(prom) == 0:
            #Não existe
            pass
        else:
            self.mydb.execute(DBConstants.remove_special_user,(id,))
            self.mydb.commit()

    def getSpecialUser(self):
        '''
            Lista de todos os administradores e especialistas
        '''
        return self.mydb.query(DBConstants.get_special_users)


    def loginUser(self, email, password):
        '''
            Função que permite fazer login
        '''
        data = self.mydb.query(DBConstants.get_log_info, (email,))
        r = 1
        usrId = True
        if len(data) == 0:
            r = -1
            usrId = False
        elif not sha256_crypt.verify(password,data[0][1]):
            r = 0 
            usrId = False
        elif data[0][3]:
            r = 2
        elif data[0][4]:
            r = 3
        if usrId:
            usrId = data[0][2]
        return r, usrId

    def addTeam(self, name, gameId, odd, home):
        '''
            Adiciona uma equipa a um jogo
        '''
        self.mydb.execute(DBConstants.add_team, (name, gameId, odd, home))
        self.mydb.commit()

    def getSports(self):
        '''
            Retorna a lista de todos os desportos disponíveis
        '''
        data = self.mydb.query(DBConstants.get_sports)
        l = []
        for elem in data:
            l.append(elem[0])
        return l

    def getBySport(self, sport, suspenso):
        '''
            Retorna a lista de todos os jogos de um determinado desporto. Pode ou não mostrar os suspensos.
        '''
        if suspenso:
            data = self.mydb.query(DBConstants.get_by_sport_wSusp, (sport,)) 
        else:
            data = self.mydb.query(DBConstants.get_by_sport, (sport,))
        l = []
        for gameId in data:
            l.append(gameId[0])
            
        self.mydb.commit()
        return l

    def getGameInfo(self, gameId):
        '''
            Retorna todas as informações sobre um jogo: Equipa, odd e se joga em casa ou não
        '''
        data = self.mydb.query(DBConstants.get_game_info, (gameId,))
        l = []
        for elem in data:
            l.append(elem)        
        return l

    def getBalance(self, usrId):
        '''
            Retorna o saldo da carteira 
        '''
        return self.mydb.query(DBConstants.get_balance, (usrId,))[0][0]

    # TODO Definir o erro
    def addPromotion(self, gameId, value):
        '''
            Adiciona uma promoção a um jogo, aumentando as odds desse jogo
        '''
        try:
            self.mydb.execute(DBConstants.create_promotion,(gameId, 1+value,))
            self.mydb.execute(DBConstants.boosted_odds,(1+value, gameId,))
            self.addNotificacao("BOOSTED ODDDDDDD!", f'Não percas esta odd gigantesca, disponível por tempo limitado!',-1)
            self.mydb.commit()
        except Exception:
            #erro
            pass
    
    # TODO Definir o erro
    def removePromotion(self, idProm):
        '''
            Remove uma promoção previamente adicionada
        '''
        prom = self.mydb.query(DBConstants.get_promotion, (idProm,))
        if len(prom) == 0:
            #Não existe
            pass
        else:
            self.mydb.execute(DBConstants.boosted_odds,(1/float(prom[0][1]), prom[0][2],))
            self.mydb.execute(DBConstants.remove_promotion,(idProm,))
            self.mydb.commit()

    def getPromotions(self):
        '''
            Retorna todas as promoções disponíveis
        '''
        return self.mydb.query(DBConstants.get_promotions)

        # Históricos
    def getHistoricoApostas(self, idUser, tipo):
        k = 0
        if tipo == 'simples':
            k = self.mydb.query(DBConstants.get_history_bets, (idUser,))
        else:
            k = self.mydb.query(DBConstants.get_history_bets_m, (idUser,))
        return k
        
    def getHistoricoTransacoes(self, idUser):
        '''
            Retorna o histórico de transações
        '''
        return self.mydb.query(DBConstants.get_history_trans, (idUser,))

    def registerTransaction(self, idUser, valor, descricao):
        '''
            Regista uma transação. Faz também a verificação de se há saldo suficiente
        '''
        bal = float(self.getBalance(idUser))
        if valor < 0 and valor*(-1) > bal:
            return -1
        else:
            idW = self.mydb.query(DBConstants.get_wallet, (idUser,))[0][0]
            self.mydb.execute(DBConstants.reg_transaction,((bal,valor,idUser,descricao)))
            self.mydb.execute(DBConstants.update_wallet,(bal+valor,idW))
            self.mydb.commit()
            return 0

    #Jogos Apostados = [(idJogo, resultadoApostado)]
    def criarAposta(self, idUser, valor, jogosApostados):
        '''
            Cria uma aposta simples ou múltipla associada a um utilizador
        '''
        wallet = self.mydb.query(DBConstants.get_wallet, (idUser,))
        if len(wallet) == 0 or self.registerTransaction(idUser,(-1)*valor,'A') == -1:
            return -1 #Não tem carteira, ou não tem dinheiro suficiente

        #Verifica se um jogo ainda não começou
        datas = []
        for id in jogosApostados:
            datas.append(self.mydb.query(DBConstants.get_game_date, (id[0],))[0][0])

        if datetime.now() > min(datas):
            return -2

        print("teste1")
        self.mydb.execute(DBConstants.reg_aposta, (idUser,valor, len(jogosApostados)))
        numAposta = self.mydb.lastrowid()
        oddsTotal = 1
        for (idJogo, resultadoApostado) in jogosApostados:
            odd = self.mydb.query(DBConstants.get_odd_by_game,(idJogo, resultadoApostado))
            oddsTotal = oddsTotal * odd[0][0]
            self.mydb.execute(DBConstants.add_game_to_bet, (numAposta,idJogo,float(odd[0][0]),resultadoApostado))
        self.mydb.execute(DBConstants.update_odd_total,(float(oddsTotal),numAposta))
        print("teste2")
        self.mydb.commit()
        
    
    def criarJogo(self, idJogo, nomeDesporto, dataJogo, equipasPresentes):
        '''
        Cria um jogo
        '''
        self.mydb.execute(DBConstants.create_game, (idJogo, nomeDesporto, dataJogo))
        for (nomeEquipa,odd,jogaEmCasa) in equipasPresentes:
            self.mydb.execute(DBConstants.add_team, (nomeEquipa,idJogo,odd,jogaEmCasa))
        self.mydb.commit()
    
    
    def datasDisponiveis(self, desporto):
        '''
        Retorna a lista com as datas em que há jogos
        '''
        return list(set([x.date() for x in [x[0] for x in (self.mydb.query(DBConstants.get_games_calendar, (desporto,)))]]))
        

    def jogoPorData(self,dia,desporto):
        '''
            Retorna os jogos numa determinada data
        '''
        return [x[1] for x in list(filter(lambda x: x[0].date() == dia, self.mydb.query(DBConstants.get_game_by_day, (desporto, ))))]
    
    def existingGame(self, idJogo):
        '''
            Retorna se já existe um jogo na base de dados
        '''
        listaJogos = self.mydb.query(DBConstants.get_game_by_ID,(idJogo,))
        return len(listaJogos) == 1

    def getLastUpdate(self, idJogo):
        '''
            Retorna a ultima vez que um jogo foi atualizado
        '''
        return self.mydb.query(DBConstants.get_last_update,(idJogo,))[0]

    def setGameState(self, finished, idJogo):
        '''
            Define o estado do jogo, se já está terminado ou não
        '''
        self.mydb.execute(DBConstants.set_game_state,(finished, idJogo,))
        self.mydb.commit()

    def getGameState(self, idJogo):
        '''
            Retorna o estado do jogo
        '''
        return self.mydb.query(DBConstants.get_game_state,(idJogo,))[0]

    def setWinner(self, idJogo, winner):
        '''
            Define o vencedor de um jogo
        '''
        self.mydb.execute(DBConstants.set_winner,(winner,idJogo))

    def updateOdds(self, idJogo, nomeEquipa, odd):
        '''
            Atualiza as odds de uma equipa num jogo
        '''
        self.mydb.execute(DBConstants.update_odds,(odd,idJogo,nomeEquipa))
        self.mydb.commit()

    def updateUserField(self, index, value, usrId):
        '''
            Permite editar o perfil
        '''
        if index == 0:
            self.mydb.execute(DBConstants.update_email_field, (value, usrId))
        elif index == 1:
            self.mydb.execute(DBConstants.update_nome_field, (value, usrId))
        self.mydb.commit()
        
    def getTeamsGame(self, gameId):
        '''
            Devolve as equipas de um jogo
        '''
        return self.mydb.query(DBConstants.get_teams_by_game, (gameId, ))

    def getGameDate(self, gameId):
        '''
            Devolve o dia do jogo de uma equipa
        '''
        return self.mydb.query(DBConstants.get_game_date, (gameId, ))[0]

    def atualizaResultadoApostas(self, idJogo, winner):
        '''
            Atualiza o resultado das apostas que tem o jogo que terminou
        '''
        self.mydb.execute(DBConstants.set_bet_winner,(idJogo, winner))
        self.mydb.execute(DBConstants.set_bet_loser,(idJogo, winner))
        apostasOndeEstavaJogoGanho = [x[0] for x in self.mydb.query(DBConstants.get_bets_winner,(idJogo,winner))]
        apostasOndeEstavaJogoPerdido = [x[0] for x in self.mydb.query(DBConstants.get_bets_loser,(idJogo,winner))]

        for idAposta in apostasOndeEstavaJogoGanho:
            
            self.mydb.execute(DBConstants.update_nmr_jogos,(idAposta,))
            nmrApostas = self.mydb.query(DBConstants.get_nmr_jogos,(idAposta,))[0][0]

            if nmrApostas == 0:
                self.setApostaGanha(idAposta)

        for idAposta in apostasOndeEstavaJogoPerdido:
            self.mydb.execute(DBConstants.set_aposta,("P",idAposta,))
            idUser = self.mydb.execute(DBConstants.get_userid_by_bet,(idAposta,))
            self.addNotificacao("Aposta perdida", f'Infelizmente perdeste a tua aposta :( Boa sorte para a próxima!',idUser)

        self.mydb.commit()
                
    def setApostaGanha(self, idAposta):
        '''
            Define a aposta dada como ganha
        '''
        self.mydb.execute(DBConstants.set_aposta,("G",idAposta,))

        (idUser, valor) = self.mydb.query(DBConstants.get_userid_by_bet,(idAposta,))[0]
        
        oddTotal = float(self.mydb.query(DBConstants.get_odd_total,(idAposta,))[0][0])
        self.addNotificacao("APOSTA GANHA!!", f'Parabéns, ganhaste uma aposta com odd {oddTotal} que te deu {float(float(valor)*oddTotal)}€!',idUser)
        self.registerTransaction(idUser,float(float(valor)*oddTotal),'G') 

    def getGanhos(self, idAposta):
        return self.mydb.query(DBConstants.ganho_por_aposta,(idAposta,))

    def suspensaoJogo(self, suspende, idJogo):
        '''
            Serve para ativar ou desativar a suspensão de um jogo
        '''
        self.mydb.execute(DBConstants.suspende_game, (suspende, idJogo))
        self.mydb.commit()

    #RETURN -> (<MontanteApostado>,<total ganho>,[([(Estoril,jogaEmCasa)],<Quem ganhou>)])
    def listaJogosPorAposta(self, idAposta):
        '''
            Devolve um tuplo com o montante apostado, o lucro ou prejuízo final e os jogos da aposta
        '''

        listaIdJogos = self.mydb.query(DBConstants.idJogos_aposta,(idAposta,))
        listaJogos = []

        montante = self.mydb.query(DBConstants.get_montante,(idAposta,))[0][0]
        ganho = 0
              
        resultado = self.mydb.query(DBConstants.get_aposta_result,(idAposta,))[0][0]

        if resultado == 'G':
            oddTotal = self.mydb.query(DBConstants.get_odd_total,(idAposta,))[0][0]
            ganho = montante * oddTotal
        
        if resultado == 'P':
            ganho = (-1) * montante
        
        for idJogo in listaIdJogos:    
            jogo = ([(i[1],i[3]) for i in self.mydb.query(DBConstants.get_teams_by_game,(idJogo[0],))])
            vencedor = self.mydb.query(DBConstants.get_game_result,(idJogo[0],))
            listaJogos.append(jogo)

        return float(montante),float(ganho),listaJogos

        # ==== NOTIFICAÇÃO ==== #
    
    def addNotificacao(self, title, text, idUser):
        '''
            Adiciona uma notificação à base de dados
        '''
        self.mydb.execute(DBConstants.add_notificacao,(idUser,title,text))

    # [(titulo, texto)]
    def getNotificacao(self, idUser):
        '''
            Devolve as notificações privadas de um utilizador, juntamente com as públicas
        '''
        return self.mydb.execute(DBConstants.add_notificacao,(idUser,))
    
    def setResultado(self, vencedor, idJogo):
        '''
            Define o resultado de um jogo
        '''
        self.mydb.execute(DBConstants.close_game,(vencedor, idJogo))
        self.mydb.execute(DBConstants.close_game_t,(idJogo,))
        self.atualizaResultadoApostas(idJogo, vencedor)
        self.mydb.commit() 
