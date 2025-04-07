#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-07
Purpose: Add Your Purpose
"""
import argparse
import csv
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Filter a CSV file for a specific value",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="The CSV file to process",
        metavar="FILE",
        type=argparse.FileType("r"),
        required=True,
    )

    parser.add_argument(
        "-v", "--val", help="The value to match against", metavar="VALUE", required=True
    )

    parser.add_argument(
        "-c", "--col", help="The column name to search for the value", metavar="COLUMN"
    )

    parser.add_argument(
        "-o", "--outfile", help="Output file name", metavar="OUTFILE", default="out.csv"
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        help="Delimiter to use for parsing the file",
        metavar="DELIM",
        default=",",
    )

    return parser.parse_args()


# --------------------------------------------------
def filter_csv(file, value, column=None, delimiter=","):
    """Filter the CSV file for the given value in the optional column (case-insensitive)"""

    # Read the CSV data using DictReader
    reader = csv.DictReader(file, delimiter=delimiter)

    # Check if the column exists, if specified
    if column and column not in reader.fieldnames:
        # Adjusting the error message format to match test expectation
        print(f'--col "{column}" not a valid column!', file=sys.stderr)
        sys.exit(1)

    # Compile a regex for case-insensitive searching
    search_for = re.compile(re.escape(value), re.IGNORECASE)

    filtered_rows = []

    # Iterate through each row in the CSV file
    for row in reader:
        if column:  # If a column is specified, filter based on it
            column_value = row.get(column, "")
            if search_for.search(column_value):  # Search in the column
                filtered_rows.append(row)
        else:  # If no column is specified, search for the value anywhere
            if any(
                search_for.search(str(cell)) for cell in row.values()
            ):  # Search in any field
                filtered_rows.append(row)

    return filtered_rows


# --------------------------------------------------
def write_output(filtered_rows, output_file, fieldnames, delimiter=","):
    """Write filtered rows to the output CSV file using DictWriter"""

    with open(output_file, "w", newline="") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()  # Write the header (column names)
        writer.writerows(filtered_rows)  # Write the filtered rows


# --------------------------------------------------
def main():
    """Main function to filter CSV based on provided arguments"""

    args = get_args()

    # Open the input file
    with args.file as file:
        # Get the filtered rows
        filtered_rows = filter_csv(file, args.val, args.col, args.delimiter)

    # If there are no filtered rows, print a message and exit
    if not filtered_rows:
        print(f"No rows found with value '{args.val}'", file=sys.stderr)
        return

    # Get the column names from the first row (fieldnames)
    fieldnames = filtered_rows[0].keys()

    # Write to the output file
    write_output(filtered_rows, args.outfile, fieldnames, args.delimiter)

    # Print the success message in the desired format without printing all the data
    print(f'Done, wrote {len(filtered_rows)} to "{args.outfile}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
