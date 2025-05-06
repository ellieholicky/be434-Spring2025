#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-05-06
Purpose: Caesar Cipher for understanding my secret coded messages
"""
import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Caesar Shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE", type=argparse.FileType("rt"), help="Input file")

    parser.add_argument(
        "-n",
        "--number",
        metavar="NUMBER",
        type=int,
        default=3,
        help="A number to shift",
    )

    parser.add_argument(
        "-d", "--decode", action="store_true", help="Decode the message"
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
        help="Output file",
    )

    return parser.parse_args()


# --------------------------------------------------
def build_substitution_table(shift, decode=False):
    """Create sub dictionary for Caesar cipher"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alpha = (
        alpha[-shift:] + alpha[:-shift] if decode else alpha[shift:] + alpha[:shift]
    )
    return str.maketrans(alpha, shifted_alpha)


# --------------------------------------------------
def main():
    """Caesar Cipherrrrrrr"""

    args = get_args()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = args.number % 26

    # Create translation table
    trans_table = build_substitution_table(shift, decode=args.decode)

    for line in args.FILE:
        result = ""
        for char in line:
            if char.upper() in alpha:
                # take only letters, keep case by uppercasing everything
                result += char.upper().translate(trans_table)
            else:
                result += char
        print(result, end="", file=args.output)


# --------------------------------------------------
if __name__ == "__main__":
    main()
