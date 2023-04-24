from datetime import *

class Note:
    def __init__(self, id, head, body):
        self._id = id
        self._head = head
        self._body = body
        self._create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'{self._id}.\t{self._head}\n\n{self._body}\n\n' \
               f'Создано: {self._create_time}\nПоследнее изменение:{self._last_change}'

    def set_head(self, new_item):
        self._head = new_item
        self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_body(self, new_item):
        self._body = new_item
        self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_note(self, new_head, new_body):
        self.set_head(new_head)
        self.set_body(new_body)

    def get_note(self):
        return self._id, self._head, self._body, self._create_time, self._create_time

    def get_id(self):
        return self._id

    def get_head(self):
        return self._head

    def get_change_time(self):
        return self._last_change
