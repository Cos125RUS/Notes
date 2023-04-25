import view
from board import Board
from checker import Checker
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.run = True
        self.ui = User_Interface()
        self.db = Data_Base()
        self.board = self.db.get_board()
        self.checker = Checker()
        self.actions = {'exit': self.exit,
                        'journal': self.journal,
                        'add': self.add,
                        'del': self.delete,
                        'show': self.show,
                        'change': self.change}

    def use(self):
        while(self.run):
            user_entry = self.ui.enter().strip()
            try:
                self.actions[user_entry]()
            except:
                self.not_found([user_entry])

    def journal(self):
        self.ui.journal(self.board.get_all_notes())

    def add(self, args=''):
        if args == '':
            args = self.ui.write_note()
        else:
            args = self.checker.treatment(args)
        self.addition(args)

    def addition(self, data):
        try:
            self.board.new(data[0], data[1])
            self.db.save()
            self.ui.add()
        except:
            self.ui.fail()

    def delete(self, args=''):
        try:
            if args != '':
                id = self.checker.treatment(args)
            else:
                id = self.ui.enter_id()
            self.deletion(id)
        except:
            self.ui.fail()

    def deletion(self, id):
        if self.board.get_size() > id:
            self.board.delete(id)
            self.db.save()
            self.ui.delete()
        else:
            self.ui.no_id(id)

    def change(self, args):
        pass

    def show(self, args):
        pass

    def exit(self):
        self.run = False
        self.ui.exit()

    def not_found(self, args):
        self.ui.not_found(args)

    def no_command(self):
        self.ui.no_command()
