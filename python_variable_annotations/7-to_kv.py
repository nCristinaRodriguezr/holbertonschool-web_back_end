#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    argumen mixed int an floats
    Return: float
    """
    return (k, float(v * v))
