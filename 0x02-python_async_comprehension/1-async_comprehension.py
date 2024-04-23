#!/usr/bin/env python3
"""Async Comprehension"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    The coroutine will collect 10 random numbers using an async
    an async comprehensing over async_generator, then return the
    10 random numbers.
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
