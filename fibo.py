"""
To run me: python fibo.py or python3 fibo.py

Different implementations of the "find the nth Fibonacci number" algorithm,
with unit tests and time profiling.
"""

from math import sqrt
from typing import Callable
from timeit import default_timer as timer


def fibo_simple(index: int) -> int:
    """Compute nth Fibonacci number using simple recursion."""

    if index < 2:
        return index

    return fibo_simple(index - 1) + fibo_simple(index - 2)


def fibo_tail(index: int) -> int:
    """Compute nth Fibonacci number using tail recursion."""

    def loop(now, next, index):
        if index < 1:
            return now
        return loop(next, now + next, index - 1)

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


def fibo_memo(index: int) -> int:
    """Compute nth Fibonacci number using memoization."""

    results: dict[int, int] = {0: 0, 1: 1}

    def loop(index):
        if index in results:
            return results[index]

        results[index] = loop(index - 1) + loop(index - 2)
        return results[index]

    return loop(index)


def fibo_for(index: int) -> int:
    """Compute nth Fibonacci number using a for loop."""

    now, next = 0, 1

    for num in range(index):
        now, next = next, now + next

    return now


def fibo_analytic(index: int) -> int:
    """Compute nth Fibonacci number using an analytic approach."""

    if index == 0:  # Otherwise f(0) = 1
        return 0

    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1 / p

    return int((p ** index + q ** index) / sqrt5 + 0.5)


def fibo_comp(index: int) -> int:
    """Compute nth Fibonacci number using a list comprehension."""

    # Doesn't type check...
    xs = [0, 1]
    xs += [(xs := [xs[1], xs[0] + xs[1]]) and xs[1] for k in range(index)]
    return xs[index]


# Add algorithm here to be included in unit testing and time profiling.
fibos_to_test: list[Callable] = [
    fibo_simple,
    fibo_tail,
    fibo_match,
    fibo_memo,
    fibo_for,
    fibo_analytic,
    fibo_comp,
]


def test_fibo(fib: Callable) -> tuple[str, float]:
    """Run unit tests for one algorithm and print result."""

    print(f"\ntesting {fib.__name__}...")
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
    print(f"  ...{fib.__name__} passed all tests!")

    return result


def test_all_fibos(fibos_to_test: list[Callable]) -> None:
    """Run all unit tests for all algorithms and print results."""

    results = []

    for fib in fibos_to_test:
        results.append(test_fibo(fib))

    sorted_results = sorted(results, key=(lambda a: a[1]))
    print("\nAlgorithms sorted by the total run time of unit tests")
    print("(in rounded milliseconds):\n")

    for name, time in sorted_results:
        print(f"{name}: {round(time, 3)}")
    print()


def profile_fibo(fib: Callable, index: int, rounds: int) -> float:
    "Run time profiling for one algorithm."

    print(f"Profiling {fib.__name__}...")
    start = timer()

    for _ in range(rounds):
        fib(index)

    end = timer()
    return (end - start) * 1000


def profile_all_fibos(
    fibos_to_profile: list[Callable], index: int, rounds: int
) -> None:
    """Run all time profiles for all algorithms and print results."""
    results = []

    for fib in fibos_to_profile:
        results.append((fib.__name__, profile_fibo(fib, index, rounds)))

    sorted_results = sorted(results, key=(lambda a: a[1]))
    print("\nAlgorithms sorted by total profile time for")
    print(f"index: {index} and rounds: {rounds} (in rounded milliseconds):\n")

    for name, time in sorted_results:
        print(f"{name}: {round(time, 3)}")
    print()


defaults = {
    "index": 25,
    "rounds": 10
}


def ask_num(id):
    """Ask user for numeric input."""
    try:
        num = int(input(f"{id}? "))
    except:
        print("Not a number, default will be used...")
        num = defaults[id]

    return num


if __name__ == "__main__":
    print("\nPlease specify profile parameters:")
    index = ask_num("index")
    rounds = ask_num("rounds")

    test_all_fibos(fibos_to_test)
    profile_all_fibos(fibos_to_test, index, rounds)
