import view
from controller import Controller

class Commutator:
    def __init__(self, args):
        self.args = args
        self.controller = Controller()
        self.function = {'info': view.get_info,
                         'add': self.controller.add,
                         'del': self.controller.delete,
                         'show': self.controller.show,
                         'journal': self.controller.journal}

    def start(self):
        try:
            self.function[self.args[1]](self.args[1:])
        except:
            if len(self.args) == 1:
                self.controller.use()
            else:
                self.controller.not_found(self.args[1:])
