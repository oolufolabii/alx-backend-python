#!/usr/bin/env python3

"""A python module on basics of async
    """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time: float = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
