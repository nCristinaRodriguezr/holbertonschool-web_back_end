#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""
from typing import List
from asyncio import gather
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [num async for num in async_generator()][:10]
