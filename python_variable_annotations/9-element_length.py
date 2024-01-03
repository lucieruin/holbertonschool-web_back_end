#!/usr/bin/env python3
"""  function’s parameters and return values with the appropriate types """


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types """
    return [(index, len(index)) for index in lst]
