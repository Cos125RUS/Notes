import view
from controller import Controller

class Commutator:
    """Модуль обработки запросов из командной строки"""
    def __init__(self, args):
        """:param args: Список введённых пользователем команд"""
        self.args = args
        self.controller = Controller()
        self.function = {'info': view.get_info,
                         'add': self.controller.add,
                         'del': self.controller.delete,
                         'sh': self.controller.show,
                         'jr': self.controller.journal,
                         'cg': self.controller.change}


    def start(self):
        """Запуск оболочки"""
        try:
            self.function[self.args[1]](self.args[1:])
        except:
            if len(self.args) == 1:
                self.controller.use()
            else:
                self.controller.not_found(self.args[1:])
