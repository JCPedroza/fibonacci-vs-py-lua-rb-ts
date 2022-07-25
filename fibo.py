"""
Min python version: 3.10
Run me with: python fibo.py or python3 fibo.py

Different implementations of the "find the nth Fibonacci number" algorithm,
with unit tests and time profiling.
"""

import argparse
from cmath import log
import sys

from math import sqrt
from typing import Callable
from timeit import default_timer as timer

defaults = {"index": 27, "reps": 10}

# Algorithms


def fibo_simple_if(index: int) -> int:
    """Compute nth Fibonacci number using simple recursion and if statement."""

    if index < 2:
        return index

    return fibo_simple_if(index - 1) + fibo_simple_if(index - 2)


def fibo_simple_match(index: int) -> int:
    """Compute nth Fibonacci number using simple recursion and
    pattern matching.
    """

    match index < 2:
        case True:
            return index
        case _:
            return fibo_simple_match(index - 1) + fibo_simple_match(index - 2)


def fibo_tail_call(index: int) -> int:
    """Compute nth Fibonacci number using tail call."""

    def loop(now, nxt, index):
        if index < 1:
            return now
        return loop(nxt, now + nxt, index - 1)

    return loop(0, 1, index)


def fibo_memoized(index: int) -> int:
    """Compute nth Fibonacci number using memoization."""

    results: dict[int, int] = {0: 0, 1: 1}

    def loop(index):
        if index in results:
            return results[index]

        results[index] = loop(index - 1) + loop(index - 2)
        return results[index]

    return loop(index)


def fibo_for_loop(index: int) -> int:
    """Compute nth Fibonacci number using a for loop."""

    now, nxt = 0, 1

    for _ in range(index):
        now, nxt = nxt, now + nxt

    return now


def fibo_while_loop(index: int) -> int:
    """Compute nth Fibonacci number using a while loop."""

    now, nxt = 0, 1
    num = 0

    while num < index:
        now, nxt = nxt, now + nxt
        num += 1

    return now


def fibo_binet(index: int) -> int:
    """Compute nth Fibonacci number using Binet's formula."""

    if index == 0:  # Otherwise f(0) = 1
        return 0

    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1 / p

    return int((p**index + q**index) / sqrt5 + 0.5)


def fibo_list_comp(index: int) -> int:
    """Compute nth Fibonacci number using a list comprehension."""

    # Doesn't type check, check mypy
    xs = [0, 1]
    xs += [(xs := [xs[1], xs[0] + xs[1]]) and xs[1] for k in range(index)]
    return xs[index]


def fibo_generator(index: int) -> int:
    """Compute nth Fibonacci number using a generator function."""

    def genloop():
        now, nxt = 0, 1
        while True:
            yield now
            now, nxt = nxt, now + nxt

    gen = genloop()
    for _ in range(index):
        next(gen)

    return next(gen)


# Add algorithm here to be included in unit testing and time profiling.
fibs: list[Callable] = [
    fibo_simple_if,
    fibo_tail_call,
    fibo_simple_match,
    fibo_memoized,
    fibo_for_loop,
    fibo_while_loop,
    fibo_binet,
    fibo_list_comp,
    fibo_generator,
]

# Printing


def fun_name_len(fun: Callable) -> int:
    """Count the number of chatacters in a function name."""
    return len(fun.__name__)


def pad_len(funs: list[Callable]) -> int:
    """Compute length of padding used to align columns during printing."""
    return fun_name_len(max(funs, key=fun_name_len))


STR_PAD_EXTRA = 1
STR_PAD = pad_len(fibs) + STR_PAD_EXTRA


def result_to_str(name: str, time: float, decimals: int = 3) -> str:
    """Convert a result into a padded string."""
    return f"{name: <{STR_PAD}} {round(time, decimals)}"


def print_result(name: str, time: float, decimals: int = 3) -> None:
    """Print result as a padded string."""
    print(result_to_str(name, time, decimals))


# Unit testing


def test(fib: Callable) -> tuple[str, float]:
    """Run unit tests for one algorithm and print result."""

    print(f"Testing algorithm {fib.__name__}...", end="\r")

    start = timer()

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(30) == 832_040

    end = timer()
    total = (end - start) * 1000
    result = (fib.__name__, total)

    sys.stdout.write("\033[K")  # Delete line
    return result


def test_all(fibs: list[Callable]) -> None:
    """Run all unit tests for all algorithms and print results."""

    results = []

    for fib in fibs:
        results.append(test(fib))

    sorted_results = sorted(results, key=(lambda a: a[1]))

    print("All unit tests passed!", end="\r\n")
    print("\nAlgorithms sorted by the total run time of unit tests\n")

    for name, time in sorted_results:
        print_result(name, time)
    print()


# Time profiling


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

    for fib in fibs:
        results.append((fib.__name__, profile(fib, index, reps)))

    sorted_results = sorted(results, key=lambda a: a[1])
    print(f"\nProfile for index: {index} reps: {reps}")

    for name, time in sorted_results:
        print_result(name, time)
    print()


def profile_all_range(fibs: list[Callable], begin: int, end: int, reps: int) -> None:
    """Run range profiling for all algorithms and pring results"""

    results = []

    for fib in fibs:
        results.append((fib.__name__, profile_range(fib, begin, end, reps)))

    sorted_results = sorted(results, key=lambda a: a[1])
    print(f"\nRange profile for begin: {begin} end: {end} reps: {reps}")

    for name, time in sorted_results:
        print_result(name, time)
    print()


# User input


def ask_int(label: str, default: int) -> int:
    """Ask user for numeric input."""

    try:
        num = int(input(f"{label}? "))
    except:
        print(f"Not a number, default {default} will be used,")
        num = defaults[label]

    return num


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser("parser")
    parser.add_argument("--index", help="index", type=int)
    parser.add_argument("--reps", help="reps", type=int)

    return parser.parse_args()


def ask_params(cli_args) -> tuple[int, int]:
    """Ask user for the program parameters."""

    print()
    index = cli_args.index or ask_int("index", defaults["index"])
    reps = cli_args.reps or ask_int("reps", defaults["reps"])
    print()

    return index, reps


# Run program

if __name__ == "__main__":
    cli_args = parse_args()
    index, reps = ask_params(cli_args)
    test_all(fibs)
    profile_all(fibs, index, reps)
    profile_all_range(fibs, 0, 27, 10)

# TODO range profile parameters from cli
