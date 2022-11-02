#python3 -m pip install simple-term-menu

import time
import re
from traceback import print_tb
import datetime
from dateutil.relativedelta import relativedelta

import MenuAdmin
import MenuEspecialista
import MenuApostador


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
mail_administrador = "nigga@123.com"
pass_administrador = "123"
mail_especialista = "mister@123.com"
pass_especialista = "123"

#### ACESSO À BD ####
def check_credentials(email,password):
    if email == mail and password == pasw:
        return 1
    elif email == mail_administrador and password == pass_administrador:
        return 2
    elif email == mail_especialista and password == pass_especialista:
        return 3
    else:
        return 0

def menu_login():
    try:
        print("Email")
        email = input()
        error = False
        back = False
        tipo = 0
        if(check(email)):
            print("Password")
            password = input()
            tipo = check_credentials(email,password)
            if tipo == 0:
                print("Aviso -> Credenciais Inválidas")
                time.sleep(2)
                error = True
                return back,error,tipo
            else:
                print(f"-> Sessão iniciada com {tipo}")
                back = True
                apostador = True
                time.sleep(2)
                return back,error,tipo                
        else:
            print("Aviso -> Email inválido")
            time.sleep(2)
            back = True
            error = True
            return back,error,tipo

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
              

def main():
    main = Menu("  RASBET.\n",["Login", "Registo", "Sair"])

    while not main.exit:
        main_sel = main.menu.show()
        if main_sel == 0:
            ##### LOGIN #######
            while not main.exit:
                main.exit,error,tipo = menu_login()         

            if not error:
                if tipo == 1:
                    MenuApostador.menu_inicial_apostador()
                elif tipo == 2:
                    MenuAdmin.menu_inicial_administrador()
                elif tipo == 3:
                    MenuEspecialista.menu_inicial_especialista()


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