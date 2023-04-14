from AddressBook import *
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class CommandValidator():

    def __init__(self):
        self._command = None

    @property
    def valide_command(self):
        return self._command

    @valide_command.setter
    def valide_command(self, command):
        if command in commands:
            self._command = command
        else:
            raise ValueError(f'There is no such command {command}!')


class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        commands[self._payload.valide_command].execute()


class Invoker:
    _on_start = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def do_something_important(self) -> None:

        if isinstance(self._on_start, Command):
            self._on_start.execute()


class Add(Command):
    def execute():
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        book.add(record)


class Congratulate(Command):
    def execute():
        print(book.congratulate())


class Edit(Command):
    def execute():
        book.save("auto_save")
        contact_name = input('Contact name: ')
        parameter = input(
            'Which parameter to edit(name, phones, birthday, status, email, note): ').strip()

        new_value = input("New Value: ")
        return book.edit(contact_name, parameter, new_value)


class Exit(Command):
    def execute():
        print('Goodbye')
        exit()


class Help(Command):
    def execute():
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))


class Load(Command):
    def execute():
        file_name = input("File name: ")
        return book.load(file_name)


class Remove(Command):
    def execute():
        pattern = input("Remove (contact name or phone): ")
        return book.remove(pattern)


class Save(Command):
    def execute():
        file_name = input("File name: ")
        return book.save(file_name)


class Search(Command):
    def execute():
        print(
            "There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + \
                    f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)


class View(Command):
    def execute():
        print(book)


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    book = AddressBook()
    book.load("auto_save")
    invoker = Invoker()
    action = CommandValidator()
    commands = {'add': Add, 'congratulate': Congratulate, 'edit': Edit,
                'exit': Exit, 'help': Help, 'load': Load, 'remove': Remove, 'save': Save, 'search': Search}
    while True:
        action.valide_command = input(
            'Type help for list of commands or enter your command\n').strip().lower()

        invoker.set_on_start(SimpleCommand(action))
        invoker.do_something_important()
