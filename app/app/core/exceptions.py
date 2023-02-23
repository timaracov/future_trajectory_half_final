import sys, traceback
from rich.console import Console


def catch_exceptions(function):
    def func_wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            current_traceback = sys.exc_info()[-1]
            frames = traceback.extract_tb(current_traceback, 100)
            _, _, fname, _ = tuple(frames[-1])
            Console().print(f"[red]err[/red]::{fname}::{e}")
    return func_wrapper
