
def user_input():
    return 'notes.py:> '


def head():
    return 'Заголовок: '


def body():
    return 'Содержание: '


def choice_number():
    return 'Укажите заметки: '

def no_command():
    print("Необходимо ввести команду")


def not_found_command(command):
    print(f"Неизвестная команда - {command}")


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
    for item in journal:
        print(f'{item[0]}\t{item[1]}\t{item[2]}')

def show_note(note):
    print(note)


def delete():
    print('Заметка удалена')


def add():
    print('Заметка создана')


def change():
    print('Изменения внесены')
