from note import Note

class Board:
    def __init__(self, count):
        self.notes = []
        self.count = count

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view