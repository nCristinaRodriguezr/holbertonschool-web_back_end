#!/usr/bin/env python3
"""
A measure_time function with integers n and max_delay
as arguments that measures the total execution time
"""

import time
import asyncio
from typing import List
import importlib

wait_random_module = importlib.import_module('1-concurrent_coroutines')
wait_n = wait_random_module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
