#!/usr/bin/env python3
""" return values with the appropriate types """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuple of item & item length """
    return [(index, len(index)) for index in lst]
