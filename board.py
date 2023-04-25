from note import Note

class Board:
    def __init__(self):
        self.notes = []
        self.count = 0

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view

    def new(self, id, head, body):
        self.notes.append(Note(id, head, body))
        self.count += 1

    def load(self, id, head, body, create_time, last_change):
        self.notes.append(Note(id, head, body, create_time, last_change))
        self.count += 1

    def change(self, id, head, body):
        self.notes[id].set_note(head, body)

    def get_note(self, index):
        return self.notes[index].get_note()

    def get_all_notes(self):
        return self.notes

