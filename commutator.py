import view
from controller import Controller

class Commutator:
    def __init__(self, args):
        self.args = args
        self.controller = Controller()
        self.function = {'info': view.get_info,
                         'use': 1,
                         'add': 2,
                         'del': 3,
                         'show': 4}

    def start(self):
        try:
            Controller().self.function[self.args[1]](self.args[1:])
        except:
            if len(self.args) == 1:
                view.no_command()
                view.info_info()
            else:
                view.not_found_command(self.args[1])
                view.info_info()
