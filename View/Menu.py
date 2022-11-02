#python3 -m pip install simple-term-menu

import time
import re
from traceback import print_tb

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
                print("-> Logged in")
                back = True
                time.sleep(2)
                return back,error
            else:
                print("Invalid Credentials")
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


def menu_registar():
    try:
        print("Email")
        email = input()
        if(check(email)):
            print("Palavra-passe")
            palavra_passe = input()
            print("Data de nascimento (AAAA-MM-DD)")
            data_nascimento = input()
            print("NIF")
            nif = input()
            print("-> Registado com sucesso")
            time.sleep(2)
        else:
            print("Aviso -> Email Invalido!")
            time.sleep(2)
            back = True
    except EOFError as e:
        print("-> Saindo...")
        time.sleep(1)
        



def menu_inicial():
    pag_inicial = Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])

    while not pag_inicial.exit:
        sel = pag_inicial.menu.show()
        if sel == 0:
            print("Desportos")
            time.sleep(2)
            menu_desportos()
        elif sel == 1:
            print("Carteira")
            time.sleep(2)
            #menu_carteira()

        
        elif sel == 2:
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