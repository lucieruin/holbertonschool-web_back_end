#!/usr/bin/env python3
""" Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple with 1st arg is a str an 2nd a float """
    return (k, v ** 2)
