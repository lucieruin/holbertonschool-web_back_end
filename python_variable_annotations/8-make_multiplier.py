#!/usr/bin/env python3
""" type-annotated function make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return function that multiplier """
    return (lambda x: x * multiplier)
