class Contact:
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f'{self.name} - {self.phone} ({self.comment})'

class PhoneBook:

    def __init__(self):
        self.contacts = []

    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.contacts = []
                for line in file.readlines():
                    name, number, comment = line.strip().split(',')
                    contact = Contact(name, number, comment)
                    self.contacts.append(contact)
            print('Файл открыт!')
        except FileNotFoundError:
            print('Файл не найден')

    def write_file(self, file_name):
        with open(file_name, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact['name']},{contact['number']},{contact['comment']}\n")
        print('Файл сохранен')

    def show_contacts(self):
        if not self.contacts:
            print('Список контактов пуст')
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['number']} ({contact['comment']})")

    def add_contact(self):
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        comment = input('Введите комментарий: ')
        self.contacts.append({'name': name, 'number': number, 'comment': comment})
        print('Контакт добавлен')

    def find_contact(self):
        name = input('Введите имя: ')
        for contact in self.contacts:
            if name.lower() == contact['name'].lower():
                print(f"{contact['name']} - {contact['number']} ({contact['comment']})")
                return
        print('Контакт не найден')

    def update_contact(self):
        name = input('Введите имя: ')
        for contact in self.contacts:
            if name.lower() == contact['name'].lower():
                contact['number'] = input('Введите новый номер: ')
                contact['comment'] = input('Введите новый комментарий: ')
                print('Контакт изменен')
                return
        print('Контакт не найден')

    def delete_contact(self):
        name = input('Введите имя: ')
        for i, contact in enumerate(self.contacts):
            if name.lower() == contact['name'].lower():
                self.contacts.pop(i)
                print('Контакт удален')
                return
        print('Контакт не найден')

    def menu(self):

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
                self.read_file(file_name)
            elif choice == '2':
                file_name = input('Введите имя файла: ')
                self.write_file(file_name)
            elif choice == '3':
                self.show_contacts()
            elif choice == '4':
                self.add_contact()
            elif choice == '5':
                self.update_contact()
            elif choice == '6':
                self.find_contact()
            elif choice == '7':
                self.delete_contact()
            elif choice == '8':
                print('Вы вышли из файла.')
                break
            else:
                print("Нужно выбрать пункт меню.")
