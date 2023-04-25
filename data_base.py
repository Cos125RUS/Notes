from board import Board


class Data_Base:
    def __init__(self):
        self.board = Board(self.get_count())


    def get_count(self):
        count = 0 #Load count with file
        return count

    def get_board(self):
        return self.board