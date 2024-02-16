import random

import rich


def confirm(prompt: str, otherwise: callable) -> None:
    """Ask the user for confirmation and call the `otherwise` function if the user declines."""
    while True:
        rich.print(prompt, end="")
        answer = input("[yellow] [Y/n] [/yellow]").lower()

        if answer in ("y", "n") and len(answer) == 1:
            if answer == "n":
                rich.print("[yellow]WARNING[/yellow]: Operation cancelled by user.\n")
                otherwise()
            return
        rich.print(
            "[red]Fatal[/red]: Please choose [green]Y[/green] or [green]n[/green]"
        )


def check(prompt: str) -> bool:
    """Ask the user for confirmation and return True if the user confirms."""
    while True:
        rich.print(prompt, end="")
        answer = input("[yellow] [Y/n] [/yellow]").lower()

        if answer in ("y", "n") and len(answer) == 1:
            return answer == "y"
        rich.print(
            "[red]Fatal[/red]: Please choose [green]Y[/green] or [green]n[/green]"
        )


def int_input(prompt: str, default: int = None, auto_default: bool = False) -> int:
    """Ask the user for integer input."""
    while True:
        rich.print(prompt, end="")
        answer = input("")

        try:
            return int(answer)
        except Exception:
            if (default is not None) and (auto_default or answer == ""):
                return default
            rich.print(
                f"[red]Fatal[/red]: Integer is required (e.g. {random
