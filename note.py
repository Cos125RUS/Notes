from datetime import *

class Note:
    def __init__(self, id, head, body):
        self.id = id
        self.head = head
        self.body = body
        self.create = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'{self.id}.\t{self.head}\n\n{self.body}\n\n' \
               f'Создано: {self.create}\nПоследнее изменение:{self.last_change}'
