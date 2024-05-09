#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    argumen mixed list and integers
    Return: sum as aa float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
