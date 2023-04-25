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
                items = file.read().replace('[', '').replace(']', '').replace('{', '')\
                    .replace('\n', '')
                items += ','
                items = items.split('},')
            for item in items:
                id, head, body, create_time, last_change = self.parse(item)
                self.board.load(id, head, body, create_time, last_change)
        except:
            pass

    def save(self):
        try:
            with open('notes_db.json', 'w') as file:
                data = '['
                for item in self.board.get_all_notes():
                    data += '{' + item.get_data() + '},'
                file.write(data[:-1] + ']')
        except:
            pass

    def parse(self, value):
        items = value.split(',')
        id = items[0].replace('"id":', '').strip()
        head = items[1].replace('"head":', '').replace('"', '').strip()
        body = items[2].replace('"body":', '').replace('"', '').strip()
        create_time = items[3].replace('"create_time":', '').replace('"', '').strip()
        last_change = items[4].replace('"last_change":', '').replace('"', '').strip()
        return id, head, body, create_time, last_change
