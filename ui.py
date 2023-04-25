import view


class User_Interface:
    def __init__(self):
        pass

    def enter(self):
        return input(view.user_input())

    def exit(self):
        view.bye()

    def journal(self, value):
        view.show_journal(value)

    def write_note(self):
        return input(view.head()), input(view.body())

    def add(self):
        view.add()

    def not_found(self, args):
        view.not_found_command(args[0])
        view.info_info()

    def no_command(self):
        view.no_command()
        view.info_info()

    def no_id(self, id):
        view.no_id(id)

    def enter_id(self):
        return int(input(view.enter_id()))

    def delete(self):
        view.delete()

    def fail(self):
        view.fail()




    def menu(self, value):
        view.show_menu()
        return input(view.user_input())

    def note(self, value):
        view.show_note(value)
        return input(view.user_input())

    def change(self, value):
        view.change()

