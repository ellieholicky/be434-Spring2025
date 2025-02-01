#!/usr/bin/env python3
"""
Author : Ellie Holicky <ellieholicky@arizona.edu>
Date   : 2025-01-31
Purpose: Greetings and howdy
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting (default: Howdy)',
                        metavar='str',
                        type=str,
                        default='Howdy')
    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet (default: Stranger)',
                        metavar='str',
                        type=str,
                        default='Stranger')
    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')
    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting_arg = args.greeting
    name_arg = args.name
    excited_arg = args.excited

    print(f'{greeting_arg}, {name_arg}{"!" if excited_arg else "."}')

# --------------------------------------------------


if __name__ == '__main__':
    main()
