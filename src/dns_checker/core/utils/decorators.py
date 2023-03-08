import sys
import time
import traceback

from rich.console import Console


def catch_exceptions(function):
    def func_wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as err:
            current_traceback = sys.exc_info()[-1]
            frames = traceback.extract_tb(current_traceback, 100)
            _, _, function_name, _ = tuple(frames[-1])
            Console().print(f"[red]err[/red]::{function_name}::{err}")
    return func_wrapper


def time_spent(function):
    def func_wrapper(*args, **kwargs):
        t_start = time.time()
        result = function(*args, **kwargs)
        t_end = time.time()
        return result, (t_end-t_start)*1000
    return func_wrapper
