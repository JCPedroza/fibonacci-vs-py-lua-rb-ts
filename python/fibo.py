"""
Min python version: 3.10

Different implementations of the "find the nth Fibonacci number" algorithm,
with unit tests and time profiling.

(this should be for JS lol)
Number.MAX_SAFE_ITEGER is     9_007_199_254_740_991
The 78th Fibonacci number is  8_944_394_323_791_464
The 79th Fibonacci number is 14_472_334_024_676_221

This program doesn't use BigInt, so the limit for the index of these algorithms is
f(78) at best, perhaps lower for some closed-form solutions that lose accuracy at
large values.
"""

from math import sqrt
from typing import Callable

from test import test_all
from cli import parse_args, ask_params
from profile import profile_all, profile_all_range


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


def fibo_memoized_dict(index: int) -> int:
    """Compute nth Fibonacci number using memoization with dictionary."""

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


def fibo_binet(index: int) -> int:
    """Compute nth Fibonacci number using Binet's formula."""

    if index == 0:  # Otherwise f(0) = 1
        return 0

    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1 / p

    return int((p**index + q**index) / sqrt5 + 0.5)


# Add algorithm here to be included in unit testing and time profiling.
fibs: list[Callable] = [
    fibo_simple_if,
    fibo_tail_call,
    fibo_simple_match,
    fibo_memoized_dict,
    fibo_for_loop,
    fibo_while_loop,
    fibo_binet,
    fibo_list_comp,
    fibo_generator,
]


if __name__ == "__main__":
    cli_args = parse_args()
    index, reps = ask_params(cli_args)
    test_all(fibs)
    profile_all(fibs, index, reps)
    profile_all_range(fibs, 3, 27, 10)

# TODO range profile parameters from cli
