import sys
from typing import Callable
from timeit import default_timer as timer

from cli import print_result, pad_len


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
    str_pad = pad_len(fibs)

    for fib in fibs:
        results.append(test(fib))

    sorted_results = sorted(results, key=(lambda a: a[1]))

    print("All unit tests passed!", end="\r\n")
    print("\nAlgorithms sorted by the total run time of unit tests\n")

    for name, time in sorted_results:
        print_result(name, time, str_pad)
    print()
