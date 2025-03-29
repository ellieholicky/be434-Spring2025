#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-29
Purpose: Add Your Purpose
"""
import argparse
import sys


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Find common words between two files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE1", metavar="FILE1", help="The first input file")

    parser.add_argument("FILE2", metavar="FILE2", help="The second input file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file (default: stdout)",
        metavar="FILE",
        type=argparse.FileType("w"),
        default=None,
    )

    return parser.parse_args()


def get_common_words(file1, file2):
    """Find common words between two files"""

    try:
        # Read words from file1
        with open(file1, "r") as f1:
            words1 = set(f1.read().split())

        # Read words from file2
        with open(file2, "r") as f2:
            words2 = set(f2.read().split())

        # Find common words
        common_words = sorted(words1.intersection(words2))

        return common_words
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with a non-zero status on failure


def main():
    """Main function to process the command-line arguments"""

    args = get_args()

    # Get the common words from both files
    common_words = get_common_words(args.FILE1, args.FILE2)

    # Output the common words to either stdout or a file
    if args.outfile:
        for word in common_words:
            args.outfile.write(word + "\n")
    else:
        for word in common_words:
            print(word)


if __name__ == "__main__":
    main()
