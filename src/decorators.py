from functools import wraps
from typing import Callable
from os.path import dirname, join


def log(filename=None):
    """логирование функций"""
    def wapper(func: Callable):
        @wraps(func)
        def iter(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__}: completed\n')
                else:
                    print(f'{func.__name__}: completed')
            except Exception as exc_info:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__}: {str(exc_info)}. Inputs: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__}: {str(exc_info)}. Inputs: {args}, {kwargs}')
                raise
            return result

        return iter

    return wapper


# # Тестирование
# if __name__ == '__main__':  #
#     # Правильное использование декоратора
#     @log('my_log.txt')  # Декоратор с параметром
#     def text(a):
#         if a > 0:
#             return 10 / a
#         raise ValueError('отрицательное')
#
#     result = text(2)
#     print(result)
