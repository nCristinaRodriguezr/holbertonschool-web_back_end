#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
