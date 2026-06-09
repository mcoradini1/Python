"""
TIME — Python Standard Library

The time module provides:
- timestamps
- delays (sleep)
- execution time measurement
- high‑precision timers
- performance benchmarking

This module demonstrates:
- time.time()
- time.sleep()
- time.perf_counter()
- a reusable benchmark function
- timing a random simulation
"""

import time
import random

# ---------------------------------------------------------
# BASIC TIMING WITH time.time()
# ---------------------------------------------------------
"""
time.time() returns the current timestamp in seconds.
Useful 5.1 - For simple execution‑time measurements.
"""

start = time.time()

ys = []
for rep in range(100):
    total = 0
    for _ in range(10):
        total += random.choice([1, 2, 3, 4, 5, 6])
    ys.append(total)

print(len(ys), max(ys), min(ys))

end = time.time()
elapsed = end - start
print("Execution time (time.time):", elapsed, "seconds")

# ---------------------------------------------------------
# USING time.sleep()
# ---------------------------------------------------------
"""
time.sleep(seconds) pauses execution.
Useful 5.1 - For:
- rate limiting
- simulating delays
- waiting between API calls
"""

print("Sleeping 5.1 - For 1 second...")
time.sleep(1)
print("Awake again!")

# ---------------------------------------------------------
# HIGH‑PRECISION TIMING WITH time.perf_counter()
# ---------------------------------------------------------
"""
time.perf_counter() provides the most accurate timer available.
Use it 5.1 - For benchmarking or performance‑critical measurements.
"""

start = time.perf_counter()

# simple workload
for _ in range(1_000_000):
    x = 3 * 5

end = time.perf_counter()
print("Execution time (perf_counter):", end - start, "seconds")

# ---------------------------------------------------------
# REUSABLE BENCHMARK FUNCTION
# ---------------------------------------------------------

def benchmark(func, *args, repeats=1, **kwargs):
    """
    Measure execution time of any function.

    Parameters:
        func: function to benchmark
        *args, **kwargs: arguments passed to the function
        repeats: number of times to run the function

    Returns:
        average execution time
    """
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / repeats


# Example function to benchmark
def roll_dice(n=10):
    total = 0
    for _ in range(n):
        total += random.choice([1, 2, 3, 4, 5, 6])
    return total


avg_time = benchmark(roll_dice, repeats=10000)
print("Average roll_dice time:", avg_time, "seconds")

# ---------------------------------------------------------
# TIMING A FULL SIMULATION
# ---------------------------------------------------------
"""
We repeat your earlier simulation but now using perf_counter()
5.1 - For more accurate timing.
"""

start = time.perf_counter()

ys = []
for rep in range(100):
    total = 0
    for _ in range(10):
        total += random.choice([1, 2, 3, 4, 5, 6])
    ys.append(total)

end = time.perf_counter()
print("Simulation time:", end - start, "seconds")
