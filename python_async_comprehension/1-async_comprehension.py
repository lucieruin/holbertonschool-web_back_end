#!/usr/bin/env python3
""" The coroutine will collect 10 random numbers """

from typing import List
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect 10 random numbers & return numbers """
    return [number async for number in async_generator()]
