#!/usr/bin/env python3

'''Python Module for Async comprehension/runtime
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Run async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for num in range(4)))
    return time.time() - start_time
