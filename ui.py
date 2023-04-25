import view


class User_Interface:
    def __init__(self):
        pass

    def menu(self, value):
        view.show_menu()
        return input(view.user_input())

    def journal(self, value):
        view.show_journal(value)
        # return input(view.user_input())

    def note(self, value):
        view.show_note(value)
        return input(view.user_input())

    def write(self, value):
        return input(view.head()) + input(view.body())


    def add(self, value):
        view.add()
        self.index = 0


    def change(self, value):
        view.change()

    def delete(self, value):
        view.delete()




    def enter(self):
        return input(view.user_input())

    def exit(self):
        return view.bye()