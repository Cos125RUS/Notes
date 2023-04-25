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

    def set_count(self, value):
        self.count = value

    def new(self, head, body):
        self.notes.append(Note(self.count, head, body))
        self.count += 1

    def load(self, id, head, body, create_time, last_change):
        self.notes.append(Note(id, head, body, create_time, last_change))

    def change(self, num, head, body):
        self.notes[num].set_note(head, body)

    def delete(self, id):
        self.notes.pop(id)

    def get_note(self, index):
        return self.notes[index].get_note()

    def get_all_notes(self):
        return self.notes

    def get_count(self):
        return self.count

    def get_size(self):
        return len(self.notes)

    def get_print(self, index):
        return self.notes[index]

    def get_data_change(self, index):
        return self.notes[index].get_change_time()