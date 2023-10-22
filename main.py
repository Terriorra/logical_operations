from function import get_text
from random import choice

for var in range(1, 4):
    right = 0

    while right < 10:

        text, q = get_text(var)
        for i in text:
            print(i)
        print()
        print(q)
        ant = input('0 или 1? ').strip()

        if ant == q.ant:
            right += 1
            print(f'Верно! Осталось ответить {10 - right} раз.')
        else:
            right = 0
            print(f'Не верно! Правильный ответ {q.ant}. Серия начинается заново.')
        input("Для продолжения нажмите enter...")

    input('Уровень пройден! Для продолжения нажмите на enter...')

right = 0
while right < 10:

    text, q = get_text(choice([4, 5]))
    for i in text:
        print(i)
    print()
    print(q)
    ant = input('0 или 1? ').strip()

    if ant == q.ant:
        right += 1
        print(f'Верно! Осталось ответить {10 - right} раз.')
    else:
        right = 0
        print(f'Не верно! Серия начинается заново.')
    input("Для продолжения нажмите enter...")

print("Тренировка пройдена!")
input('')
input('Для завершения нажмите на enter...')
