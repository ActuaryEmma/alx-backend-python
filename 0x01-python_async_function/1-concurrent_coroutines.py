#!/usr/bin/env python3
"""task 1"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n, max_delay):
    delay = []
    count = 0
    while count < n:
        task = await asyncio.create_task(wait_random(max_delay))
        delay.append(task)
        count += 1
    sorted_delay = sorted(delay)
    return sorted_delay
