#!/usr/bin/env python3
""" import asyncio and random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """random_number is the number of second on delay"""
    random_number: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
