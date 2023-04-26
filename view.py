
def user_input():
    return '\033[35m notes> '


def head():
    return 'Заголовок: '


def body():
    return 'Содержание: '


def choice_number():
    return 'Укажите № заметки: '


def no_command():
    print("Необходимо ввести команду")


def not_found_command(command):
    print(f"Неизвестная команда - {command}")


def no_index(num):
    print(f'Неверно указан индекс - {num}')


def fail():
    print('Ошибка ввода')


def info_info():
    print("Чтобы получить информацию о возможных командах введите python notes.py info")


def get_info(args):
    print('Здесь будет info с описанием команд')


def show_journal(journal, revers):
    try:
        print('№\tID\tДАТА ИЗМЕНЕНИЯ\t\tЗАГОЛОВОК')
        list = []
        for i in range(len(journal)):
            id, head, c_time = journal[i].get_journal_data()
            id = '000'[:-len(str(id))] + str(id)
            list.append(f'{i + 1}\t{id}\t{c_time}\t{head}')
        if revers:
            list = list[::-1]
        for line in list:
            print(line)
    except:
        print('Нет заметок')


def show_note(note):
    print(note)


def delete():
    print('Заметка удалена')


def add():
    print('Заметка создана')


def change():
    print('Изменения внесены')


def bye():
    print('Выход из notes\033[0m')
