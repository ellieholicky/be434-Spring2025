#!/usr/bin/env python3
"""
Author : Your Name <Your Email>
Date   : 2025-04-07
Purpose: Annotate and merge BLAST output with metadata annotations
"""

import re
import pandas as pd
import argparse
import os

def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Process CSV, search for a pattern, and write matching rows to an output file.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a', '--annotations',
                        help='Annotations file (input CSV file)',
                        metavar='FILE',
                        required=True)

    parser.add_argument('-o', '--outfile',
                        help='Output CSV file',
                        metavar='FILE',
                        default='out.csv')

    parser.add_argument('-p', '--pattern',
                        help='Pattern (string or regex) to search for',
                        metavar='PATTERN',
                        required=True)

    parser.add_argument('-c', '--column',
                        help='Column name to search in (default is None, searches all columns)',
                        metavar='COLUMN',
                        default=None)

    return parser.parse_args()

def process_csv(input_file, output_file, search_for, search_col=None):
    """
    Process the CSV, search for a pattern, and write matching rows to an output file using pandas.

    :param input_file: Input CSV file path
    :param output_file: Output CSV file path
    :param search_for: String or regex pattern to search for
    :param search_col: Column name to search in (default is None, searches all columns)
    """

    # Check if the file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"No such file or directory: '{input_file}'")

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # If a specific column is provided, search in that column only, otherwise search all columns
    if search_col:
        filtered_df = df[df[search_col].str.contains(search_for, case=False, na=False, regex=True)]
    else:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_for, case=False).any(), axis=1)]

    # Write the filtered data to the output CSV file
    filtered_df.to_csv(output_file, index=False)

    print(f"Processed {len(filtered_df)} records matching the search pattern.")

def main():
    """Main function to execute the process."""

    # Get command-line arguments
    args = get_args()

    # Extract values from arguments
    input_file = args.annotations
    output_file = args.outfile
    search_for = args.pattern
    search_col = args.column

    try:
        # Process the CSV file based on the arguments
        process_csv(input_file, output_file, search_for, search_col)
    except FileNotFoundError as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main()
