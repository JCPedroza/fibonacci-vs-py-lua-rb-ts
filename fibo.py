"""
Min python version: 3.10
Run me with: python fibo.py or python3 fibo.py

Different implementations of the "find the nth Fibonacci number" algorithm,
with unit tests and time profiling.
"""

import argparse
import sys

from math import sqrt
from typing import Callable
from timeit import default_timer as timer

defaults = {"index":27  , "rounds": 10}

# Algorithms


def fibo_simple(index: int) -> int:
    """Compute nth Fibonacci number using simple recursion."""

    if index < 2:
        return index

    return fibo_simple(index - 1) + fibo_simple(index - 2)


def fibo_tailcall(index: int) -> int:
    """Compute nth Fibonacci number using tail recursion."""

    def loop(now, nxt, index):
        if index < 1:
            return now
        return loop(nxt, now + nxt, index - 1)

    return loop(0, 1, index)


def fibo_match(index: int) -> int:
    """Compute nth Fibonacci number using simple recursion and
    pattern matching.
    """

    match index:
        case 0:
            return 0
        case 1:
            return 1
        case n:
            return fibo_match(n - 1) + fibo_match(n - 2)


def fibo_memoized(index: int) -> int:
    """Compute nth Fibonacci number using memoization."""

    results: dict[int, int] = {0: 0, 1: 1}

    def loop(index):
        if index in results:
            return results[index]

        results[index] = loop(index - 1) + loop(index - 2)
        return results[index]

    return loop(index)


def fibo_forloop(index: int) -> int:
    """Compute nth Fibonacci number using a for loop."""

    now, nxt = 0, 1

    for num in range(index):
        now, nxt = nxt, now + nxt

    return now


def fibo_whileloop(index: int) -> int:
    """Compute nth Fibonacci number using a while loop."""

    now, nxt = 0, 1
    num = 0

    while num < index:
        now, nxt = nxt, now + nxt
        num += 1

    return now


def fibo_analytic(index: int) -> int:
    """Compute nth Fibonacci number using an analytic approach."""

    if index == 0:  # Otherwise f(0) = 1
        return 0

    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1 / p

    return int((p**index + q**index) / sqrt5 + 0.5)


def fibo_listcomp(index: int) -> int:
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
fibos_to_test: list[Callable] = [
    fibo_simple,
    fibo_tailcall,
    fibo_match,
    fibo_memoized,
    fibo_forloop,
    fibo_whileloop,
    fibo_analytic,
    fibo_listcomp,
    fibo_generator
]

# Printing


def fun_name_len(fun: Callable) -> int:
    """Count the number of chatacters in a function name."""
    return len(fun.__name__)


def pad_len(funs: list[Callable]) -> int:
    """Compute length of padding used to align columns during printing."""
    return fun_name_len(max(funs, key=fun_name_len))


STR_PAD_EXTRA = 1
STR_PAD = pad_len(fibos_to_test) + STR_PAD_EXTRA


def result_to_str(name: str, time: float, decimals: int = 3) -> str:
    """Convert a result into a padded string."""
    return f"{name: <{STR_PAD}} {round(time, decimals)}"


def print_result(name: str, time: float, decimals: int = 3) -> None:
    """Print result as a padded string."""
    print(result_to_str(name, time, decimals))


# Unit testing


def test(fib: Callable, verbose: bool = True) -> tuple[str, float]:
    """Run unit tests for one algorithm and print result."""

    if verbose:
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

    if verbose:
        sys.stdout.write("\033[K")  # Delete line

    return result


def test_all(fibos_to_test: list[Callable], verbose: bool = True) -> None:
    """Run all unit tests for all algorithms and print results."""

    results = []

    for fib in fibos_to_test:
        results.append(test(fib))

    sorted_results = sorted(results, key=(lambda a: a[1]))

    print("All unit tests passed!", end="\r\n")
    print("\nAlgorithms sorted by the total run time of unit tests\n")

    for name, time in sorted_results:
        print_result(name, time)
    print()


# Time profiling


def profile(fib: Callable, index: int, rounds: int, verbose: bool = True) -> float:
    "Run time profiling for one algorithm."

    if verbose:
        print(f"Profiling {fib.__name__}...", end="\r")

    start = timer()
    for _ in range(rounds):
        fib(index)
    end = timer()

    if verbose:
        sys.stdout.write("\033[K")  # Delete line

    return (end - start) * 1000


def profile_all(fibos_to_profile: list[Callable], index: int, rounds: int) -> None:
    """Run all time profiles for all algorithms and print results."""

    results = []

    for fib in fibos_to_profile:
        results.append((fib.__name__, profile(fib, index, rounds)))

    sorted_results = sorted(results, key=(lambda a: a[1]))
    print(f"\nProfile for calculating the {index} Fibonacci number")
    print(f"{rounds} consecutive times:\n")

    for name, time in sorted_results:
        print_result(name, time)
    print()


# User input


def ask_int(id: str, default: int) -> int:
    """Ask user for numeric input."""

    try:
        num = int(input(f"{id}? "))
    except:
        print(f"Not a number, default {default} will be used,")
        num = defaults[id]

    return num


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser("parser")
    parser.add_argument("--index", help="index", type=int)
    parser.add_argument("--rounds", help="rounds", type=int)

    return parser.parse_args()


def ask_params(cli_args) -> tuple[int, int]:
    """Ask user for the program parameters."""

    print()
    index = cli_args.index or ask_int("index", defaults["index"])
    rounds = cli_args.rounds or ask_int("rounds", defaults["rounds"])
    print()

    return index, rounds


# Run program

if __name__ == "__main__":
    cli_args = parse_args()
    index, rounds = ask_params(cli_args)
    test_all(fibos_to_test)
    profile_all(fibos_to_test, index, rounds)
