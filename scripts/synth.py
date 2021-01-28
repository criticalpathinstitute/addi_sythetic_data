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
from typing import NamedTuple, Optional, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    infile: TextIO
    outfile: TextIO
    max_records: int
    seed: Optional[int]


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

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        type=int,
                        default=None)

    args = parser.parse_args()

    return Args(args.file, args.outfile, args.max, args.seed)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    random.seed(args.seed)

    reader = csv.DictReader(args.infile)
    # writer = csv.DictWriter(args.outfile, fieldnames=df.columns)
    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    data = list(reader)
    random.shuffle(data)

    num_written = 0
    for i, rec in enumerate(data):
        if args.max_records and i == args.max_records:
            break

        rec['USUBJID'] = shortuuid.uuid()
        writer.writerow(rec)
        num_written += 1

    # df = pd.read_csv(args.infile)
    # for i in track(range(args.max_records or df.shape[0])):
    #     rec = {col: random.choice(df[col].fillna('')) for col in df.columns}
    #     rec['USUBJID'] = shortuuid.uuid()
    #     writer.writerow(rec)

    print(f'Done, wrote {num_written:,} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
