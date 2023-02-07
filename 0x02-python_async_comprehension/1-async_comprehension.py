#!/usr/bin/env python3
'''Python Module for Async comprehension
'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Generating a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
