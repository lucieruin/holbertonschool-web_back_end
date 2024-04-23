#!/usr/bin/env python3
""" Write a coroutine will loop 10 times """


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ coroutin will loop 10 times """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
