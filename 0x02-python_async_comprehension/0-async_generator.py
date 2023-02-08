#!/usr/bin/env python3
"""
Coroutine called async_generator that takes no arguments
"""
import asyncio
import random


async def async_generator():
    """
    Coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    asyncio.run(async_generator)