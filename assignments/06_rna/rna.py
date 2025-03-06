#!/usr/bin/env python3
"""
Author : Elli Holicky <ellieholicky@arizona.edu>
Date   : 2025-03-06
Purpose: Transcribe DNA into RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Transcribe DNA into RNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="+",
        type=argparse.FileType("rt"),
        help="Input DNA file(s)",
    )

    parser.add_argument(
        "-o",
        "--outdir",
        metavar="DIR",
        type=str,
        default="out",
        help="Output directory (default: out)",
    )

    return parser.parse_args()


# --------------------------------------------------
def transcribe(dna):
    """Transcribe DNA to RNA"""
    return dna.replace("T", "U").replace("t", "u")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Ensure output directory exists
    os.makedirs(args.outdir, exist_ok=True)

    total_sequences = 0
    total_files = 0

    for file in args.files:
        out_file_path = os.path.join(args.outdir, os.path.basename(file.name))

        with open(out_file_path, "wt") as out_fh:
            seq_count = 0
            for line in file:
                rna = transcribe(line.rstrip())
                out_fh.write(rna + "\n")
                seq_count += 1

            if seq_count > 0:
                total_sequences += seq_count
                total_files += 1

    seq_word = "sequence" if total_sequences == 1 else "sequences"
    file_word = "file" if total_files == 1 else "files"

    print(
        f'Done, wrote {total_sequences} {seq_word} in {total_files} {file_word} to directory "{args.outdir}".'
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
