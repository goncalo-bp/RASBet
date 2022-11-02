class DBConstants:
    # Connection 
    username = "rasbet"
    password = "GrupoDosFixes?"
    host     = "rasbet69.mysql.database.azure.com"
    port     = 3306
    database = "rasbet"
    # Queries
    add_sport       = 'INSERT INTO Jogo(nomeDesporto) VALUES("?");'
    add_team        = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES("?",?,?,?);'
    register_user   = 'INSERT INTO Utilizador (email,password,idCarteira,dataNascimento,nif) VALUES ("?","?",?,?,?);'
    get_log_info    = 'SELECT email, password FROM Utilizador WHERE email="?";'
    add_wallet      = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00);'
    get_sports      = 'SELECT DISTINCT nomeDesporto FROM Jogo;'
    get_by_sport    = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = "?";'
    get_game_info   = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = ?;'
