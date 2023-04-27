from datetime import *

class Note:
    """Заметка"""
    def __init__(self, id, head, body, create_time='', last_change=''):
        """:param id: id
        :param head: заголовок
        :param body: текст сообщения
        :param create_time: дата создания
        :param last_change: дата последнего изменения
        Параметры create_time и last_change передаются только в случае загрузки данных из файла JSON"""
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
        id = '000'[:-len(str(self._id))] + str(self._id)
        return f'{id}.\t{self._head}\n\n{self._body}\n\n' \
               f'Создано: {self._create_time}\nПоследнее изменение:{self._last_change}'

    def set_head(self, new_item):
        """Изменение заголовка
        :param new_item: новый заголовок"""
        self._head = new_item
        self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_body(self, new_item):
        """Изменение текста заметки
        :param new_item: новый текст"""
        self._body = new_item
        self._last_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_note(self, new_head, new_body):
        """Изменение заголовка и текста заглавие
        :param new_head: новый заголовок
        :param new_body: новый текст заметки"""
        self.set_head(new_head)
        self.set_body(new_body)

    def get_note(self):
        """Предоставление данных заметки
        :return: данные заметки в виде словаря"""
        return {"id": self._id, "head": self._head, "body": self._body,
                "create_time": self._create_time, "last_change": self._last_change}

    def get_id(self):
        """Предоставление id
        :return: id заметки"""
        return self._id

    def get_head(self):
        """Предоставление заглавия
        :return: заглавие заметки"""
        return self._head

    def get_body(self):
        """Текст содержания заметки
        :return: содержание заметки"""
        return self._body

    def get_create_time(self):
        """Предоставление времени создания заметки
        :return: время создания заметки"""
        return self._create_time

    def get_change_time(self):
        """Предоставления времени последнего изменения заметки
        :return: время последнего изменения заметки"""
        return self._last_change

    def get_journal_data(self):
        """Данные заметки для вывода в журнале
        :return: id, заглавие, содержание"""
        return self._id, self._head, self._last_change

    def get_data(self):
        """Предоставление данных заметки
        :return: данные заметки, готовые к записи в формате JSON"""
        return f'"id": {self._id}, "head": "{self._head}", "body": "{self._body}", ' \
               f'"create_time": "{self._create_time}", "last_change": "{self._last_change}"'
