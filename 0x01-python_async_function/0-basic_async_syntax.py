#!/usr/bin/env python3
"""
Basic aasync syntax
"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """
    an asynchronous coroutine that takes in an integer argument,
    waits some seconds and returns it
    """
    await asyncio.sleep(random.uniform(0, 11))
    return max_delay


if __name__ == "__main__":
    asyncio.run(wait_random())

