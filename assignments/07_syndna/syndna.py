#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-03-20
Purpose: Create synthetic sequences
"""

import argparse
import random
import sys


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Create synthetic sequences",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        metavar="str",
        type=argparse.FileType("wt"),  # Open file handle for writing
        default="out.fa",
        help="Output filename",
    )

    parser.add_argument(
        "-t",
        "--seqtype",
        metavar="str",
        type=str,
        choices=["dna", "rna"],
        default="dna",
        help="DNA or RNA",
    )

    parser.add_argument(
        "-n",
        "--numseqs",
        metavar="int",
        type=int,
        default=10,
        help="Number of sequences to create",
    )

    parser.add_argument(
        "-m", "--minlen", metavar="int", type=int, default=50, help="Minimum length"
    )

    parser.add_argument(
        "-x", "--maxlen", metavar="int", type=int, default=75, help="Maximum length"
    )

    parser.add_argument(
        "-p",
        "--pctgc",
        metavar="float",
        type=float,
        default=0.5,
        help="Percent GC (must be between 0 and 1)",
    )

    parser.add_argument(
        "-s", "--seed", metavar="int", type=int, default=None, help="Random seed"
    )

    args = parser.parse_args()

    # Perform manual validation for pctgc
    if not (0.0 <= args.pctgc <= 1.0):
        print(
            f'usage: --pctgc "{args.pctgc}" must be between 0 and 1', file=sys.stderr
        )  # Error message
        sys.exit(1)

    return args


def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""
    t_or_u = "T" if seq_type == "dna" else "U"  # Choose base for RNA or DNA
    num_gc = int((pctgc / 2) * max_len)  # Calculate GC bases
    num_at = int(((1 - pctgc) / 2) * max_len)  # Calculate AT bases
    pool = (
        "A" * num_at + "C" * num_gc + "G" * num_gc + t_or_u * num_at
    )  # Create the base pool
    for _ in range(max_len - len(pool)):  # Padding the pool with random bases if needed
        pool += random.choice(pool)
    return "".join(sorted(pool))  # Return sorted pool for consistency


def main():
    """Main function"""
    args = get_args()
    random.seed(args.seed)  # Set random seed

    # Create a pool of bases based on pctgc and seqtype
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    # Write sequences to the output file in FASTA format
    for i in range(args.numseqs):
        seq_len = random.randint(
            args.minlen, args.maxlen
        )  # Random length for each sequence
        seq = "".join(
            random.sample(pool, seq_len)
        )  # Randomly sample from the pool to create the sequence
        args.outfile.write(f">seq_{i + 1}\n{seq}\n")

    # Print the result summary
    print(
        f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile.name}".'
    )


if __name__ == "__main__":
    main()
