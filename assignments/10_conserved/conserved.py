#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-04-14
Purpose: Show conserved bases in two or more aligned sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()

    # Read non-empty lines and strip 
    sequences = [line.strip() for line in args.FILE if line.strip()]
    args.FILE.close()

    # Check for least two sequences
    if len(sequences) < 2:
        print('Error: File must contain at least two sequences.', file=sys.stderr)
        exit(1)

    # Check sequences lengths
    length_set = set(map(len, sequences))
    if len(length_set) != 1:
        print('Error: All sequences must be of the same length.', file=sys.stderr)
        exit(1)

    # Print each sequence
    for seq in sequences:
        print(seq)

    
    conserved = ''
    for i in range(len(sequences[0])):
        chars = set(seq[i] for seq in sequences)  
                       
        conserved += '|' if len(chars) == 1 else 'X'

    print(conserved)


# --------------------------------------------------
if __name__ == '__main__':
    import sys
    main()
