#!/usr/bin/env python3
"""coroutine that will execute async_comprehension four times in parallel
using asyncio.gather
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    """
    p = time.perf_counter()
    tasks = [i async for i in async_comprehension()]
    asyncio.gather(tasks)
    elapsed = time.perf_counter() - p


if __name__ == " __main__":
    asyncio.run(measure_runtime())
