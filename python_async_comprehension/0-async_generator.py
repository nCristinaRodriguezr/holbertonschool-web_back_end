#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""
import asyncio
import random


async def async_generator():
    """
    A coroutine that yields a random number between 0 and 10
    after waiting asynchronously for 1 second, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
