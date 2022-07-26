import sys
from typing import Callable
from timeit import default_timer as timer

from cli import print_result, pad_len


def profile(fib: Callable, index: int, reps: int) -> float:
    """Run time (ms) profiling for one algorithm."""

    print(f"Profiling {fib.__name__}...", end="\r")

    total = 0.0
    for _ in range(reps):
        start = timer()
        fib(index)
        end = timer()
        total += end - start

    sys.stdout.write("\033[K")  # Delete line
    return total * 1000


def profile_range(fib: Callable, begin: int, end: int, reps: int) -> float:
    """Profile running time (ms) of a function called with a range of arguments."""

    print(f"Profiling {fib.__name__}...", end="\r")

    total = 0.0
    for _ in range(reps):
        for index in range(begin, end):
            start = timer()
            fib(index)
            total += timer() - start

    sys.stdout.write("\033[K")  # Delete line
    return total * 1000


def profile_all(fibs: list[Callable], index: int, reps: int) -> None:
    """Run profiling for all algorithms and print results."""

    results = []
    str_pad = pad_len(fibs)

    for fib in fibs:
        results.append((fib.__name__, profile(fib, index, reps)))

    sorted_results = sorted(results, key=lambda a: a[1])
    print(f"\nProfile for index: {index} reps: {reps}")

    for name, time in sorted_results:
        print_result(name, time, str_pad)
    print()


def profile_all_range(fibs: list[Callable], begin: int, end: int, reps: int) -> None:
    """Run range profiling for all algorithms and pring results"""

    results = []
    str_pad = pad_len(fibs)

    for fib in fibs:
        results.append((fib.__name__, profile_range(fib, begin, end, reps)))

    sorted_results = sorted(results, key=lambda a: a[1])
    print(f"\nRange profile for begin: {begin} end: {end} reps: {reps}")

    for name, time in sorted_results:
        print_result(name, time, str_pad)
    print()
