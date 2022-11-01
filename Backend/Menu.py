#python3 -m pip install simple-term-menu

import time

from simple_term_menu import TerminalMenu


def main():
    main_menu_title = "  RASBET.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Login", "Register"]
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

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Username")
                    username = input()
                    print("Password")
                    password = input()
                elif edit_sel == 1:
                    print("Save Selected")
                    time.sleep(5)
                elif edit_sel == 2 or edit_sel == None:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False
        elif main_sel == 1:
            print("option 2 selected")
            time.sleep(5)


if __name__ == "__main__":
    main()