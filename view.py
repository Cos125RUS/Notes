
def user_input():
    return '\033[37m notes> '


def head():
    return 'Заголовок: '


def body():
    return 'Содержание: '


def choice_number():
    return 'Укажите заметки: '


def enter_id():
    return 'Введите ID: '


def no_command():
    print("Необходимо ввести команду")


def not_found_command(command):
    print(f"Неизвестная команда - {command}")


def no_id(id):
    print(f'Неверно указан ID - {id}')


def fail():
    print('Ошибка ввода')


def info_info():
    print("Чтобы получить информацию о возможных командах введите python notes.py info")


def get_info(args):
    print('Здесь будет info с описанием команд')


def show_menu():
    print('1 - Просмотр заметок')
    print('2 - Создать заметку')
    print('3 - удалить заметку')
    print('4 - редактировать заметку')
    print('0 - выйти')


def show_journal(journal):
    try:
        print('ID\tДАТА ИЗМЕНЕНИЯ\t\tЗАГОЛОВОК')
        for item in journal:
            id, head, c_time = item.get_journal_data()
            print(f'{id}\t{c_time}\t{head}')
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
    print('Выход из notes')
