from note import Note

class Board:
    def __init__(self, count=0):
        self.notes = []
        self.count = count

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view

    def new(self, id, head, body):
        self.notes.append(Note(id, head, body))
        self.count += 1

    def change(self, id, head, body):
        self.notes[id].set_note(head, body)
