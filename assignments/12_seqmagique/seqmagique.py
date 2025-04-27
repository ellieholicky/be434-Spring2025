#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-04-27
Purpose: Argparse Python script
"""

#!/usr/bin/env python3
"""
seqmagique.py
Summarize FASTA files with min, max, average sequence lengths and number of sequences
"""

import argparse
from typing import List, NamedTuple, TextIO
from tabulate import tabulate
from Bio import SeqIO

# --------------------------------------------------
class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    tablefmt: str

class FastaInfo(NamedTuple):
    """ FASTA file information """
    filename: str
    min_len: int
    max_len: int
    avg_len: float
    num_seqs: int

# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mimic seqmagick',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        metavar='table',
                        type=str,
                        choices=[
                            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst',
                            'mediawiki', 'latex', 'latex_raw', 'latex_booktabs'
                        ],
                        default='plain',
                        help='Tabulate table style')

    args = parser.parse_args()

    return Args(args.file, args.tablefmt)

# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()

    # List to hold all FastaInfo results
    results: List[FastaInfo] = []

    for fh in args.files:
        lengths = [len(record.seq) for record in SeqIO.parse(fh, 'fasta')]
        fh.close()  # Always good to close the file handle

        if lengths:
            min_len = min(lengths)
            max_len = max(lengths)
            avg_len = sum(lengths) / len(lengths)
            num_seqs = len(lengths)
        else:
            min_len = max_len = num_seqs = 0
            avg_len = 0.0

        results.append(FastaInfo(fh.name, min_len, max_len, avg_len, num_seqs))

    # Prepare table
    headers = ('name', 'min_len', 'max_len', 'avg_len', 'num_seqs')
    data = [(fi.filename, fi.min_len, fi.max_len, fi.avg_len, fi.num_seqs)
            for fi in results]

    print(tabulate(data, headers=headers, tablefmt=args.tablefmt, floatfmt='.2f'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
