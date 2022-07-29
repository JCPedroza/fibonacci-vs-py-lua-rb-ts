"""
Different implementations of the "find the nth Fibonacci number" algorithm
"""

from math import sqrt
from typing import Callable


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


# Matrix-based helpers and solutions
# http://www.oranlooney.com/post/fibonacci/


def multiply_matrix(mtrx_a, mtrx_b):
    a, b, c, d = mtrx_a
    x, y, z, w = mtrx_b

    return [
        a * x + b * z,
        a * y + b * w,
        c * x + d * z,
        c * y + d * w,
    ]


def naive_matrix_power(mtrx_a, exp):
    if exp == 0:
        return [1, 0, 0, 1]

    mtrx_b = mtrx_a[:]
    for _ in range(exp - 1):
        mtrx_b = multiply_matrix(mtrx_b, mtrx_a)

    return mtrx_b


def fibo_matrix_naive(index: int) -> int:
    """Compute nth Fibonacci number using naive matrix multiplication."""
    return naive_matrix_power([1, 1, 1, 0], index)[1]


def matrix_power(mtrx_a, exp):
    if exp == 0:
        return [1, 0, 0, 1]
    if exp == 1:
        return mtrx_a[:]

    mtrx_b = mtrx_a[:]
    num = 2

    while num <= exp:
        mtrx_b = multiply_matrix(mtrx_b, mtrx_b)
        num *= 2

    mtrx_r = matrix_power(mtrx_a, exp - num // 2)
    return multiply_matrix(mtrx_b, mtrx_r)


def fibo_matrix(index: int) -> int:
    """Compute nth Fibonacci number using matrix multiplication."""
    return matrix_power([1, 1, 1, 0], index)[1]


def fibo_branched(index: int) -> int:
    """Compute nth Fibonacci number by conditionally calling a helper function."""

    if index < 7:
        return fibo_while_loop(index)
    if index < 15:
        return fibo_for_loop(index)

    return fibo_binet(index)


# Add algorithm here to be included in unit testing and time profiling.
fibos: list[Callable] = [
    fibo_simple_if,
    fibo_tail_call,
    fibo_simple_match,
    fibo_memoized_dict,
    fibo_for_loop,
    fibo_while_loop,
    fibo_binet,
    fibo_list_comp,
    fibo_generator,
    fibo_matrix_naive,
    fibo_matrix,
    fibo_branched,
]
