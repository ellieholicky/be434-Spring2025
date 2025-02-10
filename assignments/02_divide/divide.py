#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-02-10
Purpose: Divide two numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Divide two numbers"""

    parser = argparse.ArgumentParser(
        description="Divide two numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "numbers",
        help="Numbers to divide",
        type=int,
        metavar="INT",
        nargs=2,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num1, num2 = args.numbers

    if num2 == 0:
        print("usage:divide.py [-h] INT INT")
        print("error:Cannot divide by zero, dum-dum!")
        raise SystemExit(1)

    print(f"{num1} / {num2} = {num1 // num2}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
