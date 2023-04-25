from board import Board
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.ui = User_Interface()
        self.db = Data_Base()
        self.board = self.take_board()

    def take_board(self):
        try:
            return 1 #Load board
        except:
            return Board() #New board
