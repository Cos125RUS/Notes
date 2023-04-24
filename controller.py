from board import Board
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.ui = User_Interface()
        self.db = Data_Base()
        self.board = Board()
