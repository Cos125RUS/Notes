import view


class User_Interface:
    def __init__(self):
        self.index = 0
        self.pages = [self.menu, self.journal, self.note, self.write, self.delete]

    def run(self, value=''):
        return self.pages[self.index](value)

    def menu(self, value):
        view.show_menu()
        return input(view.user_input, end='')

    def journal(self, value):
        view.show_journal(value)
        return input(view.user_input, end='')

    def note(self, value):
        view.show_note(value)
        return input(view.user_input, end='')

    def write(self, value):
        return input(view.head(), end='') + input(view.body(), end='')


    def add(self, value):
        view.add()
        self.index = 0


    def change(self, value):
        view.change()

    def delete(self, value):
        view.delete()
