#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-02-18
Purpose: Print the reverse complement of DNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of DNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", metavar="DNA", help="Input sequence or file")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.DNA):
        with open(args.DNA, "r", encoding="utf-8") as f:
            args.DNA = f.read().rstrip()

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }

    # Reverse the sequence and apply the complement for each base
    reverse_complement = "".join(
        complement.get(base, "") for base in reversed(args.DNA)
    )

    # Output the reverse complement
    print(reverse_complement)


# --------------------------------------------------
if __name__ == "__main__":
    main()
