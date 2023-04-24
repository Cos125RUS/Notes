from controller import Controller


class Commutator:
    def __init__(self, args):
        self.args = args
        self.controller = Controller()
        self.function = {}

    def start(self):
        try:
            self.function[self.args[1]]()
        except:
            if len(self.args == 1):
                pass #Not command, info
            else:
                pass #Not found command, info