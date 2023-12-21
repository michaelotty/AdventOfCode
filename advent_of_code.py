"""Advent of code."""

import argparse
import subprocess
from datetime import date
from pathlib import Path


def advent_of_code() -> None:
    """Advent of code."""
    parser = argparse.ArgumentParser(
        prog="Advent of code", description="Advent of code runner"
    )

    parser.add_argument("--year", type=int, help="Year of challenge")
    parser.add_argument("--day", type=int, help="Date of challenge")

    args = parser.parse_args()

    december = date.fromisoformat("2023-12-01")
    today = date.today()

    if args.year:
        folder = Path(f"{args.year}")
    else:
        if today.month < december.month:
            folder = Path(f"{today.year-1}")
        else:
            folder = Path(f"{today.year-1}")

    if args.day:
        folder /= f"{args.day:02}"
    else:
        if today.month == december.month:
            day = today.day
        else:
            day = 1
        folder /= f"{day:02}"

    folder = folder.resolve()
    files = list(folder.rglob("*.py"))

    if not files:
        print(f"No files found in: {folder}")

    for file in files:
        print(f"Running: {file.name}")
        subprocess.call(["python", file])


if __name__ == "__main__":
    advent_of_code()
