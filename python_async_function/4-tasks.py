#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List
import importlib

wait_random_module = importlib.import_module('3-tasks')
task_wait_random = wait_random_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for wait_random with the given max_delay.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
