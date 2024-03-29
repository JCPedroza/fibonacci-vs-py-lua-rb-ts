"""
Run me with python main.py
Min python version: 3.10
"""

from fibo import fibos
from test import test_all
from cli import parse_args, ask_params
from profile import profile_all, profile_all_range

if __name__ == "__main__":
    cli_args = parse_args()
    index, reps, range_start, range_end, range_reps = ask_params(cli_args)
    test_all(fibos)
    profile_all(fibos, index, reps)
    profile_all_range(fibos, range_start, range_end, range_reps)
