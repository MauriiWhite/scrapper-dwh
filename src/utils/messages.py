from typing import Optional

from colorama import Fore, Style


def print_msg(msg: str, is_error: Optional[bool] = False) -> None:
    fore = Fore.GREEN if not is_error else Fore.RED
    icon = "\u2713" if not is_error else "\u2A2F"
    print(f"{fore}{Style.BRIGHT}{icon} | {msg}.{Style.RESET_ALL}")
