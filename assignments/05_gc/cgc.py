#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-02-26
Purpose: Add Your Purpose
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Compute GC content",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="?",
        type=argparse.FileType("rt"),
        default=sys.stdin,
        help="Input sequence file (or STDIN if not provided)",
    )

    return parser.parse_args()


# --------------------------------------------------
def compute_gc_content(sequence):
    """Calculate GC content percentage"""

    sequence = sequence.upper()  # Ensure uppercase for consistency
    gc_count = sequence.count("G") + sequence.count("C")
    total_bases = len(sequence)

    return (gc_count / total_bases) * 100 if total_bases > 0 else 0


# --------------------------------------------------
def parse_fasta(file):
    """Parse a FASTA file and yield (header, sequence) pairs"""

    header = None
    sequence = []

    for line in file:
        line = line.strip()

        if line.startswith(">"):
            if header:
                yield (header, "".join(sequence))
            header = line[1:]  # Remove '>'
            sequence = []
        else:
            sequence.append(line)

    if header:
        yield (header, "".join(sequence))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    try:
        max_gc_content = -1
        max_gc_id = None

        # Parse the FASTA input (file or STDIN) and compute GC content
        for header, sequence in parse_fasta(args.file):
            gc_content = compute_gc_content(sequence)

            if gc_content > max_gc_content:
                max_gc_content = gc_content
                max_gc_id = header

        if max_gc_id is not None:
            print(f"{max_gc_id} {max_gc_content:.6f}")
        else:
            print("Error: No valid sequences found.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------
if __name__ == "__main__":
    main()
