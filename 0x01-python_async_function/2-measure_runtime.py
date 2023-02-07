#!/usr/bin/env python3
"""
Measure runtime of asynchronous function
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for 'wait_n(n, max_delay)'
    Return -> float:
        'total_time/n'
    """
    s = time.perf_counter()
    await asyncio.gather(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed


if __name__ == '__main__':
    asyncio.run(measure_time)
