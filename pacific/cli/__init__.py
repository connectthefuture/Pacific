""" Command-line tools' entry points.
"""
import argparse


def main():
    """ Entry point for the ``pacific`` command.
    """
    parser = argparse.ArgumentParser(
        description='Manage Pacific Apps from a command line.'
        )
    args = parser.parse_args()
