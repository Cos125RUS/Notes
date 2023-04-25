from board import Board


class Data_Base:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        self.load()
        return self.board

    def load(self):
        try:
            with open('notes_db.json', 'r') as file:
                return file.read()
        except:
            pass

    def save(self):
        try:
            with open('notes_db.json', 'w') as file:
                file.write('[')
                for item in self.board.get_all_notes():
                    file.write(item)
                file.write(']')
        except:
            pass
