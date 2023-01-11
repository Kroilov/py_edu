# Указываем файл с контактами:
# database = 'L:\gb_edu\Python_edu\homework_py\practice_07\contacts.csv'
database = 'contacts.csv'


# Считываем файл в список:
def read_to_list(database):
    with open(database, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            data.append(line.strip().split(','))

    return data


# Спрашиваем индекс строки для редактирования:
def ask_for_edit(contacts):
    answer = input("To edit contact enter Index (or press Enter for exit): ")
    if answer.isdigit():
        if int(answer) in range(len(contacts)):
            edit_contact(int(answer), contacts)


# Просмотр списка всех контактов:
def view_all_contacts():
    print("\033[33mAll contacts:\033[0m\n")
    contacts = read_to_list(database)
    for line in contacts:
        print(contacts.index(line), ' '.join(map(str, line)))

        # Каждые 10 строк тормозим:
        if contacts.index(line) > 0 and contacts.index(line) % 10 == 0:
            input("Press Enter to continue...\n")

    # Предлагаем выбрать контакт для редактирования:
    ask_for_edit(contacts)


# Поиск контактов
def search_contact():
    search_data = str(input("\nLooking for (or press Enter for exit): "))
    contacts = read_to_list(database)
    flag = True
    for line in contacts:
        if search_data in line:
            print(contacts.index(line), ' '.join(map(str, line)))
            flag = False
    if flag:
        print('\nNo contacts found.')
    else:
        ask_for_edit(contacts)


# Добавляем контакт непосредственно в файл без чтения:
def add_contact():
    data = ()
    data = input(
        "\n\033[33mAdding a new contact\033[0m\n\nEnter contact name: ") + ','
    data += input("Enter last name: ") + ','
    data += input("Enter phone number: ") + ','
    data += input("Enter comment: ") + '\n'
    write_line(data)
    print("Successfully added!\n")


def write_line(data):
    with open(database, 'a') as file:
        file.write(data)


# Перезапись списка целиком в файл: 
def save_to_csv(data, database):
    with open(database, 'w') as file:
        for line in data:
            file.write(','.join(line) + '\n')


# Редактируем контакт через изменение списка контактов и перезапись в файл:
def edit_contact(line, contacts):
    print('\nEditing:\n',' '.join(map(str, contacts[line])))
    print("\n\033[33m\tEdit:\033[0m\n\n\
\t\033[1m1\033[0m Name\n\
\t\033[1m2\033[0m Last name\n\
\t\033[1m3\033[0m Contact number\n\
\t\033[1m4\033[0m Comment\n\
\t\033[1m5\033[0m Save changes and exit\n\
\t\033[1m6\033[0m Delete contact\n\
\tor press Enter to Exit\n")
    while True:

        # Если редактируемый параметр не был введен изначально, он будет добавлен:
        select = input("Enter command: ")
        if select.isdigit():
            if select == '1':
                contacts[line][0] = input("Enter new name: ")
                print('Name changed.\n')
            if select == '2':
                contacts[line][1] = input("Enter new last name: ")
                print('Last name changed.\n')
            if select == '3':
                contacts[line][2] = input("Enter new phone number: ")
                print('Number changed.\n')
            if select == '4':
                contacts[line][3] = input("Enter new comment: ")
                print('Comment changed.\n')
            if select == '5':
                save_to_csv(contacts, database)
                print("Changes have been saved!")
                break

            if select == '6':
                if str(input("Type <yes> for delete contact: ").lower()) == 'yes':
                    contacts.pop(line)
                    save_to_csv(contacts, database)
                    print("Successfully deleted!\n")
                    break

        else:
            break