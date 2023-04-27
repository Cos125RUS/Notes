import view


class User_Interface:
    """Взаимодействие с пользователем"""
    def __init__(self):
        pass

    def enter(self):
        """Приглашение ко вводу
        :return: notes>"""
        return input(view.user_input())

    def exit(self):
        """Прощальная фраза"""
        view.bye()

    def journal(self, value, revers=False, size=-1):
        """Журнал заметок"""
        view.show_journal(value, revers, size)

    def write_note(self):
        """Поочерёдное приглашение ко вводу заголовка и содержания заметки
        :return: заголовок, содержание"""
        return input(view.head()), input(view.body())


    def write_head(self):
        """Приглашение ко вводу заголовка
        :return: заголовок"""
        return input(view.head())


    def write_body(self):
        """Приглашение ко вводу содержания заметки
        :return: содержание заметки"""
        return input(view.body())


    def add(self):
        """Информация об успешном добавлении заметки"""
        view.add()

    def change(self):
        """Информация об успешном изменении заметки"""
        view.change()

    def delete(self):
        """Информация об удачном удалении заметки"""
        view.delete()

    def not_found(self, args):
        """Информация о том, что заметка не найдена"""
        view.not_found_command(args[0])
        view.info_info()

    def no_command(self):
        """Информация о том, что команда не распознана"""
        view.no_command()
        view.info_info()

    def no_index(self, num):
        """Информация о том, что номер позиции указан неверно"""
        view.no_index(num)

    def fail(self):
        """Сообщение об ошибке"""
        view.fail()

    def choice_number(self):
        """Приглашение ко вводу номера позиции
        :return: номер позиции в списке заметок"""
        return int(input(view.choice_number())) - 1

    def show(self, value):
        """Вывод заметки на экран
        :param value: данные выбранной заметки """
        view.show_note(value)

    def no_args(self):
        """Сообщение о том, что не хватает аргументов"""
        view.no_args()
        view.info_info()


    def no_quotes(self):
        """Сообщение о том, что не хватает кавычек"""
        view.no_quotes()

    def error_load(self):
        """Сообщение об ошибке чтения данных"""
        view.error_load()

    def error_save(self):
        """Сообщение об ошибке сохранения данных"""
        view.error_save()

    def show_info(self):
        """Показать информацию о программе"""
        view.get_info()
