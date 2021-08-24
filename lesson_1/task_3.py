"""
Разработать генератор случайных чисел. В функцию передавать начальное и
конечное число генерации (нуль необходимо исключить). Заполнить этими данными
список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

from random import randint


def generator(start, end, count):
    lst = [randint(start, end) for i in range(count)]
    dct = {f'elem_{lst.index(i)}': i for i in lst}
    print(lst)
    print(dct)


if __name__ == '__main__':
    test_data = (1, 100, 10)
    generator(*test_data)
