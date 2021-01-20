#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-01-19
Purpose: ADDI synthetic data
"""

import argparse
import csv
import pandas as pd
import random
import shortuuid
from rich.progress import track
from pprint import pprint
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    infile: TextIO
    outfile: TextIO
    max_records: int


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

    args = parser.parse_args()

    return Args(args.file, args.outfile, args.max)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    df = pd.read_csv(args.infile)
    writer = csv.DictWriter(args.outfile, fieldnames=df.columns)
    writer.writeheader()

    for i in track(range(args.max_records or df.shape[0])):
        rec = {col: random.choice(df[col]) for col in df.columns}
        rec['USUBJID'] = shortuuid.uuid()
        writer.writerow(rec)

    print(f'Done, see output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
