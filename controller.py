from checker import Checker
from data_base import Data_Base
from ui import User_Interface


class Controller:
    """Обработка запросов пользователя"""
    def __init__(self):
        self.run = True
        self.ui = User_Interface()
        self.db = Data_Base(self.ui)
        self.board = self.db.get_board()
        self.checker = Checker(self.ui, self.board)
        self.actions = {'info': self.info,
                        'exit': self.exit,
                        'jr': self.journal,
                        'add': self.add,
                        'del': self.delete,
                        'sh': self.show,
                        'cg': self.change}

    def use(self):
        """Работа внутри оболочки"""
        while(self.run):
            user_entry = self.ui.enter().strip().split()
            try:
                self.actions[user_entry[0]](user_entry)
            except:
                self.not_found([user_entry])

    def journal(self, args):
        """Вывод журнала заметок
        :param args: Список введённых пользователем команд"""
        if len(args) == 1:
            self.ui.journal(self.board.get_all_notes())
        else:
            self.checker.journal(args)

    def user_friendly(self, func):
        """Дополнительный ввод на случай неполного указания параметров
        Функция отправляет приглашение ко вводу параметров
        Результат передаётся по цепочке дальше на модуль указанной пользователем команды
        :param func: Команда введённая пользователем"""
        try:
            num = self.ui.choice_number()
            func(num)
        except:
            self.ui.fail()

    def add(self, args):
        """Сбор и обработка параметров для новой записи в журнале
        Данные передаются по цепочке в модуль добавления
        :param args: Введённые пользователем параметры"""
        if len(args) == 1:
            args = self.ui.write_note()
        else:
            args = self.checker.cath_double_flag(args)
        self.addition(args)

    def addition(self, data):
        """Модуль добавления записей
        :param data: Обработанные параметры, введённые пользователем"""
        try:
            self.board.new(data[0], data[1])
            self.db.save()
            self.ui.add()
        except:
            self.ui.fail()

    def delete(self, args):
        """Сбор и обработка параметров для удаления заметок
        Данные передаются по цепочке в модуль удаления
        :param args: Введённые пользователем параметры"""
        if len(args) == 1:
            self.user_friendly(self.deletion)
        else:
            list(map(self.deletion, [j - i for i, j in enumerate(self.checker.cath_flag(args))]))
        self.db.save()
        self.ui.delete()

    def deletion(self, num):
        """Модуль удаления записей
        :param num: номер в списке записей"""
        if self.board.get_size() > num:
            self.board.delete(num)
        else:
            self.ui.no_index(num)

    def change(self, args):
        """Сбор и обработка параметров для изменения заметок
        Данные передаются по цепочке в модуль изменения
        :param args: Введённые пользователем параметры"""
        if len(args) == 1:
            self.user_friendly(self.entry_change)
        else:
            self.changing(*self.checker.change(args))

    def entry_change(self, num):
        """Модуль ввода заголовка и сообщения
        :param num: номер в списке записей"""
        if self.board.get_size() > num:
            head, body = self.ui.write_note()
            self.changing(num, head, body)
        else:
            self.ui.no_index(num)

    def changing(self, num, head, body):
        """Модуль внесения изменений в записи
        :param num: номер позиции в журнале
        :param head: новый заголовок
        :param body: новое содержание"""
        self.board.change(num, head, body)
        self.db.save()
        self.ui.change()

    def show(self, args):
        """Сбор и обработка параметров перед показом заметок
        Данные передаются по цепочке в модуль показа
        :param args: Введённые пользователем параметры"""
        if len(args) == 1:
            self.user_friendly(self.showing)
        else:
            list(map(self.showing, [j - i for i, j in enumerate(self.checker.cath_flag(args))]))

    def showing(self, num):
        """Модуль показа заметок
        :param num: номер в журнале"""
        if self.board.get_size() > num:
            self.ui.show(self.board.get_print(num))
        else:
            self.ui.no_index(num)

    def exit(self, args):
        """Завершение роботы в оболочке
        :param args: Введённые пользователем параметры"""
        self.run = False
        self.ui.exit()

    def not_found(self, args):
        """Ввод нераспознанной команды
        :param args: Введённые пользователем параметры"""
        self.ui.not_found(args)

    def no_command(self):
        """Команда не введена"""
        self.ui.no_command()

    def info(self, data=''):
        """Показать информацию о программе"""
        self.ui.show_info()
