"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый
и второй множитель должны задаваться в виде аргументов функции. Значения каждой
строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на
основе списка строку. Полученная строка выводится в главной функции. Элементы
строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

list_to_string = lambda lst: '\t'.join([str(el) for el in lst])


def multiplying_table(a, b):
    table = []
    for row in range(a):
        table.append([])
        for col in range(b):
            table[row].append((row + 1) * (col + 1))

        string = list_to_string(table[row])
        print(string)


if __name__ == '__main__':
    test_data = [
        (10, 10),
        (5, 6),
        (3, 8),
    ]
    for data in test_data:
        multiplying_table(*data)
        print()
