#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-27
Purpose: Add Your Purpose
"""
#!/usr/bin/env python3
import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python grep",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--insensitive",
        action="store_true",
        help="Case-insensitive search (default: False)",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
        help="Output (default: STDOUT)",
    )

    parser.add_argument("pattern", metavar="PATTERN", help="Search pattern")

    parser.add_argument("files", metavar="FILE", nargs="+", help="Input file(s)")

    args = parser.parse_args()

    # Check if input files exist
    for filename in args.files:
        if not os.path.isfile(filename):
            parser.error(
                f"argument FILE: can't open '{filename}': [Errno 2] No such file or directory: '{filename}'"
            )

    return args


# --------------------------------------------------
def main():
    """Search files for lines matching PATTERN"""

    args = get_args()
    pattern = args.pattern
    files = args.files
    insensitive = args.insensitive
    out_fh = args.outfile

    # Compile the pattern with re.IGNORECASE if -i is set
    flags = re.IGNORECASE if insensitive else 0
    regex = re.compile(pattern, flags)

    multiple_files = len(files) > 1

    for filename in files:
        with open(filename, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip()
                if regex.search(line):
                    if multiple_files:
                        print(f"{filename}:{line}", file=out_fh)
                    else:
                        print(line, file=out_fh)


# --------------------------------------------------
if __name__ == "__main__":
    main()
