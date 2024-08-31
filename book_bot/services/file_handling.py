import os
import sys
from typing import Dict, Tuple

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: Dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    """Функция, возвращающая строку с текстом страницы и ее размер"""
    letters = ''.join([chr(letter) for letter in range(ord('А'), ord('я') + 1)]) + ' '
    result = ''.join(text[start:start + size]).rstrip(letters).rstrip('\n')
    if len(text) > len(result) + start + 1 and text[len(result) + start] in ',.!:;?':
        result = result.rstrip(',.!:;?').rstrip(letters)
    return result, len(result)


def prepare_book(path: str) -> None:
    """Функция, формирующая словарь книги"""
    with open(path, encoding='utf-8') as file:
        text = file.read()
        cur_idx = cur_page = 0
        while cur_idx < len(text):
            cur_page += 1
            page_text, page_length = _get_part_text(text, cur_idx, PAGE_SIZE)
            book[cur_page] = page_text.lstrip()
            cur_idx += page_length


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
