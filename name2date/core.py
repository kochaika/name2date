"""
Core functionality for name2date.

This module provides functions to extract date and time from filenames
and update file modification times accordingly.
"""

import os
import re
import glob
from datetime import datetime, timezone

def parse_filename(filename):
    """
    Extract date and time from a filename in various formats:
    - PXL_YYYYMMDD_HHMMSSXXX.mp4 (and variations with suffixes like .NIGHT, .MP, .RESTORED, etc.)
    - PXL_YYYYMMDD_HHMMSSXXX(N).jpg (where N is a number)
    - PXL_YYYYMMDD_HHMMSSXXX_exported_0_TIMESTAMP.jpg
    - lv_0_YYYYMMDDHHMMSS.mp4

    Args:
        filename (str): The filename to parse

    Returns:
        datetime or None: A datetime object in UTC if the filename matches any of the expected patterns, None otherwise
    """
    # Regular expression to match the PXL pattern and extract date and time components
    # This handles various suffixes and variations
    pxl_pattern = r'PXL_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})(\d{3})'
    match = re.search(pxl_pattern, filename)

    if match:
        year, month, day, hour, minute, second, millisecond = map(int, match.groups())
        # Create a datetime object in UTC (as per the requirement)
        dt = datetime(year, month, day, hour, minute, second, millisecond * 1000, tzinfo=timezone.utc)
        return dt

    # Regular expression to match the lv_0_YYYYMMDDHHMMSS pattern
    lv_pattern = r'lv_0_(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})'
    match = re.search(lv_pattern, filename)

    if match:
        year, month, day, hour, minute, second = map(int, match.groups())
        # Create a datetime object in UTC (as per the requirement)
        dt = datetime(year, month, day, hour, minute, second, 0, tzinfo=timezone.utc)
        return dt

    return None


def update_file_modification_time(filepath, dt):
    """
    Update the file's modification time based on the provided datetime.

    Args:
        filepath (str): Path to the file
        dt (datetime): Datetime object to use for the modification time (in UTC)

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert to timestamp (seconds since epoch)
        timestamp = dt.timestamp()

        # Update the file's modification time
        os.utime(filepath, (timestamp, timestamp))
        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False


def process_directory(directory, verbose=0):
    """
    Process all supported files in the specified directory.

    Args:
        directory (str): Path to the directory containing files to process
        verbose (int): Verbosity level (0=quiet, 1=show skipped, 2=show all)

    Returns:
        tuple: (success_count, failure_count)
    """
    # File extensions to process
    file_extensions = ['*.mp4', '*.mov', '*.avi', '*.mkv', '*.jpg']

    success_count = 0
    failure_count = 0

    # Process each file
    for ext in file_extensions:
        for filepath in glob.glob(os.path.join(directory, ext)):
            filename = os.path.basename(filepath)

            if verbose >= 2:
                print(f"Processing {filename}...")

            dt = parse_filename(filename)
            if dt:
                if update_file_modification_time(filepath, dt):
                    success_count += 1
                    if verbose >= 2:
                        print(f"  Updated: {filename} -> {dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                else:
                    failure_count += 1
            else:
                if verbose >= 1:
                    print(f"  Skipped: {filename} (doesn't match expected pattern)")
                failure_count += 1

    return success_count, failure_count