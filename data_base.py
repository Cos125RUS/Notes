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
                data = file.read().split('"board": [')
                count = int(data[0].replace('\n', '').replace(' ', '')
                            .replace(',', '').replace('{"count":', ''))
                self.board.set_count(count)
                items = data[1].replace(']\n}', '').replace(']}', '').replace('{', '')
                items = items[:items.rfind('}')].split('},')
            for item in items:
                id, head, body, create_time, last_change = self.parse(item)
                self.board.load(id, head, body, create_time, last_change)
        except:
            pass

    def save(self):
        try:
            with open('notes_db.json', 'w') as file:
                data = '{"count": %d, "board": [' % (self.board.get_count())
                for item in self.board.get_all_notes():
                    data += '{' + item.get_data() + '},'
                file.write(data[:-1] + ']}')
        except:
            pass

    def parse(self, value):
        id = value[6:value.index(', "head":')]
        head = value[value.index('"head": ') + 9:value.index('", "body":')]
        body = value[value.index('"body": ') + 9:value.index('", "create_time":')]
        create_time = value[value.index('"create_time": ') + 16:value.index('", "last_change":')]
        last_change = value[value.index('"last_change": ') + 16:-1]
        return id, head, body, create_time, last_change
