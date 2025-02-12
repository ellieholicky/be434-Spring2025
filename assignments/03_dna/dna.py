#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-02-12
Purpose: Tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", metavar="DNA", help="Input DNA sequence")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna_arg = args.DNA

    nucleotide_counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nucleotide in dna_arg:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    # Print counts in order A, C, G, T
    print(
        nucleotide_counts["A"],
        nucleotide_counts["C"],
        nucleotide_counts["G"],
        nucleotide_counts["T"],
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
