

class Board:
    def __init__(self):
        self.notes = []

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view