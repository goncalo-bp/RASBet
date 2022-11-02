#python3 -m pip install simple-term-menu

import time
import re
from traceback import print_tb
import datetime
from dateutil.relativedelta import relativedelta

from simple_term_menu import TerminalMenu

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Menu:
    def __init__(self,title,items):
        self.exit = False
        self.items = items
        self.menu = TerminalMenu(
                    menu_entries=items,
                    title=title,
                    menu_cursor="> ",
                    menu_cursor_style=("fg_green", "bold"),
                    menu_highlight_style=("bg_green", "fg_green"),
                    cycle_cursor=True,
                    clear_screen=True,
                    )

    


def check(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

mail = "ola@123.com"
pasw = "123"

#### ACESSO À BD ####
def check_credentials(email,password):
    if email == mail and password == pasw:
        return True
    else:
        return False

def menu_login():
    try:
        print("Email")
        email = input()
        error = False
        back = False
        if(check(email)):
            print("Password")
            password = input()
            if check_credentials(email,password):
                print("-> Sessão iniciada")
                back = True
                time.sleep(2)
                return back,error
            else:
                print("Aviso -> Credenciais Inválidas")
                time.sleep(2)
                error = True
                return back,error
        else:
            print("Aviso -> Email inválido")
            time.sleep(2)
            back = True
            error = True
            return back,error

    except EOFError as e:
        return True,True

def check_data(data):
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', data):
        A,M,D = data.split("-")
        data = datetime.date(int(A),int(M),int(D))
        if relativedelta(datetime.date.today(),data).years >= 18:
            return data # maior de idade
        else:
            return False # menor de idade
    else:
        return True # data invalida

def check_registo(email,passw,data_nascimento,nif):
    if check(email):
        if len(nif) == 9 and nif.isdigit():
            data = check_data(data_nascimento)
            if data == True:
                print("-> Data de nascimento inválida")
                time.sleep(2)
            elif data == False:
                print("-> Menor de idade")
                time.sleep(2)
            else:
                print("-> Registado com sucesso")
                time.sleep(2)
                
        else:
            print("-> NIF inválido")
            time.sleep(2)
    else:
        print("-> Email inválido")
        time.sleep(2)

def menu_registar():
    try:
        print("Email")
        email = input()
        print("Palavra-passe")
        palavra_passe = input()
        print("NIF")
        nif = input()
        print("Data de nascimento (AAAA-MM-DD)")
        data_nascimento = input()
        check_registo(email,palavra_passe,data_nascimento,nif)

    except EOFError as e:
        print("-> Saindo...")
        time.sleep(1)
        



def menu_inicial():
    pag_inicial = Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])

    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            menu_desportos()
        elif sel == 1:
            print("Carteira")
            #menu_carteira()

        elif sel == 2:
            print("Histórico de Apostas")
            time.sleep(2)
            #menu_historico_apostas()
        
        elif sel == 3:
            print("Histórico de transações")
            time.sleep(2)
            #menu_historico_transacoes()

        elif sel == 4:
            print("Depositar dinheiro")
            time.sleep(2)
            #menu_depositar_dinheiro()
        
        elif sel == 5:
            print("Levantar dinheiro")
            time.sleep(2)
            #menu_levantar_dinheiro()
        elif sel == 6:
            pag_inicial.exit = True
        
def menu_desportos():
    desportos = Menu("  Desportos.\n",["Futebol","Ténis","Basquetebol","MotoGP"] + ["Sair"])

    while not desportos.exit:
        sel = desportos.menu.show()
        if sel == 0:
            print("Futebol")
            time.sleep(2)
        elif sel == 1:
            print("Ténis")
            time.sleep(2)
        elif sel == 2:
            print("Basquetebol")
            time.sleep(2)
        elif sel == 3:
            print("MotoGP")
            time.sleep(2)
        elif sel == 4:
            desportos.exit = True


def main():
    main = Menu("  RASBET.\n",["Login", "Registo", "Sair"])

    while not main.exit:
        main_sel = main.menu.show()
        if main_sel == 0:
            ##### LOGIN #######
            while not main.exit:
                main.exit,error = menu_login()           

            #if apostador:
            # ...
            #if admin:
            # ...
            #if especialista:
            # ...
            
            if not error:
                menu_inicial()


            main.exit = False

        elif main_sel == 1:
            ##### REGISTO #######
            menu_registar()

        elif main_sel == 2:
            ###### SAIR #######
            print("Saindo...")
            time.sleep(1)
            main.exit = True
            


if __name__ == "__main__":
    main()