# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
#
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = []
            for line in file.readlines():
                name, number, comment = line.strip().split(',')
                contacts.append({'name': name, 'number': number, 'comment': comment})
            return contacts
    except FileNotFoundError:
        print('Файл не найден')

def write_file(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']} - {contact['number']} ({contact['comment']})\n")
    print('Файл сохранен')

def show_contacts(contacts):
    if not contacts:
        print('Список контактов пуст')
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['number']} ({contact['comment']})")

def add_contact(contacts):
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    comment = input('Введите комментарий: ')
    contacts.append({'name': name, 'number': number, 'comment': comment})
    print('Контакт добавлен')

def find_contact(contacts):
    name = input('Введите имя: ')
    for contact in contacts:
        if name.lower() == contact['name'].lower():
            print(f"{contact['name']} - {contact['number']} ({contact['comment']})")
            return
    print('Контакт не найден')

def update_contact(contacts):
    name = input('Введите имя: ')
    for contact in contacts:
        if name.lower() == contact['name'].lower():
            contact['number'] = input('Введите новый номер: ')
            contact['comment'] = input('Введите новый комментарий: ')
            print('Контакт изменен')
            return
    print('Контакт не найден')

def delete_contact(contacts):
    name = input('Введите имя: ')
    for i, contact in enumerate(contacts):
        if name.lower() == contact['name'].lower():
            contacts.pop(i)
            print('Контакт удален')
            return
    print('Контакт не найден')

def menu():
    file_name = None
    contacts = []
    while True:
        print('Меню:')
        print('1. Открыть файл')
        print('2. Сохранить файл')
        print('3. Показать контакты')
        print('4. Добавить контакт')
        print('5. Изменить контакт')
        print('6. Найти контакт')
        print('7. Удалить контакт')
        print('8. Выход')

        choice = input('Введите номер пункта меню: ')
        if choice == '1':
            file_name = input('Введите имя файла: ') # имя файла необходимо вводить contacts, иначе файл не найден
            contacts = read_file(file_name)
        elif choice == '2':
            if not file_name:   # если файла для сохранения не существует, программа попросит ввести имя для нового файла
                file_name = input('Введите имя файла: ')
            write_file(file_name, contacts)
        elif choice == '3':
            show_contacts(contacts)
        elif choice == '4':
            add_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            find_contact(contacts)
        elif choice == '7':
            delete_contact(contacts)
        elif choice == '8':
            print('Вы вышли из файла.')
            break
        else:
            print("Нужно выбрать пункт меню.")
print(menu())