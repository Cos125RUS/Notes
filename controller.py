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
        self.checker = Checker(self.ui, self.board)
        self.actions = {'exit': self.exit,
                        'journal': self.journal,
                        'add': self.add,
                        'del': self.delete,
                        'show': self.show,
                        'change': self.change}

    def use(self):
        while(self.run):
            user_entry = self.ui.enter().strip().split()
            try:
                self.actions[user_entry[0]](user_entry)
            except:
                self.not_found([user_entry])

    def journal(self, args):
        if len(args) == 1:
            self.ui.journal(self.board.get_all_notes())
        else:
            self.checker.journal(args)

    def user_friendly(self, func):
        try:
            num = self.ui.choice_number()
            func(num)
        except:
            self.ui.fail()

    def add(self, args):
        if len(args) == 1:
            args = self.ui.write_note()
        else:
            args = self.checker.add(args)
        self.addition(args)

    def addition(self, data):
        try:
            self.board.new(data[0], data[1])
            self.db.save()
            self.ui.add()
        except:
            self.ui.fail()

    def delete(self, args):
        if len(args) == 1:
            self.user_friendly(self.deletion)
        else:
            self.checker.delete(args)

    def deletion(self, num):
        if self.board.get_size() > num:
            self.board.delete(num)
            self.db.save()
            self.ui.delete()
        else:
            self.ui.no_index(num)

    def change(self, args):
        if len(args) == 1:
            self.user_friendly(self.changing)
        else:
            self.checker.change(args)

    def changing(self, num):
        if self.board.get_size() > num:
            head, body = self.ui.write_note()
            self.board.change(num, head, body)
            self.db.save()
            self.ui.change()
        else:
            self.ui.no_index(num)

    def show(self, args):
        if len(args) == 1:
            self.user_friendly(self.showing)
        else:
            self.checker.show(args)

    def showing(self, num):
        if self.board.get_size() > num:
            self.ui.show(self.board.get_print(num))
        else:
            self.ui.no_index(num)

    def exit(self, args):
        self.run = False
        self.ui.exit()

    def not_found(self, args):
        self.ui.not_found(args)

    def no_command(self):
        self.ui.no_command()
