#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-04-21
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Run-length encoding/data compression",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="DNA text or file")

    return parser.parse_args()


# --------------------------------------------------
def rle(seq: str) -> str:
    """Create RLE"""
    if not seq:
        return ""

    result = []
    prev = seq[0]
    count = 1

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            result.append(prev if count == 1 else f"{prev}{count}")
            prev = char
            count = 1

    result.append(prev if count == 1 else f"{prev}{count}")
    return "".join(result)


# --------------------------------------------------
def test_rle():
    """Test rle"""
    assert rle("A") == "A"
    assert rle("ACGT") == "ACGT"
    assert rle("AA") == "A2"
    assert rle("AAAAA") == "A5"
    assert rle("ACCGGGTTTT") == "AC2G3T4"


# --------------------------------------------------
def main():
    args = get_args()
    arg = args.text

    # Check if input is a path to a file
    if os.path.isfile(arg):
        with open(arg, "rt") as f:
            data = f.read()
    else:
        data = arg

    for seq in data.splitlines():
        print(rle(seq))


# --------------------------------------------------
if __name__ == "__main__":
    main()
