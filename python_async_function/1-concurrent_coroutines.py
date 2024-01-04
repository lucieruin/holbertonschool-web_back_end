#!/usr/bin/env python3
""" async routine called wait_n that takes in 2 int arguments
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order """

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays in ascending order """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
