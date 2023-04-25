from datetime import *

class Note:
    def __init__(self, id, head, body, create_time='', last_change=''):
        self._id = id
        self._head = head
        self._body = body
        if create_time == '':
            self._create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self._create_time = create_time
        if last_change == '':
            self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self._last_change = last_change

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
        return {"id": self._id, "head": self._head, "body": self._body,
                "create_time": self._create_time, "last_change": self._last_change}

    def get_id(self):
        return self._id

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def get_create_time(self):
        return self._create_time

    def get_change_time(self):
        return self._last_change

    def get_data(self):
        return f'"id": {self._id}, "head": {self._head}, "body": {self._body}, ' \
               f'"create_time": {self._create_time}, "last_change": {self._last_change}'
