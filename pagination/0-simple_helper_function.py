#!/usr/bin/env python3
"""
A function named index_range that takes two
integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    Devuelve una tupla con el índice de inicio y el índice de fin
    para paginar una lista de elementos.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
