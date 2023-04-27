from note import Note

class Board:
    """Доска для хранения заметок во время работы программы"""
    def __init__(self):
        self.notes = []
        self.count = 0

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view

    def set_count(self, value):
        """Изменение значения счётчика id
        :param value: переданное значение id"""
        self.count = value

    def new(self, head, body):
        """Добавление новой заметки
        :param head: заголовок
        :param body: текст сообщения"""
        self.notes.append(Note(self.count, head, body))
        self.count += 1

    def load(self, id, head, body, create_time, last_change):
        """Загрузка заметки после запуска программы
        :param id: id
        :param head: заголовок
        :param body: текст сообщения
        :param create_time: дата создания
        :param last_change: дата последнего изменения"""
        self.notes.append(Note(id, head, body, create_time, last_change))

    def change(self, num, head, body):
        """Изменение содержания заметки
        :param num: номер в списке позиций
        :param head: заголовок
        :param body: текст сообщения"""
        self.notes[num].set_note(head, body)

    def delete(self, num):
        """Удаление заметки
        :param num: номер в списке позиций"""
        self.notes.pop(num)

    def get_note(self, index):
        """Получение заметки по индексу позиции
        :param index: номер заметки в списке позиций
        :return: экземпляр класса Note (заметка)"""
        return self.notes[index].get_note()

    def get_all_notes(self):
        """Получение всего списка заметок
        :return: список заметок (экземпляров класса note)"""
        return self.notes


    def get_count(self):
        """Предоставляет значение счётчика id
        :return: значение счётчика id """
        return self.count

    def get_size(self):
        """Предоставляет информацию о количестве заметок
        :return: размер списка заметок"""
        return len(self.notes)

    def get_print(self, index):
        """Предоставляет заметку для распечатывания
        :param index: номер позиции в списке
        :return: экземпляр класса Note"""
        return self.notes[index]

    def get_data_change(self, index):
        """Предоставляет информацию о дате и времени последнего изменения заметки
        :param index: номер позиции в списке
        :return: дата последнего изменения"""
        return self.notes[index].get_change_time()
