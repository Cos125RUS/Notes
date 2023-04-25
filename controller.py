import view
from board import Board
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.ui = User_Interface()
        self.db = Data_Base()
        self.board = self.db.get_board()

    def use(self, args):
        run = True
        while(run):
            user_enter = self.ui.run()
            if user_enter == 0:
                run = False

    def add(self, args):
        pass

    def delete(self, args):
        pass

    def show(self, args):
        pass

    def journal(self, args):
        pass

    def no_command(self):
        view.no_command()
        view.info_info()

    def not_found(self, args):
        view.not_found_command(args[1])
        view.info_info()
