"""General utility functions for convast"""

from pathlib import Path
import logging
import argparse


def check_file_exists(file_path):
    """
    Check if a given filepath exists
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise argparse.ArgumentTypeError(f"{file_path} does not exist")
    return file_path


def initialise_logger():
    """
    Initialise the logger to stderr
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s-%(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    return logger
