class DBConstants:
    register_user      = 'INSERT INTO Utilizador (nome, email,password,idCarteira,dataNascimento,nif,isAdmin,isEspecialista) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s));'
    add_wallet         = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00);'
    get_wallet         = 'SELECT idCarteira FROM Utilizador WHERE idUser=%s;'
    get_log_info       = 'SELECT email, password, idUser, isAdmin, isEspecialista FROM Utilizador WHERE email=(%s);'
    add_team           = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES((%s),(%s),(%s),(%s));'    
    get_sports         = 'SELECT DISTINCT nomeDesporto FROM Jogo;'
    get_by_sport       = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = (%s);'
    #No de cima adicionar uma condição que só traga jogos cuja hora de inicio é depois da hora atual
    get_game_info      = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = (%s);'
    get_balance        ='SELECT saldoCarteira FROM Carteira WHERE idCarteira = (SELECT idCarteira FROM Utilizador WHERE idUser=%s);'
    create_promotion   ='INSERT INTO Promoção(idJogo, percentagemAumento) Values(%s,%s);'
    boosted_odds       = 'UPDATE EquipasPorJogo SET Odd = Odd * %s WHERE idJogo=%s;'
    get_promotion      = 'SELECT idPromoçao, percentagemAumento, idJogo FROM Promoção WHERE idPromoçao=%s'
    get_promotions     = 'SELECT * FROM Promoção'
    remove_promotion   = 'DELETE FROM Promoção WHERE idPromoçao=%s;'
    get_history_bets   ='SELECT idAposta, dataAposta, valorApostado FROM Aposta WHERE idUser=%s;'
    get_history_trans  = 'SELECT idTransação, dataTransação, saldoAntes, valorTransação FROM Transação WHERE idUser=%s;'
    get_balance        = 'SELECT saldoCarteira FROM Carteira WHERE idCarteira = (SELECT idCarteira FROM Utilizador WHERE idUser=%s);'
    reg_transaction    = 'INSERT INTO Transação(saldoAntes,valorTransação,idUser,descricao) VALUES(%s,%s,%s,%s)'
    reg_bet            = 'INSERT INTO Aposta(idUser, valorApostado) VALUES(%s,%s)'
    add_game_to_bet    = 'INSERT INTO JogoPorAposta(idAposta,idJogo,odd,resultadoApostado) VALUES(%s,%s,%s,%s)'
    get_odd_by_game    = 'SELECT Odd FROM EquipasPorJogo WHERE idJogo=%s AND nomeEquipa=%s'
    create_game        = 'INSERT INTO Jogo(idJogo, nomeDesporto, dataJogo) VALUES(%s, %s, %s);'
    add_team           = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES(%s,%s,%s,%s);'
    get_last_update    = 'SELECT lastUpdate FROM EquipasPorJogo WHERE idJogo=%s;'
    get_game_by_ID     = 'SELECT idJogo FROM Jogo WHERE idJogo=%s;'
    get_game_by_day    = 'SELECT idJogo FROM Jogo WHERE dataJogo=%s;'
    get_games_calendar = 'SELECT DISTINCT dataJogo FROM Jogo;'
    update_odds        = 'UPDATE EquipasPorJogo SET Odd=%s WHERE idJogo=%s AND nomeEquipa=%s;'
    update_email_field = 'UPDATE Utilizador SET email=%s WHERE idUser=%s;'
    update_nome_field  = 'UPDATE Utilizador SET nome=%s WHERE idUser=%s;'
    get_teams_by_game  = 'SELECT idJogo, nomeEquipa, Odd, jogaEmCasa from EquipasPorJogo WHERE idJogo=%s;'
    get_game_date      = 'SELECT dataJogo FROM Jogo WHERE idJogo=%s;'
    get_game_state     = 'SELECT Finalizado FROM Jogo WHERE idJogo=%s;'
    set_game_state     = 'UPDATE Jogo SET started=%s WHERE idJogo=%s;'
    set_winner         = 'UPDATE Jogo SET resultado=%s WHERE idJogo=%s;'
    #get_bets           = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado=%s'
    #get_bets_no_res    = 'SELECT idAposta FROM JogoPorAposta WHERE idJogo=%s AND resultadoApostado!=%s'
    set_bet_winner     = 'UPDATE JogoPorAposta SET ganho=%s WHERE idJogo=%s AND resultadoApostado=%s;'
    set_bet_loser      = 'UPDATE JogoPorAposta SET ganho=%s WHERE idJogo=%s AND resultadoApostado!=%s;'
    get_special_users  = 'SELECT idUser,email FROM Utilizador WHERE (isEspecialista=1 or isAdmin=1);'
    get_user           = 'SELECT idUser FROM Utilizador WHERE idUser=%s;'
    remove_special_user= 'DELETE FROM Utilizador WHERE idUser=%s;'
    