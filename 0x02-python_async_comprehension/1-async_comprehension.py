#!/usr/bin/env python3
"""
Async Comprehension
"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A Coroutine that collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result


if __name__ == "__main__":
    asyncio.run(async_comprehension())
