#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List
import importlib

wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Argument int
    Return list
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
