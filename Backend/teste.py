# pip install mysql-connector-python
import mysql.connector
import DBConstants
import DBQueries

def main():
    with mysql.connector.connect(host = DBConstants.host, 
                                 port = DBConstants.port, 
                                 user = DBConstants.username, 
                                 password = DBConstants.password, 
                                 database = DBConstants.database) as mydb:
        print(register("a","a","teste@meu.com",mydb))
        print(login("a","ad",mydb))
        print(register("b","b","teste2@meu.com",mydb))
        print(login("b","b",mydb))
        print(register("d","d","teste4@meu.com",mydb))
        getAllAccounts(mydb)
        print(getListaDesportos(mydb))
        print(getListaEventos(mydb, "Tenis"))


def login(username, password, mydb):
    cursor = mydb.cursor(buffered=True,named_tuple=True)

    # por testar
    dbq.getLoginInfo(cursor, username)
    #cursor.execute(f'SELECT username, password FROM Utilizador WHERE username="{username}"')
    
    lines = cursor.fetchall()
    
    temp = "Entrou"

    if cursor.rowcount == 0:
        temp = "Não existe conta"
    elif password != lines[0][1]:
        temp = "Password incorreta"
     
    cursor.close()
    return temp

#Problema aqui, podemos criar a carteira e depois não dar para criar o utilizador ... o que fazer?
def register(username, password, email, mydb):
    cursor = mydb.cursor(buffered=True)
    temp = "Conta criada com êxito"
    try:
        cursor.execute("INSERT INTO Carteira (saldoCarteira) VALUES(0.00)")
        cursor.execute(f'INSERT INTO Utilizador (username,password,idCarteira,email) VALUES ("{username}","{password}","{cursor.lastrowid}","{email}")')     
        # Make sure data is committed to the database
        mydb.commit()
    except Exception:
        temp = "Username ou email já existe"
    
    cursor.close()
    
    return temp

def getListaDesportos(mydb):

    cursor = mydb.cursor()
    cursor.execute(f'SELECT DISTINCT nomeDesporto FROM Jogo')
    temp = cursor.fetchall()
    temp2 = []
    for i in temp:
        temp2.append(i[0])
    cursor.close()

    return temp2

def getListaEventos(mydb, desporto):
    eventos = []
    cursor = mydb.cursor(buffered=True,named_tuple=True)

    #Lista de IdJogos do desporto
    cursor.execute(f'SELECT idJogo FROM Jogo WHERE nomeDesporto = "{desporto}"')
    listaIdJogo = cursor.fetchall()

    for id in listaIdJogo:
        cursor.execute(f'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = {id[0]}')
        evento = cursor.fetchall()
        eventos.append(evento)

    cursor.close()

    return eventos

def getAllAccounts(mydb):
    cursor = mydb.cursor()
    cursor.execute(f'SELECT username, password FROM Utilizador')
    for i in cursor.fetchall():
        print(i[0] + " - " + i[1])
    cursor.close()

if __name__ == "__main__":
    main()