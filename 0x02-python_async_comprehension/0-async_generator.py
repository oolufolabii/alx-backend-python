#!/usr/bin/env python3
"""A python module for a coroutine
    """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generating a sequence of 10 random numbers
    """
    for num in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
