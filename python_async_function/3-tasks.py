#!/usr/bin/env python3
"""
a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay and returns a asyncio.Task.
"""
import importlib
import asyncio

wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a asyncio.Task for wait_random with the given max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
