#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times and returns a sorted list of the results.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of the wait times in ascending order.
    '''
    # Execute wait_random n times concurrently and gather the results
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    # Sort the wait times before returning
    return sorted(wait_times)
