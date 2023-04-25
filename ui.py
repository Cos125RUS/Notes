import view


class User_Interface:
    def __init__(self):
        pass

    def enter(self):
        return input(view.user_input())

    def exit(self):
        view.bye()

    def journal(self, value, revers):
        view.show_journal(value, revers)

    def write_note(self):
        return input(view.head()), input(view.body())

    def add(self):
        view.add()

    def change(self):
        view.change()

    def not_found(self, args):
        view.not_found_command(args[0])
        view.info_info()

    def no_command(self):
        view.no_command()
        view.info_info()

    def no_index(self, num):
        view.no_index(num)

    def choice_number(self):
        return int(input(view.choice_number())) - 1

    def delete(self):
        view.delete()

    def show(self, value):
        view.show_note(value)

    def fail(self):
        view.fail()
