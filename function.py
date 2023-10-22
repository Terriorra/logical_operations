import os
import sys

from random import choice

sign_horisont = '═'
sign_vert = '║'
LINE_LEN = 90


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('about.txt')
with open(path, 'r', encoding='utf-8') as f:
    about = f.read().split('\n\n\n')

path = resource_path('NOT.txt')
with open(path, 'r', encoding='utf-8') as f:
    scheme_not = f.read().split('\n')

path = resource_path('AND_OR.txt')
with open(path, 'r', encoding='utf-8') as f:
    scheme_and_or = f.read()

path = resource_path('NOT_OR_AND.txt')
with open(path, 'r', encoding='utf-8') as f:
    scheme_not_or_and = f.read()

path = resource_path('NOT_OR_AND_2')
with open(path, 'r', encoding='utf-8') as f:
    scheme_not_or_and_2 = f.read()


def print_text(text, len_string):
    s = [f" {(len_string - 2) * sign_horisont} ", f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}"]

    for line in text:
        if len(line) + 4 < len_string:
            s.append(f"{sign_vert} {line}{(len_string - len(line) - 4) * ' '} {sign_vert}")
        else:
            s += cut_string(line, len_string)
    s.append(f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}")
    s.append(f" {(len_string - 2) * sign_horisont} ")

    return s


def cut_string(text, len_string):
    s = []

    text = text.split(' ')
    lines = []
    now = ''
    for i in text:
        if len(now + ' ' + i) < len_string - 4:
            now += ' ' + i
        else:
            lines.append(now)
            now = i
    lines.append(now)

    for line in lines:
        s.append(f"{sign_vert} {line}{(len_string - 4 - len(line)) * ' '} {sign_vert}")

    return s


class Quest:

    def __init__(self, quest, ant):
        """
        :param quest: Вопрос
        :param ant: Ответ
        """
        self.quest = quest
        self.ant = ant

    def __str__(self):
        return self.quest


def to_num(logic):
    """
    Преобразует
    True - 1
    False  - 0
    :param logic:
    :return:
    """
    if logic:
        return str(1)
    else:
        return str(0)


def quest_not():
    """
    Отрицание случайного высказывания.
    :return:
    """
    a = choice([True, False])

    s = f'Высказывание А = {to_num(a)}. Чему равно F?'

    q = Quest(s, to_num(not a))

    return q


def quest_or():
    """
    Сложение двух случайных высказываний.
    :return:
    """
    a = choice([True, False])
    b = choice([True, False])

    s = f'Высказывание А = {to_num(a)}, B = {to_num(b)}. Чему равно F?'

    q = Quest(s, to_num(a or b))

    return q


def quest_and():
    """
    Умножение двух случайных величин
    :return:
    """

    a = choice([True, False])
    b = choice([True, False])

    s = f'Высказывание А = {to_num(a)}, B = {to_num(b)}. Чему равно F?'

    q = Quest(s, to_num(a and b))

    return q


def quest1(oper):
    """
    Умножение двух случайных величин
    :return:
    """

    a = choice([True, False])
    b = choice([True, False])

    s = f'Высказывание А = {to_num(a)}, B = {to_num(b)}. Чему равно F?'

    q = Quest(s, to_num(eval(f'not a {oper} b')))

    return q


def quest2(oper):
    """
    Умножение двух случайных величин
    :return:
    """

    a = choice([True, False])
    b = choice([True, False])

    s = f'Высказывание А = {to_num(a)}, B = {to_num(b)}. Чему равно F?'

    q = Quest(s, to_num(eval(f'not b {oper} a')))

    return q


def get_text(var):
    """
    Создать текст задания.

    :param var:
    :return:
    """

    os.system("CLS")

    text = print_text(about[0].split('\n'), LINE_LEN)

    q = ''

    match var:
        case 1:
            # Отрицание
            text += print_text(about[1].split('\n'), LINE_LEN)
            text += print_text(scheme_not, LINE_LEN)

            q = quest_not()
        case 2:
            # Сложение
            text += print_text(about[2].split('\n'), LINE_LEN)
            scheme = scheme_and_or.replace('var', 'OR ').split('\n')
            text += print_text(scheme, LINE_LEN)

            q = quest_or()
        case 3:
            # Умножение
            text += print_text(about[3].split('\n'), LINE_LEN)
            scheme = scheme_and_or.replace('var', 'AND').split('\n')
            text += print_text(scheme, LINE_LEN)

            q = quest_and()

        case 4:
            # Составное высказывание
            text += print_text(about[4].split('\n'), LINE_LEN)

            operation = choice(['or ', 'and'])
            scheme = scheme_not_or_and.replace('var', operation.upper()).split('\n')
            text += print_text(scheme, LINE_LEN)

            q = quest1(operation)

        case 5:
            # Составное высказывание 2
            text += print_text(about[4].split('\n'), LINE_LEN)

            operation = choice(['or ', 'and'])
            scheme = scheme_not_or_and_2.replace('var', operation.upper()).split('\n')
            text += print_text(scheme, LINE_LEN)

            q = quest2(operation)

    return text, q
