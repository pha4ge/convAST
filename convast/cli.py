#!/usr/bin/env python
"""Defines CLI and main execution entrypoint to enable easier import
of key classes directly into other scripts"""

import argparse
from .utils import check_file_exists, initialise_logger

def generate_cli():
    """
    Create the CLI interface for the AST entrypoint
    """
    parser = argparse.ArgumentParser(
        description="Converts antibiotic susceptibility "
        "testing data to INSDC standardised format"
    )

    # takes input file and confirms it exists
    parser.add_argument("input_file", help="The input file to convert", type=check_file_exists)
    parser.add_argument(
        "-f", "--format", help="Origin of input file", required=True, choices=["VITEK"]
    )
    parser.add_argument("-o", "--output", help="The output file destination")
    return parser


def main():
    """
    CLI entrypoint
    """
    parser = generate_cli()
    args = parser.parse_args()

    if not args.output:
        args.output = args.input_file.with_suffix(".insdc.csv")

    logger = initialise_logger()

    logger.info(f"Converting {args.input_file} as {args.format} to INSDC {args.output}")
