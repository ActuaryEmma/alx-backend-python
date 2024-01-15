#!/usr/bin/env python3
""" Takes 2 int args, waits for random delay """

import asyncio
import random
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> List[float]:
    """sorting the list of delays"""
    delay = []
    count = 0
    while count < n:
        task = await asyncio.create_task(wait_random(max_delay))
        delay.append(task)
        count += 1
    sorted_delay = sorted(delay)
    return sorted_delay
