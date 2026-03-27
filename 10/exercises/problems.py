"""Lecture 10 practice problems: threading, multiprocessing, and async/await.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Use only the Python standard library.
"""

from __future__ import annotations

import asyncio
import time


def simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow blocking fetch and return the same input value."""
    time.sleep(0.1)
    return value


async def async_simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow async fetch and return the same input value."""
    await asyncio.sleep(0.1)
    return value


def locked_counter_total(num_threads: int, increments_per_thread: int) -> int:
    def worker():
        nonlocal counter
        for i in range(increments_per_thread):
            with lock:
                counter += 1

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter


def threaded_square_map(values: list[int]) -> list[int]:
    results = [0] * len(values)
    def worker(index: int, value: int):
        results[index] = value * value

    threads = []
    for i, val in enumerate(values):
        t = threading.Thread(target=worker, args=(i, val))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results


def threadpool_sleep_map(delays: list[float], max_workers: int = 4) -> list[float]:
    if max_workers < 1:
        raise ValueError()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(simulated_long_fetch, delays))
    return results


def processpool_square_map(values: list[int], max_workers: int = 2) -> list[int]:
    if max_workers < 1:
        raise ValueError()

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(pow, values, itertools.repeat(2)))

    return results


async def async_tag_fetch(labels: list[str], delay: float = 0.01) -> list[str]:
    async def process_label(label: str) -> str:
        await async_simulated_long_fetch(label)
        return f"done:{label}"

    tasks = [process_label(label) for label in labels]
    return await asyncio.gather(*tasks)


async def async_blocking_double(values: list[int]) -> list[int]:
    async def process_value(val: int) -> int:
        result = await asyncio.to_thread(simulated_long_fetch, val)
        return result * 2

    tasks = [process_value(val) for val in values]
    return await asyncio.gather(*tasks)
