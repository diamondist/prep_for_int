"""
Дополнить следующую функцию недостающим кодом:
"""

from pathlib import Path


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    p = Path(sPath)
    if p.exists():
        try:
            for item in p.iterdir():
                if item.is_file():
                    print(item)
                else:
                    print_directory_contents(item)
        except PermissionError:
            print('Passing not autorized file...')
    else:
        print('Wrong path name')


if __name__ == '__main__':
    print_directory_contents('/etc')
