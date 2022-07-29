import argparse
from typing import Any, Callable

defaults = {
    "index": 27,
    "reps": 10,
    "range_start": 3,
    "range_end": 27,
    "range_reps": 20,
}


def fun_name_len(fun: Callable) -> int:
    """Count the number of chatacters in a function name."""
    return len(fun.__name__)


def pad_len(funs: list[Callable]) -> int:
    """Compute length of padding used to align columns during printing."""
    return fun_name_len(max(funs, key=fun_name_len))


def result_to_str(name: str, time: float, pad: int, decimals: int = 3) -> str:
    """Convert a result into a padded string."""
    return f"{name: <{pad}} {round(time, decimals)}"


def print_result(name: str, time: float, pad: int, decimals: int = 3) -> None:
    """Print result as a padded string."""
    print(result_to_str(name, time, pad, decimals))


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
    parser.add_argument("--reps", help="repetitions", type=int)
    parser.add_argument("--range_start", help="start of range", type=int)
    parser.add_argument("--range_end", help="end of range", type=int)
    parser.add_argument("--range_reps", help="range repetitions", type=int)

    return parser.parse_args()


def ask_param(cli_args, param_key) -> int:
    args_dict = vars(cli_args)

    if args_dict[param_key] is not None:
        return args_dict[param_key]

    return ask_int(param_key, defaults[param_key])


def ask_params(cli_args) -> tuple[int, int]:
    """Ask user for the program parameters."""

    print()
    index = ask_param(cli_args, "index")
    reps = ask_param(cli_args, "reps")
    range_start = ask_param(cli_args, "range_start")
    range_end = ask_param(cli_args, "range_end")
    range_reps = ask_param(cli_args, "range_reps")
    print()

    return index, reps, range_start, range_end, range_reps
