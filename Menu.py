#python3 -m pip install simple-term-menu
import time
from traceback import print_tb

from CheckStructure import *

from simple_term_menu import TerminalMenu


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
    
    @staticmethod
    def showMessage(msg, t):
        print(msg)
        time.sleep(t)

    def menu_login(self):
        try:
            print("Email:")
            email = input()
            if not CheckStruct.check(email):
                self.showMessage("\nAviso -> Email inválido", 2)
                return True,email,None
            print("Password:")
            password = input()
            return False, email, password            
        except EOFError as e:
            return True,None,None
        
    def menu_registar(self):
        try:
            print("Email:")
            email = input()
            print("Palavra-passe:")
            palavra_passe = input()
            print("NIF:")
            nif = input()
            print("Data de nascimento: (AAAA-MM-DD)")
            data_nascimento = input()
            return email,palavra_passe,data_nascimento,nif
        except EOFError as e:
            self.showMessage("-> Saindo...", 1)
