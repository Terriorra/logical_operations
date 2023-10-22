# logical_operations
Introduction to Logical Operations

Это тренажёр для знакомства с базовыми логическими действиями:

1. Отрицание
2. Сложение
3. Умножение

Для перехода на следующий уровень необходимо ответить 10 раз подряд правильно.


1. Отрицание
Инверсия — логическое отрицание (обозначается ¬, NOT или чертой над логической переменной)
Отрицание истинного высказывания делает его ложным.
Отрицания ложного высказывания делает его истинным.

В речи используется НЕ.
А - Это кошка.
¬A - Это НЕ кошка.

Пусть 0 - это ложное высказывание.
Пусть 1 - это истинное высказывание.

      A  |  ¬A
    ------------
      0  |  1
      1  |  0


2. Сложение
Дизъюнкция — логическое сложение (обозначается ∨, OR или значком +)

Для того чтобы составное высказывание было истинным необходимо, чтобы хотя бы одна из его частей была истинной.

В речи используется союз или.
А - Число 4 четное.
В - Число 4 больше десяти.
А + В - Число 4 четное или больше 10.

Составное высказывание истинно, так как одна из частей истинна.

Пусть 0 - это ложное высказывание.
Пусть 1 - это истинное высказывание.

      A  |  B  |  A + B
    -------------------
      0  |  0  |    0
      0  |  1  |    1
      1  |  0  |    1
      1  |  1  |    1


3. Умножение
Конъюнкция — логическое умножение (обозначается ∧, AND или значком *)

Для того чтобы высказывание было истинным необходимо, чтобы обе части составного высказываниям были истинными.

В речи используется союз и.
А - Зимой холодно.
В - Зимой идёт снег.
А * В - Зимой холодно и идёт снег.

Составное высказывание истинно, так как обе части истинны.

Пусть 0 - это ложное высказывание.
Пусть 1 - это истинное высказывание.

      A  |  B  |  A * B
    -------------------
      0  |  0  |    0
      0  |  1  |    0
      1  |  0  |    0
      1  |  1  |    1
