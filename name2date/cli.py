"""
Command-line interface for name2date.

This module provides the command-line interface for the name2date package.
"""

import os
import argparse
from .core import process_directory

def main():
    """Main function to parse arguments and process files."""
    parser = argparse.ArgumentParser(
        description="Update file modification dates based on their filenames."
    )
    parser.add_argument(
        "directory", 
        help="Directory containing files to process"
    )
    parser.add_argument(
        "-v", "--verbose", 
        help="Verbosity level: -v shows skipped files, -vv shows all processing details",
        action="count",
        default=0
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory")
        return

    print(f"Processing directory: {args.directory}")
    print("Expected timezone in the filenames: UTC\n")

    success, failure = process_directory(args.directory, args.verbose)

    print(f"\nSummary:")
    print(f"  Successfully processed: {success} files")
    print(f"  Failed or skipped: {failure} files")


if __name__ == "__main__":
    main()