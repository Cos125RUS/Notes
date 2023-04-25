import view
from board import Board
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.run = True
        self.ui = User_Interface()
        self.db = Data_Base()
        self.board = self.db.get_board()
        self.actions = {'exit': self.exit,
                        'journal': self.journal}

    def use(self, args):
        while(self.run):
            self.actions[self.ui.enter().strip()]()

    def add(self, args):
        pass

    def delete(self, args):
        pass

    def show(self, args):
        pass

    def journal(self, args):
        self.ui.journal(self.board.get_all_notes())

    def exit(self):
        self.run = False
        view.bye()

    def no_command(self):
        view.no_command()
        view.info_info()

    def not_found(self, args):
        view.not_found_command(args[1])
        view.info_info()
