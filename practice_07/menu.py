from contact_actions import add_contact, view_all_contacts, search_contact


def print_main_menu():
    while True:
        print("\n\033[33m\tCommands:\033[0m\n\n\
\t\033[1m0\033[0m View all contacts\n\
\t\033[1m1\033[0m Search contact\n\
\t\033[1m2\033[0m Add contact\n\
\t\033[1m5\033[0m Exit\n")
        select = input("Enter command: ")
        if select.isdigit():
            if select == '0':
                view_all_contacts()
            if select == '1':
                search_contact()
            if select == '2':
                add_contact()
            if select == '5':
                raise SystemExit
            else:
                print_main_menu()
