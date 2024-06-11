#!/usr/bin/env python3
'''This is task 2's module.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''a func that executes async_comprehension 4 times and measures the
    total execution time.

    Returns: float
    '''
    begin_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - begin_time
