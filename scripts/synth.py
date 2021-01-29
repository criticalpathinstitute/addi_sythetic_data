#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-01-19
Purpose: ADDI synthetic data
"""

import argparse
import pandas as pd
from shortuuid import uuid
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    infile: TextIO
    outfile: TextIO
    max_records: int
    exclude: List[str]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='ADDI synthetic data',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-m',
                        '--max',
                        help='Maximum number of records',
                        type=int,
                        default=0)

    parser.add_argument('-x',
                        '--exclude',
                        help='Exclude fields',
                        type=str,
                        nargs='+',
                        default=['CMGRPID', 'CMSPID', 'CMLNKID'])

    args = parser.parse_args()

    return Args(args.file, args.outfile, args.max, args.exclude)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    # "low_memory" keeps Pandas quiet on mixed datatypes
    df = pd.read_csv(args.infile, low_memory=False)

    # Drop unwanted/empty columns
    drop = set(args.exclude +
               [col for col in df.columns if df[col].isnull().all()])
    df.drop(columns=drop, inplace=True)

    # Generate random values for subject ID
    nrows = df.shape[0]
    df['USUBJID'] = [uuid() for _ in range(nrows)]

    # Sample or not
    data = df.sample(args.max_records) if args.max_records else df

    # Write output
    data.to_csv(args.outfile, index=False)

    print(f'Done, wrote {data.shape[0]:,} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
