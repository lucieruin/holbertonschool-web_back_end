#!/usr/bin/env python3
""" async routine called wait_n that takes in 2 int arguments """

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays in ascending order """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)

    return sorted(delay)
