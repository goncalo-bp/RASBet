#python3 -m pip install simple-term-menu

import time
import re
import teste

from simple_term_menu import TerminalMenu

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def main():
    main_menu_title = "  RASBET.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Login", "Registo", "Sair"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_green", "bold")
    main_menu_style = ("bg_green", "fg_green")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    edit_menu_title = "  Edit Menu.\n  Press Q or Esc to back to main menu. \n"
    edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(
        edit_menu_items,
        title=edit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    login_menu_title = "  Bem Vindo à RASBET.\n  Pressione Q ou Esc para voltar ao menu anterior. \n"
    login_menu_items = ["Desporto", "Carteira", "Sair"]
    login_menu_back = False
    login_menu = TerminalMenu(
        login_menu_items,
        title=login_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    desporto_menu_title = "  Desportos.\n  Pressione Q ou Esc para voltar ao menu anterior. \n"
    desporto_menu_items = ["Futebol"] + ["Sair"]   #teste.getListaDesportos()
    desporto_menu_back = False
    desporto_menu = TerminalMenu(
        desporto_menu_items,
        title=desporto_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:

            back = False
            while not back:
                print("Email")
                email = input()
                
                if(check(email)):
                    print("Password")
                    password = input()

                else:
                    print("Invalid Email")
                    time.sleep(1)
                    back = True

                while not login_menu_back:
                    login_sel = login_menu.show()

                    if login_sel == 0:

                        while not desporto_menu_back:
                            desporto_sel = desporto_menu.show()

                            if desporto_sel == 0:
                                print("Futebol")
                                time.sleep(1)

                            elif desporto_sel == 1:
                                print("Saindo...")
                                time.sleep(1)
                                desporto_menu_back = True

                    elif login_sel == 1:
                        print("Carteira")

                    elif login_sel == 2:
                        login_menu_back = True
                        back = True
        elif main_sel == 1:
            back = False
            while not back:
                print("Email")
                email = input()
                if(check(email)):
                    print("Palavra-passe")
                    palavra_passe = input()
                    print("Data de nascimento")
                    data_nascimento = input()
                    print("NIF")
                    nif = input()

                else:
                    print("Invalid Email")
                    time.sleep(1)
                    back = True
                back = True
        elif main_sel == 2:
            main_menu_exit = True
            


if __name__ == "__main__":
    main()